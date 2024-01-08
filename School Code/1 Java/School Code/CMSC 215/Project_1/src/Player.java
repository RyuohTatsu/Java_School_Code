
/**
 * @author Brian Walters
 * CMSC 215
 * Assignment 1
 * Project 1
 * Class - Player
 * October 26, 2023
 */

/**
 * This purpose of this class is to take the input values from Project1 class.
 * Store Values into an array. Returns a string with the correct labels and
 * values of players.
 */
class Player extends Project1 {

	private final String NAME;
	private final int AGE;

	private final Height HEIGHT;

	/**
	 * Constructs a new Player object with the given name, height, and age.
	 *
	 * @param name   The player's name.
	 * @param height The player's height.
	 * @param age    The player's age.
	 */
	public Player(String name, int age, Height height) {
		this.NAME = name;
		this.AGE = age;
		this.HEIGHT = height;
	}

	/**
	 *
	 * @return The player's name.
	 */
	public String getName() {
		return NAME;
	}

	/**
	 *
	 * @return The player's age.
	 */
	public int getAge() {
		return AGE;
	}

	/**
	 *
	 * @return The player's height.
	 */
	public Height getHeight() {
		return HEIGHT;
	}

	/**
	 *
	 * @return A string representation of the player.
	 */
	@Override
	public String toString() {
		return "Player [Name: " + NAME + ", Age: " + AGE + ", Height: " + HEIGHT.toString() + "]";
	}

}