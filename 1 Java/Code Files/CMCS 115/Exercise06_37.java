import java.util.Scanner;

public class Exercise06_37 {
	/** Main Method */
	public static void main(String[] args) {
            // Create a Scanner
            Scanner input = new Scanner(System.in); 

            // Prompt the user to enter a number and its width
            System.out.print("Enter a number and its width: ");
            int number = input.nextInt();
            int width = input.nextInt();
            
            // Call format Method
            format(number, width);
	}

	/** Method format returns a string for the number with one or more prefix 0s */
	public static void format(int number, int width) {
            // String representation for the number
            String num = number + ""; 

            // If the number is shorter than the width format
            // Else return the string representation for the number
            if (num.length() < width) {
                for (int i = width - num.length(); i > 0; i--) {
                    num = 0 + num;
                }
            }
        // Display a string of formatted number
        System.out.println(number + " formatted to width " + width + ": " + num);
	}
}

