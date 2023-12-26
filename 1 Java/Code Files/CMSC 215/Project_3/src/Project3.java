import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ComboBox;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

/**
 * @author Brian Walters
 * CMSC 215
 * Assignment 3
 * Project 3
 * Class - Project3
 * November 28, 2023
 */

/**
 * This class will construct a GUI for a Trip Cost Estimator. The GUI will ask
 * for user input for Distance, Gasoline Cost, Gas Mileage, Number of Days,
 * Hotel Cost per Day, Food Cost per day, Attraction Cost per day. Once the user
 * inputs the data and hits the calculate button the total trip cost will be
 * displayed. The embedded immutable TripCost class will create an object and
 * calculate the totals to be displayed.
 *
 */

public class Project3 extends Application {
	/**
	 * Make Text Fields and ComboBoxes
	 */
	private final static TextField distanceField = new TextField();
	private final ComboBox<String> distanceUnitComboBox = new ComboBox<>();

	private final static TextField gasolineCostField = new TextField();
	private final ComboBox<String> gasolineCostUnitComboBox = new ComboBox<>();

	private final static TextField gasMileageField = new TextField();
	private final ComboBox<String> gasMileageUnitComboBox = new ComboBox<>();

	private final static TextField numDaysField = new TextField();

	private final static TextField hotelCostField = new TextField();

	private final static TextField foodCostField = new TextField();

	private final static TextField attractionsCostField = new TextField();

	private final TextField totalCostField = new TextField();

	private final Button calculateButton = new Button("Calculate");

	private TripCost tripCost;

	/**
	 * Start Stage
	 */

	@Override
	public void start(Stage primaryStage) throws Exception {

		// Create GridPane for UI
		GridPane gridPane = new GridPane();
		gridPane.setHgap(10);
		gridPane.setVgap(10);
		gridPane.setPadding(new Insets(10, 10, 10, 10));

		// Add labels, text fields, and combo boxes to HBoxes
		gridPane.add(new Label("Distance:"), 0, 0);
		gridPane.add(distanceField, 1, 0);
		gridPane.add(distanceUnitComboBox, 2, 0);

		gridPane.add(new Label("Gasoline Cost:"), 0, 1);
		gridPane.add(gasolineCostField, 1, 1);
		gridPane.add(gasolineCostUnitComboBox, 2, 1);

		gridPane.add(new Label("Gas Mileage:"), 0, 2);
		gridPane.add(gasMileageField, 1, 2);
		gridPane.add(gasMileageUnitComboBox, 2, 2);

		gridPane.add(new Label("Number of Days:"), 0, 3);
		gridPane.add(numDaysField, 1, 3);

		gridPane.add(new Label("Hotel Cost:"), 0, 4);
		gridPane.add(hotelCostField, 1, 4);

		gridPane.add(new Label("Food Cost:"), 0, 5);
		gridPane.add(foodCostField, 1, 5);

		gridPane.add(new Label("Attractions:"), 0, 6);
		gridPane.add(attractionsCostField, 1, 6);

		// Add button to GridPane
		gridPane.add(calculateButton, 1, 7);

		gridPane.add(new Label("Total Trip Cost:"), 0, 8);
		gridPane.add(totalCostField, 1, 8);

		// Set UI properties
		gridPane.setAlignment(Pos.CENTER);

		distanceUnitComboBox.getItems().addAll("Miles", "Kilometers");
		distanceUnitComboBox.setValue("Miles");

		gasolineCostUnitComboBox.getItems().addAll("Dollars per Gallon", "Dollars per Liter");
		gasolineCostUnitComboBox.setValue("Dollars per Gallon");

		gasMileageUnitComboBox.getItems().addAll("Miles per Gallon", "Kilometers per Liter");
		gasMileageUnitComboBox.setValue("Dollars per Gallon");

		// Set totalCostField so user can't input a value
		totalCostField.setEditable(false);

		// Set action on button
		calculateButton.setOnAction(e -> {
			// Validate blanks
			if (!validateFields()) {
				totalCostField.setText("Blank Field");
				return;
			}

			// Create the TripCost object
			try {
				tripCost = new TripCost(Double.parseDouble(distanceField.getText()),
						Double.parseDouble(gasMileageField.getText()), Double.parseDouble(gasolineCostField.getText()),
						Integer.parseInt(numDaysField.getText()), Double.parseDouble(hotelCostField.getText()),
						Double.parseDouble(foodCostField.getText()), Double.parseDouble(attractionsCostField.getText()),
						distanceUnitComboBox, gasolineCostUnitComboBox, gasMileageUnitComboBox);

			} catch (NumberFormatException ex) {
				totalCostField.setText("Invalid Input");
				return;
			} catch (IllegalArgumentException ex) {
				totalCostField.setText(ex.getMessage());
				return;
			}

			// Validate negatives
			if (!validateNegative()) {
				totalCostField.setText("No Negative Numbers");
				return;
			}

			// Calculate total cost and set it to the totalCostField
			tripCost.calculateTotalCost();
		});

		// Set the stage title and scene
		primaryStage.setTitle("Trip Cost Estimator");
		Scene scene = new Scene(gridPane, 450, 350);
		primaryStage.setScene(scene);

		// Make the stage non-resizable
		primaryStage.setResizable(false);

		// Show the stage
		primaryStage.show();
	}

