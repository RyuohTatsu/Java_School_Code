/**
 *
 * @author brian
 */
public class discusion_week_8 {

// Beer Class.Java
	public class Beer {
		// Data Fields
		private String type = "";
		private int size = 0;
		private static int numberOfBeers = 0;

		// Constructor
		public Beer(String beerType) {
			this.setType(beerType);
			discusion_week_8.Beer.numberOfBeers++;
		}

		// Get number of types of beer
		public static int numberOfBeers() {
			return numberOfBeers;
		}

		// Get pack size
		public void setPackSize(int packSize) {
			this.size = packSize;
		}

		// Return Size
		public double getPackSize() {
			return size;
		}

		public String getType() {
			return type;
		}

		public void setType(String type) {
			this.type = type;
		}
	}

// Main Class.Java
	static class Main {
		public static void main(String[] args) {

			Beer beer1 = new Beer("Sapporo");
			Beer beer2 = new Beer("Asahi");
			beer1.setPackSize(6);
			beer2.setPackSize(12);
			System.out.println("The size of the pack of beer1 is " + beer1.getPackSize());
			System.out.println("There are " + Beer.numberOfBeers() + " types of beer stored.");
		}
	}
}
