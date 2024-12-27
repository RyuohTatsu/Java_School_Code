import homework.homework_1.LoginFrame;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class LoginFrameTest {

    private LoginFrame frame;

    @BeforeEach
    public void setUp() {
        frame = new LoginFrame();
        frame.setVisible(true);
        assertEquals("", frame.userText.getText());
        assertEquals("", new String(frame.passwordText.getPassword()));
    }

    @Test
    public void testSuccessfulLogin() {
        boolean loginResult = frame.performLogin("admin", "password123");
        assertTrue(loginResult, "The login should be successful.");
    }

    @Test
    public void testUnsuccessfulLogin() {
        boolean loginResult = frame.performLogin("admin", "wrongpassword");
        assertFalse(loginResult, "The login should fail with incorrect credentials.");
    }

    @Test
    public void testLogging() {
        // Use the absolute path to the log file
        String logFilePath = "C:\\Users\\brian\\2. Code\\School Code\\1. Java\\School Code\\CYOP 460\\Homework_1\\Log.txt";

        // Directly call the logAttempt method with test data
        frame.logAttempt("testUser", true);

        // Check if the log file contains the expected entry
        try (BufferedReader reader = new BufferedReader(new FileReader(logFilePath))) {
            String logEntry = reader.readLine();
            assertNotNull(logEntry, "Log entry should not be null");
            assertTrue(logEntry.contains("Username: testUser"), "Log entry should contain the username");
            assertTrue(logEntry.contains("Success: true"), "Log entry should indicate a successful login");
        } catch (IOException e) {
            fail("Could not read the log file.");
        }
    }

    @Test
    void testResetButton() {
        // Set some initial values in the text fields
        frame.userText.setText("Brian");
        frame.passwordText.setText("password");

        // Trigger the reset button action
        frame.resetButton.doClick();

        // Verify that the fields are empty after reset
        assertTrue(frame.userText.getText().isEmpty());
        assertTrue(new String(frame.passwordText.getPassword()).isEmpty());
    }
}
