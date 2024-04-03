<?php
// $row = 1;
// for ($i=1; $i <= 19 ; $i = $i + 3) { 
//   for($j = 0; $j < $row; $j++) {
//     echo "#";
//   }
//   $row = $row + 1;
//   echo " $i\n";
// }

function getVal($x): float
{
  if($x > 10) {
    return $x ** 2 + 0.5;
  } else if($x > 0) {
    return $x ** 3 - 1;
  } else {
    return  $x ** 2 + 4 * $x;
  }
}

