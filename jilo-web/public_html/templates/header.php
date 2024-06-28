<?php

session_start();

$scriptname = basename($_SERVER['SCRIPT_NAME']);

if ( !isset($_SESSION['user_id']) && ($scriptname !== 'login.php' && $scriptname !== 'register.php') ) {
    header('Location: login.php');
    exit();
}

if ( isset($_SESSION['username']) ) {
    echo "Welcome, " . htmlspecialchars($_SESSION['username']) . "!";
}

if (isset($error)) {
    echo "<p style='color: red;'>Error: $error</p>";
}

?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" type="text/css" href="templates/all.css">
    <title>Jilo Web</title>
</head>

<body>

<ul class="menu">
<?php if ( !isset($_SESSION['user_id']) ) { ?>
    <li><a href="login.php">login</a></li>
    <li><a href="register.php">register</a></li>
<?php } else { ?>
    <li><a href="logout.php">logout</a></li>
<?php } ?>
</ul>
