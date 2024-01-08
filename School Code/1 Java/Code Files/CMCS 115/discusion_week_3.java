import java.util.Scanner;
public class discusion_week_3 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        // Prompt.Get user response for Breaking Marker.
        System.out.print("Pick a breaking marker. 200 meters to 100 meters? ");
        int brakeDistance = input.nextInt();
        if (brakeDistance > 99)
            if (brakeDistance > 200)
                System.out.print("You are breaking to early and will cause a crash.");
            else
                System.out.print("You have chosen the " + brakeDistance + " braking marker.");
        else
            System.out.print("You missed the last marker and you will crash.");
    }

}
