import java.util.Scanner;

public class Exercise05_01 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int positives = 0; 	// Count the number of positive numbers
        int negatives = 0; 	// Count the number of negative numbers
        int count = 0;          // Count all numbers
        double total = 0;       // Accumulate a total


        // Prompt the user to enter an integer or 0 to exit
        System.out.print("Enter an integer, the input ends if it is 0: ");
        int number = input.nextInt();

        // Test for sentinel value
        while (number != 0) {
            
            // Increase positives
            if (number > 0)
                positives++;
            // Increase negatives
            else
                negatives++;	
            
            // Accumulate total
            total += number;
            // Increase the count
            count++;		
            number = input.nextInt();
        }

        // Calculate the average
        double average = total / count;

        // If only Number is 0
        if (count == 0) {	
            System.out.println("No numbers are entered except 0");
        }
        // Display results
        else
        System.out.println(
            "The number of positive is " + positives +
            "\nThe number of negatives is " + negatives +
            "\nThe total is total " + total +
            "\nThe average is " + average);
    }
    
}
