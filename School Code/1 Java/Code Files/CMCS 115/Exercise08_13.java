import java.util.Scanner;

public class Exercise08_13 {
    /** Main method */
    public static void main(String[] args) {
        // Create a Scanner
        Scanner input = new Scanner(System.in);

        // Prompt the user to enter size of a two-dimensional array 
        System.out.print("Enter the number of rows and columns of the array: ");
        int row = input.nextInt();
        int column = input.nextInt();
        
        // Create Array    
        double[][] numbersArray = new double[row][column];

        // Prompt the user to enter the array
        System.out.println("Enter the array:");
        for (int i = 0; i < numbersArray.length; i++) {
            for (int j = 0; j < numbersArray[i].length; j++) {
                numbersArray[i][j] = input.nextDouble();
            }
        }

        // Get the location of the largest element
        int[] location = locateLargest(numbersArray);

        // Display results
        System.out.println("The location of the largest element is at (" +
            location[0] + ", " + location[1] + ")");
    }

    /** locateLargest returns the location of the 
        largest element in a two-dimensional array*/
    public static int[] locateLargest(double[][] a) {
        
        // Create Variables
        int[] location = new int[] { 0, 0 };
        double largest = a[0][0];
        
        // Loop to check for largest
        for (int i = 0; i < a.length; i++) {

            for (int k = 0; k < a[i].length; k++) {

                if (a[i][k] > largest) {
                    location[0] = i; // row
                    location[1] = k; // column
                    largest = a[i][k];
                }

            }
        }
        // Return Largest location
        return location;
    }
}