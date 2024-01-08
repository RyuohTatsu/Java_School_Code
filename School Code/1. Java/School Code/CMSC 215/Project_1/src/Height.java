
/**
 * @author Brian Walters
 * CMSC 215
 * Assignment 1
 * Project 1
 * Class - Height
 * October 26, 2023
 */
/**
 * This purpose of this class is to take the height value from the array in
 * Player class. Convert the Feet and Inches into an total inches Object. Have a
 * toString method for converting the total inches into a Feet and Inches string
 * for output.
 */
class Height extends Project1 {

	private final int FEET;
	private final int INCHES;

	/**
	 * Constructs a new Height object with the given feet and inches.
	 *
	 * @param feet   The number of feet in the height.
	 * @param inches The number of inches in the height.
	 */
	public Height(int feet, int inches) {
		this.FEET = feet;
		this.INCHES = inches;
	}

	/**
	 * @return the fEET
	 */
	public int getFEET() {
		return FEET;
	}

	/**
	 * @return the iNCHES
	 */
	public int getINCHES() {
		return INCHES;
	}

	/**
	 *
	 * @return The total height in inches.
	 */
	public int toInches() {
		return (FEET * 12) + INCHES;
	}

	/**
	 *
	 * @return A string representation of the height.
	 */
	@Override
	public String toString() {
		return FEET + "'" + convertInches(INCHES) + "\"";
	}

	/**
	 * Normalizes the inches to be less than 12.
	 *
	 * @param inches The number of inches.
	 * @return The normalized inches.
	 */

	private int convertInches(int inches) {
		inches %= 12;
		if (inches < 0) {
			inches += 12;
		}
		return inches;
	}
}
