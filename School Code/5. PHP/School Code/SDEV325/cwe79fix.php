<!DOCTYPE html>
<html>
<head>
    <title>Guest Book</title>
</head>
<body>
    <h1>Welcome to our Guest Book!</h1>
    <form action="submit_comment.php" method="post">
        <label for="comment">Leave a comment:</label><br>
        <textarea id="comment" name="comment"></textarea><br>
        <input type="submit" value="Submit">
    </form>
    <?php
    // Display comments with HTML escaping
    $comments = htmlspecialchars($_POST['comment']);
    echo "<p>Previous Comments:</p>";
    echo $comments;
    ?>
</body>
</html>
