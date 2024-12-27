package homework.homework_1;

import javax.swing.*;
import java.awt.*;
import java.io.FileWriter;
import java.io.IOException;

/**
 *
 * @author brian
 */

public class LoginFrame extends JFrame{
    public JTextField userText;
    public JPasswordField passwordText;
    public JButton loginButton;
    public JButton resetButton;
    
    public LoginFrame() {
        // Initialize components here
        userText = new JTextField(20);
        passwordText = new JPasswordField(20);
        loginButton = new JButton("Login");
        resetButton = new JButton("Reset");
        
        // Set the title of the window
        setTitle("Login System");

        // Set the size of the window
        setSize(500, 300);

        // Set the default close operation to exit the application
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Center the window on the screen
        setLocationRelativeTo(null);

        // Create a panel to hold the components
        JPanel panel = new JPanel();
        // Use a GridBagLayout to help with centering
        panel.setLayout(new GridBagLayout());
        add(panel);
        
        // Call a method to place the components on the panel
        placeComponents(panel);

        // Make the window visible
        setVisible(true);
    }

    private void placeComponents(JPanel panel) {
    // Create a GridBagConstraints object to manage layout
    GridBagConstraints gbc = new GridBagConstraints();
    gbc.insets = new Insets(10, 10, 10, 10); // Add padding between components
    gbc.gridx = 0;
    gbc.gridy = 0;
    gbc.anchor = GridBagConstraints.CENTER;

    // Create a label for the username
    JLabel userLabel = new JLabel("User:");
    userLabel.setFont(new Font("Arial", Font.PLAIN, 18)); 
    panel.add(userLabel, gbc);

    // Create a text field for the username input
    gbc.gridx = 1;
    JTextField userText = new JTextField(20);
    userText.setFont(new Font("Arial", Font.PLAIN, 18)); 
    userText.setPreferredSize(new Dimension(200, 40)); 
    panel.add(userText, gbc);

    // Create a label for the password
    gbc.gridx = 0;
    gbc.gridy = 1;
    JLabel passwordLabel = new JLabel("Password:");
    passwordLabel.setFont(new Font("Arial", Font.PLAIN, 18)); 
    panel.add(passwordLabel, gbc);

    // Create a password field for password input
    gbc.gridx = 1;
    JPasswordField passwordText = new JPasswordField(20);
    passwordText.setFont(new Font("Arial", Font.PLAIN, 18)); 
    passwordText.setPreferredSize(new Dimension(200, 40));
    panel.add(passwordText, gbc);

    // Create a panel for the buttons to align them side by side
    gbc.gridx = 0;
    gbc.gridy = 2;
    gbc.gridwidth = 2; // Span across two columns
    JPanel buttonPanel = new JPanel();
    buttonPanel.setLayout(new FlowLayout(FlowLayout.CENTER, 20, 0)); 

    // Create a login button
    JButton loginButton = new JButton("Login");
    loginButton.setFont(new Font("Arial", Font.BOLD, 18)); 
    loginButton.setPreferredSize(new Dimension(120, 50)); 
    buttonPanel.add(loginButton);

    // Create a reset button
    JButton resetButton = new JButton("Reset");
    resetButton.setFont(new Font("Arial", Font.BOLD, 18)); 
    resetButton.setPreferredSize(new Dimension(120, 50)); 
    buttonPanel.add(resetButton);

    panel.add(buttonPanel, gbc);
    
        // Add action listener for the login button
        loginButton.addActionListener(e -> {
            boolean success = performLogin(userText.getText(), new String(passwordText.getPassword()));
            if (success) {
                JOptionPane.showMessageDialog(this, "Login Successful!");
                logAttempt(userText.getText(), true);
            } else {
                JOptionPane.showMessageDialog(this, "Login Failed!");
                logAttempt(userText.getText(), false);
            }
        });

        // Add action listener for the reset button
        resetButton.addActionListener(e -> {
            userText.setText(null);
            passwordText.setText(null);
        });
    }

    // New method to perform login and return a boolean
    public boolean performLogin(String username, String password) {
        // Hard-coded credentials for demonstration purposes
        String correctUsername = "admin";
        String correctPassword = "password123";

        return username.equals(correctUsername) && password.equals(correctPassword);
    }

    public void logAttempt(String username, boolean success) {
        try (FileWriter writer = new FileWriter("Log.txt", true)) {
            writer.write("Username: " + username + ", ");
            writer.write("Date/Time: " + new java.util.Date() + ", ");
            writer.write("Success: " + success + "\n");
        } catch (IOException ex) {
            // Notify the user about the logging error (optional)
            System.out.println("An error occurred while trying to log the attempt.");
        }
    }
    
    public static void main(String[] args) {
        // Start the LoginFrame window
        new LoginFrame(); 
    }
}
