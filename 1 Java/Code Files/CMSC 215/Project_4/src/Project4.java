import java.text.ParseException;
import java.text.SimpleDateFormat;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

/**
 * @author Brian Walters
 * CMSC 215
 * Assignment 4
 * Project 4
 * Class - Project4
 * December 12, 2023
 */

/**
 * Represents the main application for the Time Interval Checker. Allows users
 * to compare intervals and check if a specific time is within them.
 */

public class Project4 extends Application {

	/**
	 * Set Labels
	 */
	private final Label startTime = new Label("Start Time");
	private final Label endTime = new Label("End Time");
	private final Label timeInterval1 = new Label("Time Interval 1");
	private final Label timeInterval2 = new Label("Time Interval 2");
	private final Label timeToCheck = new Label("Time to Check");

	/**
	 * Set textFields
	 */
	private final TextField timeInterval1StartTime = new TextField();
	private final TextField timeInterval1EndTime = new TextField();
	private final TextField timeInterval2StartTime = new TextField();
	private final TextField timeInterval2EndTime = new TextField();
	private final TextField timeToCheckInput = new TextField();
	private final TextField results = new TextField();

	/**
	 * Set Buttons
	 */
	private final Button compareIntervals = new Button("Compare Intervals");
	private final Button checkTime = new Button("Check Time");

	/**
	 * Start Stage
	 */
	@Override
	public void start(Stage primaryStage) throws Exception {

		/**
		 * Create GridPane for UI
		 */
		GridPane gridPane = new GridPane();
		gridPane.setHgap(5);
		gridPane.setVgap(5);
		gridPane.setPadding(new Insets(10, 10, 10, 10));

		/**
		 * Add labels, text fields, and buttons to HBoxes
		 */
		// Set preferred width for buttons
		compareIntervals.setPrefWidth(Double.MAX_VALUE);
		checkTime.setPrefWidth(Double.MAX_VALUE);

		// Center the label horizontally in the middle of the column
		GridPane.setHalignment(startTime, javafx.geometry.HPos.CENTER);
		GridPane.setHalignment(endTime, javafx.geometry.HPos.CENTER);

		// Apply CSS styling to center the text
		timeInterval1StartTime.setStyle("-fx-alignment: CENTER;");
		timeInterval1EndTime.setStyle("-fx-alignment: CENTER;");
		timeInterval2StartTime.setStyle("-fx-alignment: CENTER;");
		timeInterval2EndTime.setStyle("-fx-alignment: CENTER;");
		timeToCheckInput.setStyle("-fx-alignment: CENTER;");

		gridPane.add(startTime, 1, 0);
		gridPane.add(endTime, 2, 0);

		gridPane.add(timeInterval1, 0, 1);
		gridPane.add(timeInterval1StartTime, 1, 1);
		gridPane.add(timeInterval1EndTime, 2, 1);

		gridPane.add(timeInterval2, 0, 2);
		gridPane.add(timeInterval2StartTime, 1, 2);
		gridPane.add(timeInterval2EndTime, 2, 2);

		gridPane.add(compareIntervals, 0, 3, 3, 1);

		gridPane.add(timeToCheck, 0, 4);
		gridPane.add(timeToCheckInput, 1, 4, 2, 1);

		gridPane.add(checkTime, 0, 5, 3, 1);

		gridPane.add(results, 0, 6, 3, 1);

		/**
		 * Set UI properties
		 */
		gridPane.setAlignment(Pos.CENTER);

		/**
		 * Set OutputFields so user can't input a value
		 */
		results.setEditable(false);

		/**
		 * Set action on buttons
		 */
		compareIntervals.setOnAction(e -> {
			try {
				// Validate time fields before proceeding
				validateTimeFields();

				// Call the compareIntervals method
				compareIntervals();
			} catch (InvalidTime ex) {
				results.setText("Invalid time input: " + ex.getMessage());
			}
		});

		checkTime.setOnAction(e -> {
			try {
				// Validate time fields before proceeding
				validateTimeFields();

				// Call the checkTime method
				checkTime();
			} catch (InvalidTime ex) {
				results.setText("Invalid time input: " + ex.getMessage());
			}
		});

		/**
		 * Set Stage
		 */
		primaryStage.setTitle("Time Interval Checker");
		Scene scene = new Scene(gridPane, 425, 215);
		primaryStage.setScene(scene);
		primaryStage.setResizable(false);
		primaryStage.show();
	}

