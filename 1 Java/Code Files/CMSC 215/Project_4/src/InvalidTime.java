/**
 * @author Brian Walters
 * CMSC 215
 * Assignment 4
 * Project 4
 * Class - InvalidTime
 * December 12, 2023
 */

/**
 * This Class will allow you to throw exceptions with a custom error message
 * when something goes wrong during time validation.
 */
public class InvalidTime extends Exception {

	/**
	 * I have no idea why I was getting the following warning but this was a fix
	 * that I found. "The serializable class InvalidTime does not declare a static
	 * final serialVersionUID field of type long"
	 */
	private static final long serialVersionUID = -3931349844227927801L;

	// Instance variable to store the error message
	public InvalidTime(String message) {
		super(message);
	}

	// Getter method to retrieve the error message
	@Override
	public String getMessage() {
		return super.getMessage();
	}
}
