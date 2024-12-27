import java.util.Scanner;

public class Exercise18_11_b {

	public static void main(String[] args) {

		@SuppressWarnings("resource")
		Scanner input = new Scanner(System.in);
		long number;

		System.out.print("Enter an integer: ");
		number = input.nextLong();

		System.out.println("The sum of all digits is: " + sumDigits(number));

	}

	public static int sumDigits(long num) {
		char[] numArray = Long.toString(num).toCharArray();
		return sumDigits(numArray, String.valueOf(num).length());
	}

	public static int sumDigits(char[] numbers, int length) {
		if (length == 1) {
			return Integer.parseInt(String.valueOf(numbers[0]));
		} else {
			return Integer.parseInt(String.valueOf(numbers[length - 1])) + sumDigits(numbers, length - 1);
		}

	}
}
