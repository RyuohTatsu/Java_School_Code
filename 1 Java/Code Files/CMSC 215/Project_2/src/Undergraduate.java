/**
 * @author Brian Walters
 * CMSC 215
 * Assignment 2
 * Project 2
 * Class - Project1
 * November 15, 2023
 */
/**
 * This purpose of this class is to add year to the Student object and determine
 * if the Undergrad is eligible for Honors Society. It will also add the year
 * onto the Student String.
 */
class Undergraduate extends Student {
	/**
	 * Initiate final value for Undergrad Year.
	 */
	private final String year;

	/**
	 * Constructor to add year into the Student Object.
	 */
	public Undergraduate(String name, int creditHours, int qualityPoints, String year) {
		super(name, creditHours, qualityPoints);
		this.year = year;
	}

	/**
	 * This will ensure the eligible undergrad students are a Junior or Senior to be
	 * eligible for Honors Society.
	 *
	 * @Override
	 */
	@Override
	public boolean eligibleForHonorSociety() {
		return (calculateGpa() >= Student.getGpaThreshold()) && (year.equals("Junior") || year.equals("Senior"));
	}

	/**
	 * This String will add the Undergrad Year to the Student String.
	 *
	 * @Override
	 */
	@Override
	public String toString() {
		return super.toString() + "; Year: " + year;
	}
}
