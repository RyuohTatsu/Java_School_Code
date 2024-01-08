
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

/**
 * @author Brian Walters
 * CMSC 215
 * Assignment 2
 * Project 2
 * Class - Project1
 * November 15, 2023
 */
/**
 * This purpose of this class is to read in a .txt file. It then splits each
 * line of the file into parts that are separated for use. An arraylist is
 * created to store the data. Average GPA is calculated. The threshold for the
 * GPA to make Honors Society is set and displayed. The Students who are
 * eligible are displayed.
 */
public class Project2 {
	/**
	 * Set the path to the file to be read.
	 */
	private static final String FILE_NAME = "students_base.txt";

	/**
	 * Main method to call the methods to run the program.
	 */
	public static void main(String[] args) throws IOException {
		ArrayList<Student> students = readStudentsFromFile();
		double averageGpa = calculateAverageGpa(students);
		setGpaThreshold(averageGpa);
		printEligibleStudents(students);
	}

	/**
	 * This method will create an arraylist from a text file.
	 */
	private static ArrayList<Student> readStudentsFromFile() throws IOException {
		ArrayList<Student> students = new ArrayList<>();
		/**
		 * This try will look for the file. If the file is not found it will throw an
		 * IOException.
		 */
		try (Scanner scanner = new Scanner(new File(FILE_NAME))) {
			/**
			 * This while loop will read in the data from the text file and separate the
			 * data into 4 pieces of data: name, credithours, qualitypoints, and year for
			 * Undergrads or degree for Grads.
			 */
			while (scanner.hasNextLine()) {
				String line = scanner.nextLine();
				String[] studentInput = line.split(" ");
				String name = studentInput[0];
				int creditHours = Integer.parseInt(studentInput[1]);
				int qualityPoints = Integer.parseInt(studentInput[2]);
				String finalValue = studentInput[3];
				/**
				 * If / else to separate Undergraduates from Graduates by the final value of the
				 * input.
				 */
				if (finalValue.equals("Freshman") || finalValue.equals("Sophomore") || finalValue.equals("Junior")
						|| finalValue.equals("Senior")) {
					students.add(new Undergraduate(name, creditHours, qualityPoints, finalValue));
				} else {
					students.add(new Graduate(name, creditHours, qualityPoints, finalValue));
				}
			}
			/**
			 * Close Scanner
			 */
			scanner.close();
		}
		return students;
	}

	/**
	 * This method will calculate the average GPA of all the students.
	 */
	private static double calculateAverageGpa(ArrayList<Student> students) {
		double totalGpa = 0;

		for (Student student : students) {
			totalGpa += student.calculateGpa();
		}
		return totalGpa / students.size();
	}

	/**
	 * This methods purpose is to set the GPA threshold and display the result.
	 */
	private static void setGpaThreshold(double averageGpa) {
		Student.setGpaThreshold((averageGpa + 4.0) / 2.0);
		System.out.println(
				"GPA threshold for Honor Society membership: " + String.format("%.2f", Student.getGpaThreshold()));
	}

	/**
	 * This method will display the Students who are Eligible for the Honor Society
	 * by running a for loop.
	 */
	private static void printEligibleStudents(ArrayList<Student> students) {
		System.out.println("\nEligible students for Honor Society membership:");

		for (Student student : students) {
			if (student.eligibleForHonorSociety()) {
				System.out.println(student.toString());
			}
		}
	}
}
