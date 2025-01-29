<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $message = htmlspecialchars($_POST['message']);

    // Here you can add code to send the email or save the data to a database

    echo "<h1>Thank you for contacting us, $name!</h1>";
    echo "<p>Your message has been received.</p>";
} else {
    echo "<h1>Contact Us</h1>";
    echo "<p>Please fill out the form to get in touch.</p>";
}
?>

<form action="contact.php" method="post">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>
    
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>
    
    <label for="message">Message:</label>
    <textarea id="message" name="message" required></textarea>
    
    <button type="submit">Send</button>
</form>