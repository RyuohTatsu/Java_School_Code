package Exercise09_13;

/**
 *
 * @author brian
 */
// Implement Location class
class Location {
    // Data fields
    int row;         	// Row index of maximal value
    int column;		// Column index of maximal value
    double maxValue;	// Maximal value

    /** Constructs a default Location object */
    Location(double[][] a) {
        maxValue = a[0][0];
        row = 0;
        column = 0;
        // for loop to get instance of Location
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a[i].length; j++) {
                if (a[i][j] > maxValue) {
                    maxValue = a[i][j];
                    row = i;
                    column = j;
                }
            }
        }
    }
}
