<?php

$hi = 'Hello World'; // $ 定义变量
$hello = "Hello World"; // 字符串的两种类型

echo $hi . "\n"; // 打印数据 . 拼接字符串
var_dump($hi); // 打印数据类型 以及数据s

$arrays = array(1, 2, 3, 4); // 数组定义


/* 类 */
class Person {
    public $name;
    public function __construct($name = 'tom')
    {
        $this->name = $name;
        echo $this->name . "\n";
    }
}

// new 对象
$person = new Person('yuri');

var_dump($nullVal = null);

const NAME = '你好，掘金'; // 常量
echo NAME . "\n"; // 运行结果：你好，掘金

function getVal($val)
{
    echo "获得的值是 $val\n";
}

getVal(2333);

//echo $_GET['name']; // 接收get方式传参的name值
//echo $_POST['name']; // 接收post方式传参的name值

echo <<<EOF
yuri is yes \n
EOF;

// phpinfo(); 打印php信息