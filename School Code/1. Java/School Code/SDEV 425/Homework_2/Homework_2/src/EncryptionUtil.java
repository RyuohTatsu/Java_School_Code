import java.util.Base64;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;

public class EncryptionUtil {

    // **IMPORTANT SECURITY NOTE:** This code uses a hardcoded key for demonstration
    // purposes only.
    // In a real-world application, you should never hardcode sensitive data like
    // encryption keys.
    // Consider using environment variables or secure key management solutions.
    private static final String KEY = "0123456789abcdef0123456789abcdef"; // This should be stored in a secure
                                                                          // environment.
    private static final String ALGORITHM = "AES";

    /**
     * Encrypts a plain text string using the AES algorithm with the specified key.
     * 
     * @param value The plain text string to encrypt.
     * @return The encrypted string in Base64 encoding.
     * @throws Exception If any error occurs during encryption.
     */
    public static String encrypt(String value) throws Exception {
        byte[] keyBytes = KEY.getBytes();
        SecretKeySpec key = new SecretKeySpec(keyBytes, ALGORITHM);
        Cipher cipher = Cipher.getInstance(ALGORITHM);
        cipher.init(Cipher.ENCRYPT_MODE, key);
        byte[] encryptedValue = cipher.doFinal(value.getBytes());
        return Base64.getEncoder().encodeToString(encryptedValue);
    }

    /**
     * Decrypts an encrypted string using the AES algorithm with the specified key.
     * 
     * @param encryptedValue The encrypted string in Base64 encoding.
     * @return The decrypted plain text string.
     * @throws Exception If any error occurs during decryption.
     */
    public static String decrypt(String encryptedValue) throws Exception {
        byte[] keyBytes = KEY.getBytes();
        SecretKeySpec key = new SecretKeySpec(keyBytes, ALGORITHM);
        Cipher cipher = Cipher.getInstance(ALGORITHM);
        cipher.init(Cipher.DECRYPT_MODE, key);
        byte[] decryptedValue = cipher.doFinal(Base64.getDecoder().decode(encryptedValue));
        return new String(decryptedValue);
    }
}
