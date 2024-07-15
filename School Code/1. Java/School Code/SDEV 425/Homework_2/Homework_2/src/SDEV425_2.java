/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author jim Adopted from Oracle's Login Tutorial Application
 *         https://docs.oracle.com/javafx/2/get_started/form.htm
 * 
 *         Modified by Brian Walters
 *         Class: SDEV 425 / Spring 2024
 *         Professor : Justin Boswell
 *         Homework 2
 * 
 * 
 */

import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.GridPane;
import javafx.scene.paint.Color;
import javafx.scene.text.Text;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.Random;

/**
 * JavaFX application for a secure login with multi-factor authentication (MFA)
 * via email.
 */
public class SDEV425_2 extends Application {
    private static int loginAttempts = 0; // Counter for unsuccessful login attempts
    private static final int MAX_ATTEMPTS = 3; // Maximum allowed login attempts

    /**
     * Starts the JavaFX application, initializing the login interface.
     *
     * @param primaryStage The primary stage for the JavaFX application.
     */
    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("SDEV425 Login");
        GridPane grid = new GridPane();
        grid.setAlignment(Pos.CENTER);
        grid.setHgap(10);
        grid.setVgap(10);

        Text scenetitle = new Text("Welcome. Login to continue.");
        grid.add(scenetitle, 0, 0, 2, 1);

        Label userName = new Label("User Name:");
        grid.add(userName, 0, 1);

        TextField userTextField = new TextField();
        grid.add(userTextField, 1, 1);

        Label pw = new Label("Password:");
        grid.add(pw, 0, 2);

        PasswordField pwBox = new PasswordField();
        grid.add(pwBox, 1, 2);

        // Add email field for multi-factor authentication
        Label emailLabel = new Label("Email:");
        grid.add(emailLabel, 0, 3);

        TextField emailField = new TextField();
        grid.add(emailField, 1, 3);

        Button btn = new Button("Login");
        grid.add(btn, 1, 4);

        final Text actiontarget = new Text();
        grid.add(actiontarget, 1, 6);

        // System Use Notification
        Text systemUseNotification = new Text("By using this system, you agree to our terms of use.");
        grid.add(systemUseNotification, 0, 5, 2, 1);

        btn.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent e) {
                String username = userTextField.getText();
                String password = pwBox.getText();
                String email = emailField.getText();
                boolean isValid = authenticate(username, password);

                try {
                    // Log the login attempt
                    AuditLog.logLoginAttempt(username, isValid);
                } catch (IOException ex) {
                    ex.printStackTrace();
                }

                if (isValid) {
                    loginAttempts = 0; // Reset counter on successful login
                    // Multi-factor Authentication
                    String securityCode = sendSecurityCode(email);
                    displaySecurityCodePrompt(primaryStage, username, securityCode);
                } else {
                    loginAttempts++;
                    if (loginAttempts >= MAX_ATTEMPTS) {
                        actiontarget.setFill(Color.FIREBRICK);
                        actiontarget.setText("Account locked due to too many failed login attempts.");
                    } else {
                        actiontarget.setFill(Color.FIREBRICK);
                        actiontarget.setText("Please try again.");
                    }
                }
            }
        });

        Scene scene = new Scene(grid, 500, 400);
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    /**
     * Main method to launch the JavaFX application.
     *
     * @param args Command line arguments.
     */
    public static void main(String[] args) {
        launch(args);
    }

    /**
     * Authenticates the user by verifying the username and password.
     *
     * @param user  The username entered by the user.
     * @param pword The password entered by the user.
     * @return true if the username and password are authenticated, false otherwise.
     */
    public boolean authenticate(String user, String pword) {
        try {
            String storedPassword = UserCredentials.retrievePassword(user);
            return storedPassword != null && storedPassword.equals(pword);
        } catch (Exception e) {
            e.printStackTrace();
            return false;
        }
    }

    /**
     * Sends a security code to the user's email for multi-factor authentication.
     *
     * @param email The email address of the user to send the security code.
     * @return The security code sent to the user's email.
     */
    private String sendSecurityCode(String email) {
        Random random = new Random();
        String securityCode = String.format("%04d", random.nextInt(10000));
        try {
            System.out.println(securityCode); // Very bad practice. Not allowed!!!!!!
            JavaMail.sendEmail(email, securityCode);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return securityCode;
    }

    /**
     * Displays a prompt for the user to enter the security code received via email.
     *
     * @param primaryStage The primary stage of the JavaFX application.
     * @param username     The username of the user logging in.
     * @param securityCode The security code sent to the user's email.
     */
    private void displaySecurityCodePrompt(Stage primaryStage, String username, String securityCode) {
        GridPane grid = new GridPane();
        grid.setAlignment(Pos.CENTER);
        grid.setHgap(10);
        grid.setVgap(10);

        Label codeLabel = new Label("Enter Security Code:");
        grid.add(codeLabel, 0, 1);

        TextField codeField = new TextField();
        grid.add(codeField, 1, 1);

        Button btn = new Button("Submit");
        grid.add(btn, 1, 4);

        final Text actiontarget = new Text();
        grid.add(actiontarget, 1, 6);

        btn.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent e) {
                if (codeField.getText().equals(securityCode)) {
                    grid.setVisible(false);
                    GridPane grid2 = new GridPane();
                    grid2.setAlignment(Pos.CENTER);
                    grid2.setHgap(10);
                    grid2.setVgap(10);
                    Text scenetitle = new Text(
                            "Welcome " + username + "! You are Entering Very Secret Rabbit Hunting Territory!");
                    grid2.add(scenetitle, 0, 0, 2, 1);
                    Scene scene = new Scene(grid2, 500, 400);
                    primaryStage.setScene(scene);
                    primaryStage.show();
                } else {
                    actiontarget.setFill(Color.FIREBRICK);
                    actiontarget.setText("Invalid security code. Please try again.");
                }
            }
        });

        Scene scene = new Scene(grid, 500, 400);
        primaryStage.setScene(scene);
        primaryStage.show();
    }
}