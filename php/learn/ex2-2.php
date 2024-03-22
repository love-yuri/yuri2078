<!DOCTYPE html>
<html>
<head>
    <title>Calculator</title>
</head>
<body>
<h1>实现一个计算器</h1>
<form method="post" action="ex2.php">
    第一个数: <input type="text" name="num1"><br><br>
    第二个数: <input type="text" name="num2"><br><br>
    <label>
        Select operation:
        <select name="operation">
            <option value="add">Addition</option>
            <option value="subtract">Subtraction</option>
            <option value="multiply">Multiplication</option>
            <option value="divide">Division</option>
        </select>
    </label><br><br>
    <input type="submit" value="Calculate">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $num1 = $_POST["num1"];
    $num2 = $_POST["num2"];
    $operation = $_POST["operation"];

    switch ($operation) {
        case "add":
            $result = $num1 + $num2;
            echo "Result: $num1 + $num2 = $result";
            break;
        case "subtract":
            $result = $num1 - $num2;
            echo "Result: $num1 - $num2 = $result";
            break;
        case "multiply":
            $result = $num1 * $num2;
            echo "Result: $num1 * $num2 = $result";
            break;
        case "divide":
            if ($num2 != 0) {
                $result = $num1 / $num2;
                echo "Result: $num1 / $num2 = $result";
            } else {
                echo "Cannot divide by zero!";
            }
            break;
        default:
                echo "Invalid operation selected.";
    }
}
?>
</body>
</html>
