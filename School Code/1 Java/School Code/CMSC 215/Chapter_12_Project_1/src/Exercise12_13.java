import java.io.File;
import java.util.Scanner;

public class Exercise12_13 {
	/** Main method */
	public static void main(String[] args) throws Exception {
		// Makes sure there is an actual command from the command line prompter
		if (args.length != 1) {
			System.out.println("Usage: java filename");
			System.exit(1);
		}

		// Checks if file exists
		File file = new File(args[0]);
		if (!file.exists()) {
			System.out.println("File " + args[0] + " does not exist");
			System.exit(2);
		}

		// Initialize variables
		int characters = 0; // Number of character
		int words = 0; // Number of words
		int lines = 0; // Number of lines

		// This loop will count the characters and the lines
		try (
				// Create input file
				Scanner input = new Scanner(file);) {
			while (input.hasNext()) {
				lines++;
				String line = input.nextLine();
				characters += line.length();
			}
		}

		// This loop will count the words
		try (
				// Create input file
				Scanner input = new Scanner(file);) {
			while (input.hasNext()) {
				String line = input.next();
				words++;
			}
		}

		// Displays results
		System.out.println("File " + file.getName() + " has");
		System.out.println(characters + " characters");
		System.out.println(words + " words");
		System.out.println(lines + " lines");
	}
}