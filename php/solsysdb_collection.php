<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Солнечная система PHP SQlite</title>
  <link rel="stylesheet" href="../collections.css">
  <link rel="stylesheet" href="../solarsystem/style.css">
  <script src="../collections.js"></script>
  <script src="../solarsystem/script.js"></script>

  <link rel="icon" type="image/png" href="../solarsystem/favicon.png">
</head>
<body>
<body onload="findDate()">
<nav class="menu">
<ul>
  <li>Коллекции:</li>
  <li>Солнечная система</li>
  <li><a href="../stars/">Звезды</a></li>
  <li><a href="../galaxies/">Галактики</a></li>
  <li><a href="../exoplanets/">Экзопланеты</a></li>
</ul>
</nav>

<div id="messageBox">
<div id="contents"></div>
</div>

<h1>&laquo;Семейный портрет&raquo; Солнечной системы</h1>

<div class="cont">
<b>Пульт управления информацией:</b><br>
<input type="checkbox" name=".name" value="block" checked onclick="showHideThis(this)">Имя,
<input type="checkbox" name=".size" value="block" checked onclick="showHideThis(this)">Радиус,
<input type="checkbox" name=".date" value="block" checked onclick="showHideThis(this)">Дата открытия,
<input type="checkbox" name=".mass" value="block" onclick="showHideThis(this)">Масса,
<input type="checkbox" name=".delta-v" value="block" onchange="showHideThis(this)">Δv<br>
<input type="checkbox" name=".highcontrast,.lightcurve" value="inline-block" checked onchange="showHideThis(this)">"восстановленное" изображение или модель<br>
<input type="checkbox" name=".dot,.lowcontrast" value="inline-block" checked onchange="showHideThis(this)">Фото низкого разрешения или точечное<br>
<input type="checkbox" name=".radar" value="inline-block" checked onchange="showHideThis(this)">Радарное изображение<br>
<input type="checkbox" name=".he" value="inline-block" checked onchange="showHideThis(this)">"круглые" тела (в гидростатическом равновесии)<br>
<input type="checkbox" name=".animation" value="block" checked onclick="showHideThis(this)">С анимированными картинками.<br>
<input type="text" id="year" size="4" maxlength="4" value="1990">
<button type="button" onclick="showHideByDate('none')">Скрыть объекты, открытые после указанного года</button>
<button type="button" onclick="showHideByDate('inline-block')">Показать объекты, открытые после указанного года</button><br>
Сортировать: <button type="button" onclick="toSort('date')">по году открытия</button>
<button type="button" onclick="toSort('size')">по возрастанию размера</button>
<button type="button" onclick="toSort('mass')">по возрастанию массы</button>
<button type="button" onclick="toSort('delta-v')">по возрастанию Δv</button><br>
Фокус на картинке &ndash; полная информация.
</div>

<div id="tab">

<?php
$file_db = new PDO('sqlite:../py/solsysobjs.db');
$db = null;
$rezult = $file_db->query('SELECT * FROM sobject');

foreach ($rezult as $result) {
	
  echo '<div class="obj star he">';
  echo '<div class="img" onmouseover="show(this)" onmouseout="hide()"><img alt="';
  if (!empty($result['anumber']))
    print $result['anumber'];
	print $result['name'];
  echo '" src="../solarsystem/images/';
  echo $result['filename'];
  echo '"></div>';
  echo '<div class="name"><a href="https://en.wikipedia.org/wiki/';
  print $result['name'];
  echo '">';
  print $result['runame'];
  echo '</a></div>';
  echo '<div class="size">';
  print $result['size'];
  echo '</div>';
  echo '<div class="mass">';
  print $result['mass'];
  echo '</div>';
  echo '<div class="date">';
  if ($result['discoverdate']) {
    $date = date_create($result['discoverdate']);
    print date_format($date, 'd.m.Y');
  }
  echo '</div>';
  echo '<div class="delta-v">';
  print $result['deltaV'];
  echo '</div>';
  echo '<div class="desc"></div>';
echo '</div>';
//print $result['is_moon'];
}
?>

</body>
</html>