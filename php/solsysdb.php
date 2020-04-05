<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Солнечная система: таблица PHP SQlite</title>
  <link rel="stylesheet" href="../solarsystem/style.css">
  <link rel="icon" type="image/png" href="../solarsystem/favicon.png">
  <script src="../solarsystem/script.js"></script>
</head>
<body>
  <h1>Таблица параметров тел Солнечной системы</h1>
  <table>
  <tr>
    <th>Номер</th>
    <th>Имя</th>
    <th>По-русски</th>
    <th>Это луна?</th>
    <th>Радиус, км</th>
    <th>Масса, кг</th>
    <th>ΔV, км/с</th>
    <th>Дата открытия</th>
    <th>Картинка</th>
  </tr>
  <tbody>
<?php
$file_db = new PDO('sqlite:../py/solsysobjs.db');
$db = null;
$rezult = $file_db->query('SELECT * FROM sobject');

foreach ($rezult as $result) {
  echo "<td>";
  if (!empty($result['anumber']))
    print $result['anumber'];
  echo "</td><td>";
  print $result['name'];
  echo "</td><td>";
  print $result['runame'];
  echo "</td><td>";
  print $result['is_moon'];
  echo "</td><td>";
  print $result['size'];
  echo "</td><td>";
  print $result['mass'];
  echo "</td><td>";
  print $result['deltaV'];
  echo "</td><td>";
  if ($result['discoverdate']) {
    $date = date_create($result['discoverdate']);
    print date_format($date, 'd.m.Y');
  }
  echo "</td><td><img src='../solarsystem/images/";
  echo $result['filename'];
  echo "'></td></tr>\n";
}
?>
</tbody>
</table>
</body>
</html>