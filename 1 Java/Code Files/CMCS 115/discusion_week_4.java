import java.util.Scanner;
    
public class discusion_week_4 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        // Initialize variables
        int sumDistance = -500;
        int brakeMarker = -1;
        int brakePressure = -1;
               
        // Start a do loop that will exculte at least one time before checking the while loop at the bootom to see if the condition was met to exit loop.
        do {
            
            // Get random braking marker
            brakeMarker = (int) (Math.random() * (200 - 150 + 1) + 150); 
            System.out.println("A child jumps into the street " + brakeMarker + " meeters in frount of you." );
            System.out.println("This simulation will repeat until you guess the perfect distance or hit enter 0." );

            // Prompt.Get user response for Brake Pressure.
            System.out.print("How much pressure will you apply to stop before hitting the child? "
                    + "Please enter a pressure between 50 and 100 percent. ");
            brakePressure = input.nextInt();
            
            // Intial feedback on the braking pressure applied.
            if (brakePressure > 50){
                if (brakePressure > 95)
                    System.out.println("You have applied the brakes to hard and locked the wheels to slide into the child.");
                else
                    System.out.println("You have chosen " + brakePressure + " braking pressure.");
            }
            else {
                System.out.println("You didn't apply enough brake pressure and ran over the child.");
            }
            
            // Calculate the stopping distance
            sumDistance = (brakeMarker - 100) - brakePressure;
            
            // Print results
            if (sumDistance < 0){
                System.out.println("You stopped with plenty of room to spare.");
            }
            else if (sumDistance > 0){
                System.out.println("You did not stop in time to save the child's life.");       
            }
            else if (sumDistance == 0) {
                System.out.println("Perfect stop. You are a Hero.");  
            }
        
        // While to hold the termination conditions after the do loop has run at least once.
        } while (brakePressure !=0 && sumDistance != 0);
    }

}
    

