package Exercise09_01;

/**
 *
 * @author brian
 */
public class Exercise09_01 {
    /** Main method */
    public static void main(String[] args) {
        // Create a Rectangle with width 4 and height 40
        Rectangle rectangle1 = new Rectangle(4, 40);

        // Create a Rectangle with width 3.5 and height 35.9
        Rectangle rectangle2 = new Rectangle(3.5, 35.9);

        // Create a Rectangle with width 6.9 and height 10.2
        Rectangle rectangle3 = new Rectangle(6.9, 10.2);

        // Display the width, height, area, and perimeter of rectangle1
        System.out.println("The area of a rectangle with width " + rectangle1.width + " height " + rectangle1.height + " is " + rectangle1.getArea());
        System.out.println("The perimeter of a rectangle is " + rectangle1.getPerimeter());

        // Display the width, height, area, and perimeter of rectangle2
        System.out.println("The area of a rectangle with width " + rectangle2.width + " height " + rectangle2.height + " is " + rectangle2.getArea());
        System.out.println("The perimeter of a rectangle is " + rectangle2.getPerimeter());

        // Display the width, height, area, and perimeter of rectangle2
        System.out.println("The area of a rectangle with width " + rectangle3.width + " height " + rectangle3.height + " is " + rectangle3.getArea());
        System.out.println("The perimeter of a rectangle is " + rectangle3.getPerimeter());
    }
}
