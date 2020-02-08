<?php
 if ($_POST['message'] != '')
 {
  $message = $_POST['message'];
  $name = $_POST['name'];
  $message = str_replace ("\n","<br>",$message);
  $message = strip_tags ($message, '<br>');

  $newRow = '<div class="viewGuestbook">' . ($message) .
  	    '<br>' . date('d.m.Y H:i') . ' - ' . strip_tags ($name) .
  	    '</div>';

  $oldRows = join ('', file ('guestbook.txt') );
  $fileName = fopen ('guestbook.txt', 'w');
  fputs ($fileName, $newRow . chr(13) . chr(10) . $oldRows);
  fclose ($fileName);
 }

 include ("readbook.php");
?>
