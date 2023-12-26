import java.util.Scanner;

public class Exercise03_23 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		// Prompt the user to enter a point (x, y)
                System.out.println("Enter two integers to find out if the point is in the rectangle.");
		System.out.print("Enter width x: ");
		double x = input.nextDouble();
		System.out.print("Enter hight y: ");
		double y = input.nextDouble();
		// Display results
                if (x <= (10.0 / 2.0) && x >= (-10.0 / 2.0) && y <= (5.0 / 2.0) && y >= (-5.0 / 2.0))
                    System.out.println("Point (" + x + ", " + y + ") is in the rectangle");
                else
                    System.out.println("Point (" + x + ", " + y + ") is not in the rectangle");
	}
}
