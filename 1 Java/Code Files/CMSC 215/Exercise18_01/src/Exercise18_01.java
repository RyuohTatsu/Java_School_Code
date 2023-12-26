
import java.math.BigInteger;
import java.util.Scanner;

public class Exercise18_01 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		System.out.print("Enter an integer: ");
		int n = scanner.nextInt();

		if (n < 0) {
			System.out.println("Factorial is not defined for negative numbers.");
		} else {
			BigInteger result = factorial(BigInteger.valueOf(n));
			System.out.println("Factorial of " + n + " is: " + result);
		}

		scanner.close();
	}

	// Recursive method to calculate factorial using BigInteger
	public static BigInteger factorial(BigInteger n) {
		// Base case: factorial of 0 is 1
		if (n.equals(BigInteger.ZERO)) {
			return BigInteger.ONE;
		} else {
			// Recursive case: n! = n * (n-1)!
			return n.multiply(factorial(n.subtract(BigInteger.ONE)));
		}
	}
}
