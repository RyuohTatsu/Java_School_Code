import java.util.Scanner;

public class Exercise07_03 {
	/** Main Method */
	public static void main(String[] args) {
            
            // Open Array
            int[] numbers = new int[100]; 

            // Prompt the user to enter integers between 1 and 100
            System.out.print("Enter the integers between 1 and 100: ");

            // Call Method to Count occurrence of numbers
            count(numbers);

            // Display results
            for (int i = 0; i < numbers.length; i++) {
                if (numbers[i] > 0)
                    System.out.println((i + 1) + " occurs " + numbers[i] +
                        " time" + (numbers[i] > 1 ? "s" : ""));
            }
	}

	/** Method count reads integers between 1 and 100 
	*   and counts the occurrences of each */
	public static void count(int[] numbers){
            Scanner input = new Scanner(System.in);
            // Variable to hold user input
            int num;
            
            // Loop to count occurrences
            do {
                num = input.nextInt();
                if (num >= 1 && num <= 100)	
                    numbers[num - 1]++;
            
            // Exit loop condition
            } while (num != 0);
	}
}