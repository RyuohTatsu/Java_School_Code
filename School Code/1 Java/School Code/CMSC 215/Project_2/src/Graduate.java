/**
 * @author Brian Walters
 * CMSC 215
 * Assignment 2
 * Project 2
 * Class - Project1
 * November 15, 2023
 */
/**
 * This purpose of this class is to add the degree to the Student object and
 * determine if the Graduate student is eligible for Honors Society. It will
 * also add the degree to the end of the Student String.
 */
class Graduate extends Student {
	/**
	 * Initialize the degreeSought final variable.
	 */
	private final String degreeSought;

	/**
	 * Constructor to add degree into the Student Object.
	 */
	public Graduate(String name, int creditHours, int qualityPoints, String degreeSought) {
		super(name, creditHours, qualityPoints);
		this.degreeSought = degreeSought;
	}

	/**
	 * This will ensure the eligible graduate students are in a masters degree to be
	 * eligible for Honors Society.
	 *
	 * @Override
	 */
	@Override
	public boolean eligibleForHonorSociety() {
		return (calculateGpa() >= Student.getGpaThreshold()) && degreeSought.equals("Masters");
	}

	/**
	 * This String will add the Graduate degree to the Student String.
	 *
	 * @Override
	 */
	@Override
	public String toString() {
		return super.toString() + "; Degree Sought: " + degreeSought;
	}
}
