<?php

class User {
    private $db;

    public function __construct($database) {
        $this->db = $database->getConnection();
    }

    public function register($username, $password) {
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
        $query = $this->db->prepare("INSERT INTO users (username, password) VALUES (:username, :password)");
        $query->bindParam(':username', $username);
        $query->bindParam(':password', $hashedPassword);

        return $query->execute();
    }

    public function login($username, $password) {
        $query = $this->db->prepare("SELECT * FROM  users WHERE username = :username");
        $query->bindParam(':username', $username);
        $query->execute();

        $user = $query->fetch(PDO::FETCH_ASSOC);
        if ( $user && password_verify($password, $user['password'])) {
            session_start();
            $_SESSION['user_id'] = $user['id'];
            $_SESSION['username'] = $user['username'];
            return true;
        } else {
            return false;
        }
    }

}

?>
