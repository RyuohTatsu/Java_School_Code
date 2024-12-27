
/**
 *
 */

import java.util.Scanner;

/**
 *
 */
public class Exercise12_07 {

	/**
	 * @param args
	 */

	public static void main(String[] args) throws NumberFormatException {
		@SuppressWarnings("resource")
		Scanner input = new Scanner(System.in);
		System.out.print("Enter an Integer: ");
		String binaryString = input.nextLine();
		bin2Dec(binaryString);
	}

	public static int bin2Dec(String binaryString) {
		int decimal = 0;
		for (int i = 0, j = binaryString.length() - 1; i < binaryString.length(); i++, j--) {
			if ((binaryString.charAt(i) < '0') || (binaryString.charAt(i) > '1')) {
				throw new NumberFormatException("Not a binary string: " + binaryString);
			}
			decimal += (Integer.parseInt(String.valueOf(binaryString.charAt(i)))) * Math.pow(2, j);
		}
		return decimal;
	}
}