	/**
	 * Validates the time fields by checking for null or empty values.
	 */
	private void validateTimeFields() throws InvalidTime {
		// Get user input from text fields
		String interval1StartTimeString = timeInterval1StartTime.getText();
		String interval1EndTimeString = timeInterval1EndTime.getText();
		String interval2StartTimeString = timeInterval2StartTime.getText();
		String interval2EndTimeString = timeInterval2EndTime.getText();

		// Check for null values and handle accordingly
		if (interval1StartTimeString.isEmpty() || interval1EndTimeString.isEmpty() || interval2StartTimeString.isEmpty()
				|| interval2EndTimeString.isEmpty()) {
			throw new InvalidTime("Please fill in all time fields.");
		}
	}

	/**
	 * Handles the event when the "Compare Intervals" button is clicked.
	 */
	private void compareIntervals() {
		try {
			// Get user input from text fields
			Time interval1StartTime = new Time(timeInterval1StartTime.getText());
			Time interval1EndTime = new Time(timeInterval1EndTime.getText());
			Time interval2StartTime = new Time(timeInterval2StartTime.getText());
			Time interval2EndTime = new Time(timeInterval2EndTime.getText());

			// Initialize intervals
			Interval interval1 = Interval.createInterval(interval1StartTime.toDate(), interval1EndTime.toDate());
			Interval interval2 = Interval.createInterval(interval2StartTime.toDate(), interval2EndTime.toDate());

			// Compare intervals and display result in resultsTextField
			if (interval1.subinterval(interval2)) {
				results.setText("Interval 1 is a sub-interval of interval 2");
			} else if (interval2.subinterval(interval1)) {
				results.setText("Interval 2 is a sub-interval of interval 1");
			} else if (interval1.overlaps(interval2)) {
				results.setText("The intervals overlap");
			} else {
				results.setText("The intervals are disjoint");
			}
		} catch (InvalidTime | ParseException e) {
			results.setText("Invalid input: " + e.getMessage());
		}
	}

	/**
	 * Handles the event when the "Check Time" button is clicked.
	 */
	private void checkTime() {
		try {
			// Get user input from text field
			Time timeToCheck = new Time(timeToCheckInput.getText());
			SimpleDateFormat timeFormat = new SimpleDateFormat("hh:mm a");
			Time interval1StartTime = new Time(timeInterval1StartTime.getText());
			Time interval1EndTime = new Time(timeInterval1EndTime.getText());
			Time interval2StartTime = new Time(timeInterval2StartTime.getText());
			Time interval2EndTime = new Time(timeInterval2EndTime.getText());

			// Initialize intervals
			Interval interval1 = Interval.createInterval(interval1StartTime.toDate(), interval1EndTime.toDate());
			Interval interval2 = Interval.createInterval(interval2StartTime.toDate(), interval2EndTime.toDate());

			// Example: Check time and display result in resultsTextField
			if (interval1.contains(timeToCheck.toDate()) && interval2.contains(timeToCheck.toDate())) {
				results.setText("Both intervals contain the time " + timeFormat.format(timeToCheck.toDate()));
			} else if (interval1.contains(timeToCheck.toDate())) {
				results.setText("Only interval 1 contains the time " + timeFormat.format(timeToCheck.toDate()));
			} else if (interval2.contains(timeToCheck.toDate())) {
				results.setText("Only interval 2 contains the time " + timeFormat.format(timeToCheck.toDate()));
			} else {
				results.setText("Neither interval contains the time " + timeFormat.format(timeToCheck.toDate()));
			}
		} catch (InvalidTime | ParseException e) {
			results.setText("Invalid input: " + e.getMessage());
		}
	}

	/**
	 * Main method to launch from Eclipse.
	 */
	public static void main(String[] args) {
		launch(args);
	}
}
