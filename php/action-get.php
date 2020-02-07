<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>PHP response</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
<h2>Пример обработки форм, метод GET</h2>
<p>Главный тег: <?php echo htmlspecialchars($_GET['name']); ?>.<br>
<p>Лишний тег: <?php echo $_GET['tag1']; ?><br>
<p>Строчный тег: <?php echo $_GET['tag2']; ?><br>
Картинка: <img src="<?php echo htmlspecialchars($_GET['imgurl']); ?>" alt=""><br>
<?php if ((int)$_GET['year'] == 1990): ?>
Год создания WWW &ndash; <?php echo (int)$_GET['year']; ?>.
<?php else: ?>
Нет, год создания WWW &ndash; не <?php echo (int)$_GET['year']; ?>.
<?php endif; ?>
<br>
<p>Сообщение: <?php echo htmlspecialchars($_GET['msg']); ?></p>
Согласился с условиями? <?php if ( isset($_GET['checker']) )
{
  echo "Да";
} else {
  echo "Нет";
} ?>


<?php
$empty = $get = array();
foreach ($_GET as $varname => $varvalue) {
    if (empty($varvalue)) {
        $empty[$varname] = $varvalue;
    } else {
        $get[$varname] = $varvalue;
    }
}

print "<pre>";
if (empty($empty)) {
    print "В GET не было пустых значений, вот что там было:\n";
    var_dump($get);
} else {
    print "Пришло " . count($empty) . " пустых значений\n";
    print "Всего отправлено:\n"; var_dump($get);
    print "Пустых:\n"; var_dump($empty);
    exit;
}
?>

</body>
</html>