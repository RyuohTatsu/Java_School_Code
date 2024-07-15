import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class helloworld {

  public static void main(String[] args) {
    // Get current date and time
    LocalDateTime now = LocalDateTime.now();
    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
    String formattedTime = formatter.format(now);

    // Print formatted message
    System.out.println("Hello, World!");
    System.out.println(formattedTime);
    System.out.println("Brian Walters (Developer)");
    System.out.println("Greetings, I am looking forward to SDEV 425.");
    System.out.println("I am excited to learn what this class has to offer.");
  }
}