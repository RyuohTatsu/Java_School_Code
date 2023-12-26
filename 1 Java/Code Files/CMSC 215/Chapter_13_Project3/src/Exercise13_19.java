
/**
 * @author Brian Walters
 * CMSC 215
 * Assignment 2
 * Project 2
 * Class - Project1
 * November 17, 2023
 */

import java.util.Scanner;

public class Exercise13_19 {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.print("Enter a decimal number: ");
		String decimalValue = input.next();

		try {
			System.out.println("The fraction number is " + decimalToFraction(decimalValue));
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}

		input.close();
	}

	/**
	 * Converts a decimal number to a fraction.
	 *
	 * @param decimalValue The decimal number to convert.
	 * @return The equivalent fraction.
	 * @throws Exception If the provided input is not a valid decimal number.
	 */
	private static String decimalToFraction(String decimalValue) throws Exception {
		boolean isNegative = decimalValue.startsWith("-");

		String[] decimalNumberParts = decimalValue.split("\\.");
		if (decimalNumberParts.length != 2) {
			throw new Exception("You must enter a decimal number like: 123.12");
		}

		if (decimalNumberParts[0].isEmpty() || decimalNumberParts[1].isEmpty()) {
			throw new Exception("Invalid decimal number format.");
		}

		long leftSideOfDecimal = Long.parseLong(decimalNumberParts[0]);
		Rational rightSideOfDecimal = new Rational(Long.parseLong(decimalNumberParts[1]),
				(long) Math.pow(10, decimalNumberParts[1].length()));

		Rational result = new Rational(leftSideOfDecimal, 1).add(rightSideOfDecimal);
		return (isNegative ? "-" : "") + result.toString();
	}
}
