import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

/**
 * @author Brian Walters
 * CMSC 215
 * Assignment 4
 * Project 4
 * Class - Interval
 * December 12, 2023
 */

/**
 * Represents an interval with start and end values of a generic type.
 * Implements the Comparable interface to enable comparison between Interval
 * objects.
 */
public class Interval implements Comparable<Interval> {

	private final Date start;
	private final Date end;

	/**
	 * Constructs an Interval object with the specified start and end dates.
	 */
	public Interval(Date start, Date end) {
		this.start = start;
		this.end = end;
	}

	/**
	 * Checks if the interval contains a specific date.
	 */
	public boolean contains(Date value) {
		return (start.compareTo(value) <= 0) && (end.compareTo(value) >= 0);
	}

	/**
	 * Checks if the interval is a subinterval of another interval.
	 */
	public boolean subinterval(Interval other) {
		return (start.compareTo(other.start) >= 0) && (end.compareTo(other.end) <= 0);
	}

	/**
	 * Checks if the interval overlaps with another interval.
	 */
	public boolean overlaps(Interval other) {
		return (start.compareTo(other.end) <= 0) && (end.compareTo(other.start) >= 0);
	}

	/**
	 * Compares this interval with another interval based on their start dates.
	 */
	@Override
	public int compareTo(Interval other) {
		return start.compareTo(other.start);
	}

	/**
	 * Creates a new Interval object with the specified start and end dates, and
	 * validates that the end date is after the start date.
	 */
	public static Interval createInterval(Date start, Date end) throws InvalidTime {
		if (start.compareTo(end) > 0) {
			throw new InvalidTime("End must be after start");
		}
		return new Interval(start, end);
	}

	/**
	 * Parses a string representation of time into a Date object.
	 */
	public static Date parseDate(String timeString) throws ParseException {
		SimpleDateFormat dateFormat = new SimpleDateFormat("hh:mm a");
		return dateFormat.parse(timeString);
	}
}