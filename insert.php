<html>
<body>
 
<?php
$con = mysql_connect("localhost","31366436_moja","J3bWuPP7");
if (!$con)
  {
  die('Nie mozna polaczyc: ' . mysql_error());
  }
  
mysql_select_db("31366436_moja", $con);
  
$sql="INSERT INTO dane1 (one, two)
VALUES
('$_POST[one]','$_POST[two]')";
  
if (!mysql_query($sql,$con))
  {
  die('Blad: ' . mysql_error());
  }
echo "Dodano wpis!";
  
mysql_close($con)
?>
 
</body>
</html>