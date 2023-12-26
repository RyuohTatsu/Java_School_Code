import java.util.ArrayList;
import java.util.Scanner;

/**
 * @author Brian Walters
 * CMSC 215
 * Assignment 1
 * Project 1
 * Class - Project1
 * October 26, 2023
 */
/**
 * This purpose of this class is to prompt user for input values: Player Name,
 * Age, Height. Find average age of players. Find tallest player whose age is
 * less than or equal to the average age. Output the average age and the tallest
 * player equal to or under the average age.
 */

public class Project1 {

	public static void main(String[] args) {

		/**
		 * Create an ArrayList to store player information
		 */
		ArrayList<Player> players = new ArrayList<>();
		/**
		 * Create a Scanner to read player information from the console
		 */
		Scanner scanner = new Scanner(System.in);

		/**
		 * Create variable playerInfo
		 */
		String playerInfo = "M";

		/**
		 * While the user is still entering information
		 */
		while (!playerInfo.isEmpty()) {

			/**
			 * Prompt the user for player information
			 */
			System.out.println("Enter Player Name, Age, and Height (Feet space then inches). Example is: Joe 34 5 10");

			/**
			 * Get the player information from the user
			 */
			playerInfo = scanner.nextLine();

			/**
			 * Split the player information into name, age, and height
			 */
			String[] playerInfoParts = playerInfo.split(" ");

			/**
			 * Check if the input is valid
			 */
			if ((playerInfoParts.length != 4) || !isValidName(playerInfoParts[0]) || !isValidAge(playerInfoParts[1])
					|| !isValidFeet(playerInfoParts[2]) || !isValidInches(playerInfoParts[3])) {

				/**
				 * If the input is not valid, print an error message and prompt the user to
				 * enter again
				 */
				System.out.println("Input format wrong. Try again with example: Joe 34 5 10");
			}

			else {
				/**
				 * Create a new Height object
				 */
				Height height = new Height(Integer.parseInt(playerInfoParts[2]), Integer.parseInt(playerInfoParts[3]));

				/**
				 * Create a new Player object and add it to the ArrayList
				 */
				Player player = new Player(playerInfoParts[0], Integer.parseInt(playerInfoParts[1]), height);
				players.add(player);
			}
		}

		/**
		 * Close the scanner
		 */
		scanner.close();

		/**
		 * Calculate the total age of all players
		 */
		int totalAge = 0;
		for (Player player : players) {
			totalAge += player.getAge();
		}

		/**
		 * Calculate the average age of all players
		 */
		double averageAge = (double) totalAge / players.size();

		/**
		 * Find the tallest player whose age is less than or equal to the average age of
		 * all players
		 */
		Player tallestPlayer = null;
		for (Player player : players) {
			if (player.getAge() <= averageAge) {
				if ((tallestPlayer == null) || (tallestPlayer.getHeight().toInches() < player.getHeight().toInches())) {
					tallestPlayer = player;
				}
			}
		}

		/**
		 * Print the average age of all players
		 */
		System.out.println("The average age of all players is: " + averageAge);
		System.out.println();

		/**
		 * Print the information of the tallest player whose age is less than or equal
		 * to the average age of all players
		 */
		System.out.println("The tallest player whose age is less than or equal to the average age of all players is:");
		System.out.println();

		System.out.println(tallestPlayer);
		System.out.println();

		System.out.println("The list of Players on the team is:");

		/**
		 * Print the list of players from the array
		 */
		for (int i = 0; i < players.size(); i++) {
			System.out.println(players.get(i));
		}
	}

	/**
	 *
	 * @param playerName
	 * @return
	 */
	private static boolean isValidName(String playerName) {
		return (playerName != null) && !playerName.isEmpty();
	}

	/**
	 *
	 * @param playerAge
	 * @return
	 */
	private static boolean isValidAge(String playerAge) {
		int age;
		try {
			age = Integer.parseInt(playerAge);
		} catch (NumberFormatException e) {
			return false;
		}
		return ((age >= 12) && (age <= 95));
	}

	/**
	 *
	 * @param playerInches
	 * @return
	 */
	private static boolean isValidInches(String playerInches) {
		int inches;
		try {
			inches = Integer.parseInt(playerInches);
		} catch (NumberFormatException e) {
			return false;
		}
		return ((inches >= 0) && (inches < 12));
	}

	/**
	 *
	 * @param playerFeet
	 * @return
	 */
	private static boolean isValidFeet(String playerFeet) {
		int feet;
		try {
			feet = Integer.parseInt(playerFeet);
		} catch (NumberFormatException e) {
			return false;
		}
		return ((feet >= 4) && (feet <= 10));
	}
}
