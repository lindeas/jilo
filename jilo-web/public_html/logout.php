<?php

session_start();
session_unset();
session_destroy();
unset($error);

echo "You logged out.";

include 'templates/header.php';
include 'templates/body.php';
include 'templates/footer.php';

?>