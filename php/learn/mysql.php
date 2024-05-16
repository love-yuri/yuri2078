<?php
/*
 * @Author: love-yuri yuri2078170658@gmail.com
 * @Date: 2024-05-13 18:58:01
 * @LastEditTime: 2024-05-13 18:58:06
 * @Description: 连接MySQL
 */
// MySQL 数据库连接信息
$servername = "localhost"; // MySQL 服务器地址
$username = "root"; // MySQL 用户名
$password = "yuri"; // MySQL 密码
$database = "database"; // 要连接的数据库名

// 创建连接
$conn = new mysqli($servername, $username, $password, $database);

// 检查连接是否成功
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

echo "Connected successfully";

// 执行 SQL 查询等操作...

// 关闭连接
$conn->close();
