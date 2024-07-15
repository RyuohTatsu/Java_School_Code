import java.io.FileWriter;
import java.nio.file.Files;
import java.nio.file.Paths;

public class UserCredentials {

    private static final String FILE_PATH = "user_credentials.txt";

    /**
     * Saves user credentials (username and password) to a text file.
     * 
     * @param username The username of the user.
     * @param password The plain text password of the user.
     * @throws Exception If any error occurs during file writing or encryption.
     * 
     *                   *****Hashing and salting would add an extra layer of
     *                   security in this step!
     */

    public static void saveCredentials(String username, String password) throws Exception {

        String encryptedPassword = EncryptionUtil.encrypt(password); // Encrypt plain text password (not secure)
        String content = username + ":" + encryptedPassword;
        FileWriter writer = new FileWriter(FILE_PATH);
        writer.write(content);
        writer.close();
    }

    /**
     * Retrieves the encrypted password for a given username from the text file.
     * 
     * @param username The username of the user.
     * @return The decrypted password if the username is found, otherwise null.
     * @throws Exception If any error occurs during file reading or decryption.
     */
    public static String retrievePassword(String username) throws Exception {
        String content = new String(Files.readAllBytes(Paths.get(FILE_PATH)));
        String[] credentials = content.split(":");
        if (credentials[0].equals(username)) {
            return EncryptionUtil.decrypt(credentials[1]);
        }
        return null;
    }
}
