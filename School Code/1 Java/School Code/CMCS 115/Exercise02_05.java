/*
(Financial application: calculate tips) Write a program that reads the subtotal
and the gratuity rate, then computes the gratuity and total. For example, if the
user enters 10 for subtotal and 15% for gratuity rate, the program displays $1.5
as gratuity and $11.5 as total.
*/
import java.util.Scanner;

public class Exercise02_05 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);	// Create new Scanner object.

		// Prompt the user to enter the subtotal
		System.out.print("Enter the subtotal: ");
		double subtotal = input.nextDouble();
                // Prompt the user to enter the gratuity rate
                System.out.print("Enter the gratuity rate: ");
		double gratuityRate = input.nextDouble();

		// Calculate gratuity and total
		double gratuity = subtotal * (gratuityRate / 100.0);
		double total = subtotal + gratuity;

		// Display results
		System.out.println("The gratuity is $" + (int)(gratuity * 100) / 100.0 +
			" and total is $" + (int)(total * 100) / 100.0);
	}
}