/*
* @Author: love-yuri yuri2078170658@gmail.com
* @Date: 2024-04-01 14:07:59
* @LastEditTime: 2024-04-15 15:50:36
* @Description: php 教程
*/
<?php
$arr = array('1', 40, 33, 5, 8);
sort($arr);
foreach ($arr as $key => $value) {
  echo "$key => $value ";
}
echo "\n";
?>