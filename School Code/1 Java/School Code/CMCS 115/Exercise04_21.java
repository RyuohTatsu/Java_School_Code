import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Exercise04_21 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

		// Prompt the user to enter a Social Security number
		System.out.print("Enter a SSN in the format of DDD-DD-DDDD: ");
                    String ssn = input.nextLine();

		// Check whether the input is valid
                boolean validSSN = true;{
                    Pattern pattern = Pattern.compile("^\\d{3}-\\d{2}-\\d{4}$");
                    Matcher matcher = pattern.matcher(ssn);
                    
                        if (!matcher.matches()){
                        System.out.println(ssn + " is an invalid social security number.");
                        }
                        else{
                        System.out.println(ssn + " is a valid social security number.");
                        }
                }
        }
}   

