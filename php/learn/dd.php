<?php
/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2024-05-10 21:55:37
 * @LastEditTime: 2024-05-13 18:53:34
 * @Description: php请求测试
 */

header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: GET, POST");
header("Access-Control-Allow-Headers: Content-Type");
header("Content-Type: application/json");
require_once ("../index.php");
$age = $_GET["age"];
echo "年龄是：" . $age;