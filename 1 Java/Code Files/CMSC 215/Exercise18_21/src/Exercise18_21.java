import java.util.Scanner;

public class Exercise18_21 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		// Prompt the user to enter a decimal number
		System.out.print("Enter a decimal number: ");
		int decimalNumber = scanner.nextInt();

		// Convert the decimal number to binary and display the result
		String binaryEquivalent = dec2Bin(decimalNumber);
		System.out.println("Binary equivalent: " + binaryEquivalent);

		scanner.close();
	}

	// Recursive method to convert a decimal number to binary
	public static String dec2Bin(int value) {
		// Base case: if the value is 0 or 1, return its string representation
		if ((value == 0) || (value == 1)) {
			return Integer.toString(value);
		} else {
			// Recursive case: convert the quotient to binary and append the remainder
			int quotient = value / 2;
			int remainder = value % 2;
			return dec2Bin(quotient) + Integer.toString(remainder);
		}
	}
}
