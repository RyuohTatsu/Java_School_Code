/**
 * This class reads email addresses from a text file with improved security
 * measures.
 *
 * @author Jim (improved by Bard)
 * 
 * Modified by Brian Walters
 * Class: SDEV 425 / Spring 2024
 * Professor : Justin Boswell
 * Homework 1
 * 
 */
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.regex.Pattern;

public class SDEV425_2 {

    private static final Pattern ALLOWED_FILENAME_PATTERN = Pattern.compile("^[a-zA-Z0-9_.-]+$");

    /**
     * Main method that reads email addresses from a file.
     *
     * @param args the command line arguments. The first argument should be the
     *             filename.
     */
    public static void main(String[] args) {
        if (args.length == 0) {
            System.err.println("Error: Please provide a filename as a command line argument.");
            return;
        }

        String filename = validateFilename(args[0]);
        if (filename == null) {
            System.err.println("Error: Invalid filename provided.");
            return;
        }

        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            System.out.println("Email Addresses:");
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            System.err.println("Error reading file: " + e.getMessage());
            e.printStackTrace(); // Log stack trace for debugging
        }
    }

    /**
     * Validates the filename to prevent path traversal attacks.
     *
     * @param filename the filename to validate
     * @return the validated filename or null if invalid
     */
    private static String validateFilename(String filename) {
        // Restrict allowed characters using regular expression
        if (!ALLOWED_FILENAME_PATTERN.matcher(filename).matches()) {
            return null;
        }
        // Additional checks can be added here, like checking directory restrictions
        return filename;
    }
}
