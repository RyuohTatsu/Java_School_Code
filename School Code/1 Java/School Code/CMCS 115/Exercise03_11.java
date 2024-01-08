import java.util.Scanner;
//Class
public class Exercise03_11 {
    //Main Function
    public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
        // Get month from user.
        System.out.print("Enter a month:  ");
        int month = input.nextInt();
        //Get year from user.
        System.out.print("Enter a year:  ");
        int year = input.nextInt();
        // Leap year formula
        boolean leapYear = ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0));
        // Switch Statement to get month and number of days.
        switch (month){
        case 1 : {
            String monthName = "January";
            System.out.println(monthName + " " + year + " has 31 days");
            break;
            }
        case 3 : {
            String monthName = "March";
            System.out.println(monthName + " " + year + " has 31 days");
            break;
            }
        case 5 : {
            String monthName = "May";
            System.out.println(monthName + " " + year + " has 31 days");
            break;
            }
        case 7 : {
            String monthName = "July";
            System.out.println(monthName + " " + year + " has 31 days");
            break;
            }
        case 8 : {
            String monthName = "August";
            System.out.println(monthName + " " + year + " has 31 days");
            break;
            }
        case 10 : {
            String monthName = "October";
            System.out.println(monthName + " " + year + " has 31 days");
            break;
            }
        case 12 : {
            String monthName = "December";
            System.out.println(monthName + " " + year + " has 31 days");
            break;
            }
        case 4 : {
            String monthName = "April";
            System.out.println(monthName + " " + year + " has 30 days");
            break;
            }
        case 6 : {
            String monthName = "June";
            System.out.println(monthName + " " + year + " has 30 days");
            break;
            }
        case 9 : {
            String monthName = "September";
            System.out.println(monthName + " " + year + " has 30 days");
            break;
            }
        case 11 : {
            String monthName = "November";
            System.out.println(monthName + " " + year + " has 30 days");
            break;
            }
        //Leap year month.
        case 2 : {
            String monthName = "February";
            //If Statement to determine Leap Year.
                if(leapYear){
                    System.out.println(monthName + " " + year + " has 29 days");
                }
                else{
                    System.out.println(monthName + " " + year + " has 28 days");}
            }
        }
            }
}
