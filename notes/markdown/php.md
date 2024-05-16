# php开发实践

> 使用php, vue, mysql 开发

## 安装

### 安装php

1. 下载php的可执行文件: [下载地址](https://windows.php.net/downloads/releases/php-8.3.7-nts-Win32-vs16-x64.zip)

2. 解压到c盘根据路，并将文件夹命名成php(别问，问就是这样方便)

3. 将目录添加到系统path

4. 打开终端输入`php --version` 测试是否安装成功

   ```shell
   PHP 8.3.7 (cli) (built: May  8 2024 08:56:34) (NTS Visual C++ 2019 x64)
   Copyright (c) The PHP Group
   Zend Engine v4.3.7, Copyright (c) Zend Technologies
   ```

5. 打开vscode安装php插件，搜索php安装第一个插件就行

### 安装node

百度直接下载

### 安装mysql

百度直接下载

## 连接mysql

1. 添加mysqli插件

   1. 查看php目录有没有php.ini配置文件。如果没有则将`"C:\php\php.ini-development"`拷贝成`php.ini`
   2. 修改`php.ini`， 取消`extension=mysqli`前的注释

2. 使用` php -S localhost:8000` 启动看看有没有报错。这个命令会在当前目录下启动服务器。浏览器访问这个网址可以看到效果。默认访问`index.php`文件

3. 配置连接信息

   ```php
   // MySQL 数据库连接信息
   $servername = "localhost"; // MySQL 服务器地址
   $username = "root"; // MySQL 用户名
   $password = "yuri"; // MySQL 密码
   $database = "php_news"; // 要连接的数据库名
   
   // 创建连接
   $conn = new mysqli($servername, $username, $password, $database);
   ```

4. 检查连接

   ```php
   // 检查连接是否成功
   if ($conn->connect_error) {
       die("数据库连接失败: " . $conn->connect_error);
   }
   
   echo "数据库连接成功!!!\n";
   ```

5. 然后就可以使用数据库了。

6. 常用函数

   1. 执行sql: `$result = $conn->query($sql);`
   2. 获取检查结果:  ` while($row = $result->fetch_assoc())` 
   3. 获取具体的值: `$ros["age"]
   
7. 
