import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.VBox;
import javafx.scene.text.Text;
import javafx.stage.Stage;

public class HelloWorld extends Application {

    @Override
    public void start(Stage primaryStage) throws Exception {
        // Create a Text object for the label
        Text helloText = new Text("Hello World!");

        // Create a layout container (VBox in this case)
        VBox root = new VBox();
        root.getChildren().add(helloText); // Add the text to the layout

        // Create a scene with the layout and set its size
        Scene scene = new Scene(root, 300, 250); // Set width and height

        primaryStage.setTitle("Hello World!"); // Set the title of the window
        primaryStage.setScene(scene); // Set the scene on the stage
        primaryStage.show(); // Display the window
    }

    public static void main(String[] args) {
        launch(args);
    }
}
