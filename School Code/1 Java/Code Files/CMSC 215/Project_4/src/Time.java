import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * @author Brian Walters
 * CMSC 215
 * Assignment 4
 * Project 4
 * Class - Time
 * December 12, 2023
 */

/**
 * This class represents a time with hours, minutes, and meridian (AM or PM).
 * Implements the Comparable interface to enable comparison between Time
 * objects.
 */
public class Time implements Comparable<Time> {

	private final int hours;
	private final int minutes;
	private final String meridian;

	/**
	 * Constructs a Time object with specified hours, minutes, and meridian.
	 */
	public Time(int hours, int minutes, String meridian) throws InvalidTime {
		// Check validity of hours, minutes, and meridian

		this.hours = hours;
		this.minutes = minutes;
		this.meridian = meridian;
	}

	/**
	 * Constructs a Time object from a string representation in the format "HH:MM
	 * AM/PM".
	 */
	public Time(String timeString) throws InvalidTime {
		StringBuilder errorMessages = new StringBuilder(); // StringBuilder to accumulate error messages
		int errorCount = 0;

		// Define a regular expression for the expected format (HH:MM AM/PM)
		String timeRegex = "^(1[0-2]|0?[1-9]):([0-5][0-9]) (AM|PM)$";

		// Create a Pattern object
		Pattern pattern = Pattern.compile(timeRegex);

		// Create a Matcher object
		Matcher matcher = pattern.matcher(timeString);

		// Check if the input matches the general format
		if (!matcher.matches()) {
			// Provide more detailed error messages based on specific issues

			// Check if the format contains ":" between hours and minutes
			if (timeString.indexOf(":") == -1) {
				errorMessages.append("Invalid format. ':' should be between HH:MM.\n");
				errorCount++;
			}

			// Check if the hours are not between 1 and 12
			if (!timeString.matches(".*\\b(1[0-2]|0?[1-9]):.*")) {
				errorMessages.append("Invalid hours. Hours must be between 1 and 12.\n");
				errorCount++;
			}

			// Check if the minutes are not between 00 and 59
			if (!timeString.matches(".*:([0-5][0-9])\\b.*")) {
				errorMessages.append("Invalid minutes. Minutes must be between 00 and 59.\n");
				errorCount++;
			}

			// Check if the meridian is not "AM" or "PM"
			if (!timeString.matches(".*\\b(AM|PM)\\b.*")) {
				errorMessages.append("Invalid meridian. Meridian must be either 'AM' or 'PM'.\n");
				errorCount++;
			}

			// If more than one issue, throw a general message
			if (errorCount > 1) {
				throw new InvalidTime("Invalid input: Multiple errors.");
			}

			// If there's only one error, print the original error message
			if (errorCount == 1) {
				throw new InvalidTime(errorMessages.toString());
			}
		}

		// Parse hours, minutes, and meridian from the matched groups
		int parsedHours = Integer.parseInt(matcher.group(1));
		int parsedMinutes = Integer.parseInt(matcher.group(2));
		String parsedMeridian = matcher.group(3);

		// Assign values to instance variables
		this.hours = parsedHours;
		this.minutes = parsedMinutes;
		this.meridian = parsedMeridian;
	}

	/**
	 * @return the hours
	 */
	public int getHours() {
		return hours;
	}

	/**
	 * @return the minutes
	 */
	public int getMinutes() {
		return minutes;
	}

	/**
	 * @return the meridian
	 */
	public String getMeridian() {
		return meridian;
	}

	/**
	 * Compares two Time objects for order.
	 */
	@Override
	public int compareTo(Time other) {
		// Compare hours
		if (this.hours != other.hours) {
			return Integer.compare(this.hours, other.hours);
		}

		// If hours are equal, compare minutes
		if (this.minutes != other.minutes) {
			return Integer.compare(this.minutes, other.minutes);
		}

		// If hours and minutes are equal, compare meridian
		return this.meridian.compareTo(other.meridian);
	}

	/**
	 * Returns the string representation of the time in the format "HH:MM AM/PM".
	 */
	@Override
	public String toString() {
		// Implement the toString method to return the string representation (HH:MM
		// AM/PM)
		// Example: 10:30 AM
		return String.format("%02d:%02d %s", hours, minutes, meridian);
	}

	/**
	 * Converts a Time instance to a Date instance.
	 */
	public Date toDate() throws ParseException {
		SimpleDateFormat dateFormat = new SimpleDateFormat("hh:mm a");
		return dateFormat.parse(String.format("%02d:%02d %s", hours, minutes, meridian));
	}
}
