import java.io.FileWriter;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class AuditLog {

    private static final String FILE_PATH = "logger.txt";

    /**
     * Logs a login attempt to a separate text file.
     * 
     * @param username The username of the user attempting to login.
     * @param success  True if the login attempt was successful, false otherwise.
     * @throws IOException If any error occurs during file writing.
     */
    public static void logLoginAttempt(String username, boolean success) throws IOException {
        String timestamp = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(new Date());
        String message = String.format("%s: Login attempt for user '%s' - %s", timestamp, username,
                success ? "Success" : "Failed");
        FileWriter writer = new FileWriter(FILE_PATH, true); // Append to existing log
        writer.write(message + "\n");
        writer.close();
    }
}
