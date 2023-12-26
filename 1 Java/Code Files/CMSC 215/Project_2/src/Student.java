/**
 * @author Brian Walters
 * CMSC 215
 * Assignment 2
 * Project 2
 * Class - Project1
 * November 15, 2023
 */
/**
 * This purpose of this class is to build a Student object, calculate the GPA
 * for each student, and check if the student is eligible for Honors Society. It
 * also creates a string to display the Student name and GPA.
 */
public class Student {
	/**
	 * Setting Final class variables.
	 */
	private static double GPA_THRESHOLD = 2.5;
	private final String name;
	private final int creditHours;
	private final int qualityPoints;

	/**
	 * Constructor to create Student Object.
	 */
	public Student(String name, int creditHours, int qualityPoints) {
		this.name = name;
		this.creditHours = creditHours;
		this.qualityPoints = qualityPoints;
	}

	/**
	 * Calculating GPA.
	 */
	public double calculateGpa() {
		return qualityPoints / (double) creditHours;
	}

	/**
	 * Boolean to determine if Student is Eligible for Honors Society.
	 */
	public boolean eligibleForHonorSociety() {
		return calculateGpa() >= GPA_THRESHOLD;
	}

	/**
	 * Set GPA Threshold.
	 */
	public static void setGpaThreshold(double gpaThreshold) {
		Student.GPA_THRESHOLD = gpaThreshold;
	}

	/**
	 * Get the GPA Threshold from Project2.
	 */
	public static double getGpaThreshold() {
		return GPA_THRESHOLD;
	}

	/**
	 * Create a string to print out Students who made the Honors Society.
	 *
	 * @Override
	 */
	@Override
	public String toString() {
		return "Name: " + name + "; GPA: " + String.format("%.2f", calculateGpa());
	}
}
