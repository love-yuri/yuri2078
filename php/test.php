<?php
require_once ("index.php");
$arr = array('1', 40, 33, 5, 8);
sort($arr);
foreach ($arr as $key => $value) {
  echo "$key => $value ";
}
echo "\n";
