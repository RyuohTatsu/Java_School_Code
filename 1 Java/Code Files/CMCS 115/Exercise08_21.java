import java.util.Scanner;


public class Exercise08_21 {
 
    // Main method
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        // Prompt user for number of cities
        System.out.println("Enter the number of cities: ");
            int numberOfCities = input.nextInt();
            // New Array
            double[][] n = new double[numberOfCities][2];
        
        // Prompt user for coordinates for cities
        System.out.println("Enter the coordinates of the cities:");
        // Loop to fill array with all coordinates
        for (int i = 0; i < n.length; i++) {
            n[i][0] = input.nextDouble();
            n[i][1] = input.nextDouble();
        }
        
        // Call method for total distance from center city
        double[] sumOfDis = calSomeOfDis(calDis(n));
        // Call method for finding center city
        int cityIndex = findMin(sumOfDis);

        // Display results
        System.out.println("The central city is at (" + n[cityIndex][0] + "," +  n[cityIndex][1] + ")");
        System.out.printf("The total distance to all other cities is " + "%.2f" , sumOfDis[cityIndex]);
    }
 
    // Method to plot coordinates 
    public static double[][] calDis(double[][] n) {
        // Calculate distances from cities and put them in square matrix.
        double[][] distances = new double[n.length][n.length];
        
        for (int i = 0; i < distances.length; i++) {
            for (int j = 0; j < distances.length; j++) {
                double x1 = n[i][0];
                double x2 = n[j][0];
                double y1 = n[i][1];
                double y2 = n[j][1];
                distances[i][j] = Math.sqrt(Math.pow(x1 - x2, 2)
                  + Math.pow(y1 - y2, 2));
            }
        }
        return distances;
    }
    // Method to calculate total distance to center city
    public static double[] calSomeOfDis(double[][] n) {
 
        double[] sum = new double[n.length];
 
        for (int i = 0; i < sum.length; i++) {
            for (int j = 0; j < sum.length; j++) {
            sum[i] += n[i][j];
            }
 
        }
        return sum;
    }
    // Method to find center city
    public static int findMin(double[] n) {
 
        double min = n[0];
        int minIndex = 0;
        
        for (int i = 0; i < n.length; i++) {
            if (min > n[i]) {
            min = n[i];
            minIndex = i;
            }
        }
        return minIndex;
    }
}