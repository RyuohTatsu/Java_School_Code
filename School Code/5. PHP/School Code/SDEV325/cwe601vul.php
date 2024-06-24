<!DOCTYPE html>
<html>
<head>
    <title>Unsafe Redirect</title>
</head>
<body>
    <h1>Unsafe Redirect</h1>

    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="get">
        <label for="url">Enter URL to Redirect:</label><br>
        <input type="text" id="url" name="redirect"><br>
        <input type="submit" value="Go">
    </form>

    <?php
    // Check if the form is submitted
    if ($_SERVER["REQUEST_METHOD"] == "GET") {
        // Get redirect URL from query parameter
        $redirect_url = $_GET['redirect'];

        // Redirect user to the specified URL (without validation)
        header("Location: $redirect_url");
        exit; // Prevent further execution of the script
    }
    ?>
</body>
</html>