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
<h2>Пример обработки форм, метод POST</h2>
<p>Главный тег: <?php echo htmlspecialchars($_POST['name']); ?>.<br>
<p>Лишний тег: <?php echo $_POST['tag1']; ?><br>
<p>Строчный тег: <?php echo $_POST['tag2']; ?><br>
Картинка: <img src="<?php echo htmlspecialchars($_POST['imgurl']); ?>" alt=""><br>
<?php if ((int)$_POST['year'] == 1990): ?>
Год создания WWW &ndash; <?php echo (int)$_POST['year']; ?>.
<?php else: ?>
Нет, год создания WWW &ndash; не <?php echo (int)$_POST['year']; ?>.
<?php endif; ?>
<br>
<p>Сообщение: <?php echo htmlspecialchars($_POST['msg']); ?></p>
Согласился с условиями? <?php if ( isset($_POST['checker']) )
{
  echo "Да";
} else {
  echo "Нет";
} ?>
</body>
</html>