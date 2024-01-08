import java.util.Scanner;
public class discusion_week_7 {
        /** Main method */
    public static void main(String[] args) {
        // Create a Scanner
        Scanner input = new Scanner(System.in);

        // Prompt the user to enter size of a two-dimensional array 
        System.out.print("Enter the number of items in your list twice: ");
        int row = input.nextInt();
        int column = input.nextInt();
        
        // Create Array    
        double[][] sample = new double[row][column];

        // Prompt the user to enter the item number and price
        System.out.println("Enter the item # and price:");
        for (int i = 0; i < sample.length; i++) {
            for (int j = 0; j < sample[i].length; j++) {
                sample[i][j] = input.nextDouble();
            }
        }
    }
            /** Main method */
    public class NameSorting {

        public static void main(String[] args) {
            Scanner input = new Scanner(System.in);
            //single dimensional array
            String[] array = new String[20];
            //ask for names
            System.out.println("Please enter 20 names to sort");              
            Scanner s1 = new Scanner(System.in);
            for (int i = 0; i < 20; i++) {
                array[i] = s1.nextLine();
            }

            //display list
            System.out.println(array[0]);
        }
    }
}   
