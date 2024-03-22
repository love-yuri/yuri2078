<?php
$name = 'hello, world1';
$Name = 'hello, world2';
$NAME = 'hello, world3';

echo "\$name = $name" . "<br>";
EcHO "\$NAME = $NAME" . "<br>";
ECHO "\$NaME = $NAME" . "<br>";

$what = "Fred";
echo "\$what的值=$what\n<br>";
if (is_string($what)) echo "\$wha是字符串数据<br>";

$what = 1;
echo "\$what的值=$what\n<br>";
if (is_int($what)) echo "\$wha是整型数据<br>";

$what = array("12", 3, "34");
foreach ($what as $e)
    echo "e-> $e<br>";

if (is_array($what)) echo "\$wha是数组数据<br>\n";

$name = 'Tom';
echo "Hi, $name<br>";
echo 'Hi, $name<br>';

$person = array(
    "Edison" => "Light bulb",
    "Wankel" => "Rotary Engine",
    "Crapper" => "Toilet"
);

foreach ($person as $name => $invention) {
    echo "$name invented the $invention.\n";
}

<?? >
echo date();