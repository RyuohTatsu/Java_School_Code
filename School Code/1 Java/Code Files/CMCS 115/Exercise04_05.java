import java.util.Scanner;

public class Exercise04_05 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

                // Welcome message.
                System.out.println("Calculate the area of a Polygon by entering the following data.");
                // Prompt the user to enter the number of sides  
		System.out.print("Enter the number of sides: ");
		int sides = input.nextInt();
                // Prompt user to enter the length of the sides
		System.out.print("Enter the length of the sides: ");
		double sideLength = input.nextDouble();

		// Compute the area of a regular polygon
		double area = (sides * Math.pow(sideLength, 2) / 
			(4 * Math.tan(Math.PI / sides)));

		// Display result
		System.out.println("The area of the polygon is " + area);
        }  
}