	/**
	 * Validate method for empty fields
	 */
	private boolean validateFields() {
		return !distanceField.getText().isEmpty() && !gasMileageField.getText().isEmpty()
				&& !gasolineCostField.getText().isEmpty() && !numDaysField.getText().isEmpty()
				&& !hotelCostField.getText().isEmpty() && !foodCostField.getText().isEmpty()
				&& !attractionsCostField.getText().isEmpty();
	}

	/**
	 * Validate method for negative values
	 */
	private boolean validateNegative() {
		boolean isValid = true;

		if (tripCost.getDistance() < 0) {
			totalCostField.setText("No Negative Numbers");
			isValid = false;
		}
		if (tripCost.getGasMileage() < 0) {
			totalCostField.setText("No Negative Numbers");
			isValid = false;
		}
		if (tripCost.getGasolineCost() < 0) {
			totalCostField.setText("No Negative Numbers");
			isValid = false;
		}
		if (tripCost.getNumDays() < 0) {
			totalCostField.setText("No Negative Numbers");
			isValid = false;
		}
		if (tripCost.getHotelCost() < 0) {
			totalCostField.setText("No Negative Numbers");
			isValid = false;
		}
		if (tripCost.getFoodCost() < 0) {
			totalCostField.setText("No Negative Numbers");
			isValid = false;
		}
		if (tripCost.getAttractionsCost() < 0) {
			totalCostField.setText("No Negative Numbers");
			isValid = false;
		}

		return isValid;
	}

	/**
	 * Nested Immutable class to build TripCost object and calculate the total cost
	 * of the trip.
	 */
	public final class TripCost {
		/**
		 * Initiate Variables
		 */
		private final static double KILOMETERS_PER_MILE = 1.609347;
		private final static double LITERS_PER_GALLON = 3.78541178;
		private double distance;
		private double gasMileage;
		private double gasolineCost;
		private final int numDays;
		private final double hotelCost;
		private final double foodCost;
		private final double attractionsCost;
		private String distanceUnit;
		private String gasolineCostUnit;
		private String gasMileageUnit;
		private String totalCost;

		/**
		 * Initiate object
		 */
		public TripCost(double distance, double gasMileage, double gasolineCost, int numDays, double hotelCost,
				double foodCost, double attractionsCost, ComboBox<String> distanceUnitComboBox,
				ComboBox<String> gasolineCostUnitComboBox, ComboBox<String> gasMileageUnitComboBox) {

			this.distance = distance;
			this.gasMileage = gasMileage;
			this.gasolineCost = gasolineCost;
			this.numDays = numDays;
			this.hotelCost = hotelCost;
			this.foodCost = foodCost;
			this.attractionsCost = attractionsCost;

			// Set these values based on your ComboBox selections
			setDistanceUnitComboBox(distanceUnitComboBox);
			setGasolineCostUnitComboBox(gasolineCostUnitComboBox);
			setGasMileageUnitComboBox(gasMileageUnitComboBox);
		}

		/**
		 * change values if needed
		 */
		public void setDistanceUnitComboBox(ComboBox<String> distanceUnitComboBox) {
			distanceUnit = distanceUnitComboBox.getValue();
			if (distanceUnit.equals("Kilometers")) {
				distance /= KILOMETERS_PER_MILE;
			}
		}

		public void setGasolineCostUnitComboBox(ComboBox<String> gasolineCostUnitComboBox) {
			gasolineCostUnit = gasolineCostUnitComboBox.getValue();
			if (gasolineCostUnit.equals("Dollars per Liter")) {
				gasolineCost /= LITERS_PER_GALLON;
			}
		}

		public void setGasMileageUnitComboBox(ComboBox<String> gasMileageUnitComboBox) {
			gasMileageUnit = gasMileageUnitComboBox.getValue();
			if (gasMileageUnit.equals("Kilometers per Liter")) {
				gasMileage /= KILOMETERS_PER_MILE;
			}
		}

		/**
		 * @return the distance
		 */
		public double getDistance() {
			return distance;
		}

		/**
		 * @return the gasMileage
		 */
		public double getGasMileage() {
			return gasMileage;
		}

		/**
		 * @return the gasolineCost
		 */
		public double getGasolineCost() {
			return gasolineCost;
		}

		/**
		 * @return the numDays
		 */
		public int getNumDays() {
			return numDays;
		}

		/**
		 * @return the hotelCost
		 */
		public double getHotelCost() {
			return hotelCost;
		}

		/**
		 * @return the foodCost
		 */
		public double getFoodCost() {
			return foodCost;
		}

		/**
		 * @return the attractionsCost
		 */
		public double getAttractionsCost() {
			return attractionsCost;
		}

		/**
		 * @return the totalCost
		 */
		public String getTotalCost() {
			return totalCost;
		}

		/**
		 * Method will calculate the total cost by getting values when the calculate
		 * button is pushed
		 */
		public void calculateTotalCost() {

			// Update units before calculations
			setDistanceUnitComboBox(distanceUnitComboBox);
			setGasolineCostUnitComboBox(gasolineCostUnitComboBox);
			setGasMileageUnitComboBox(gasMileageUnitComboBox);

			// Calculate the total cost
			double totalGasCost = (distance / gasMileage) * gasolineCost;
			double totalDailyCost = hotelCost + foodCost;
			double totalTripCost = totalGasCost + (totalDailyCost * numDays) + attractionsCost;

			// Set the total cost in the output field
			totalCostField.setText(String.format("$%.2f", totalTripCost));

			// Set the total cost variable
			totalCost = totalCostField.getText();
		}
	}

	/**
	 * Main method to launch from Eclipse.
	 */
	public static void main(String[] args) {
		launch(args);
	}
}
