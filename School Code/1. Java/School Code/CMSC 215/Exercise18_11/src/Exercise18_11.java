import java.util.Scanner;

public class Exercise18_11 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		System.out.print("Enter an integer: ");
		long num = scanner.nextLong();

		int result = sumDigits(num);

		System.out.println("The sum of the digits is: " + result);

		scanner.close();
	}

	// Recursive method to calculate the sum of the digits
	public static int sumDigits(long n) {
		// Base case: if n is a single-digit number, return the digit itself
		if (n < 10) {
			return (int) n;
		} else {
			// Recursive case: sum of digits = last digit + sum of digits in the remaining
			// part
			return (int) (n % 10) + sumDigits(n / 10);
		}
	}
}
