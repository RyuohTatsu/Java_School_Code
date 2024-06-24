<!DOCTYPE html>
<html>
<head>
    <title>Safe Redirect</title>
</head>
<body>
    <h1>Safe Redirect</h1>

    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="get">
        <label for="url">Enter URL to Redirect:</label><br>
        <input type="text" id="url" name="redirect"><br>
        <input type="submit" value="Go">
    </form>

    <?php
    // Define a list of trusted domains
    $whitelisted_domains = array("example.com", "trustedsite.com");

    // Check if the form is submitted
    if ($_SERVER["REQUEST_METHOD"] == "GET") {
        // Get redirect URL from query parameter
        $redirect_url = $_GET['redirect'];

        // Validate redirect URL
        if (!empty($redirect_url) && in_array(parse_url($redirect_url, PHP_URL_HOST), $whitelisted_domains)) {
            // Redirect user to the specified URL
            header("Location: $redirect_url");
            exit; // Prevent further execution of the script
        } else {
            // Display an error message
            echo "<p style='color: red;'>Error: Invalid URL</p>";
        }
    }
    ?>
</body>
</html>