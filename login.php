<?php
 
    session_start();
    
    include "config.php";
 
    $user_login = $_GET['login'];
    $user_pass  = $_GET['pass'];
    
    $sql = "SELECT * FROM user WHERE user_name = '".$user_login."' AND user_pass = '".$user_pass."';";
    $result = mysql_query($sql)
        or die("Podałeś błędny login lub hasło");
        
    $rows = mysql_num_rows($result);
    
    if ($rows == 1) {
        
        $r = mysql_fetch_assoc($result);
        session_register("user_id");
        session_register("user_name");
        session_register("user_email");
        session_register("user_rights");
        session_register("user_date");
        
        $_SESSION['user_id']     = $r['user_id'];
        $_SESSION['user_name']   = $r['user_name'];
        $_SESSION['user_email']  = $r['user_email'];
        $_SESSION['user_rights'] = $r['user_rights'];
        $_SESSION['user_date']   = $r['user_date'];
        
        header("Location: index.php");
    }
    else {
        echo "Podałeś błędny login lub hasło... <br> <a href=\"index.php\">Powrót</a>";
    }
 
?>