<div class="guestbookTop">
<a href="postform.php">Write</a> to a guestbook<br><br>
</div>

<?php

 $fileName = file ("guestbook.txt");
 $rows = count ($fileName);
  
 if ($rows > 10)
 {
 	if (!isset ($row) )
 	{
 		$row = 0;
 	}
 
 	print ("<table class=\"guestbookLinks\"><tr><td width=\"50%\">");
  
 	if ($row > 0)
 	{
		echo "<div class=\"nextPage\"><< <a href=\"readbook.php?row=" . ($row - 10) . "\">Next 10</a></div>";
	}
	
	print ("</td><td width=\"50%\">");

 	if ( ($rows - $row) > 10)
 	{
		echo "<div class=\"previousPage\"><a href=\"readbook.php?row=" . ($row + 10) . "\">Previous 10</a> >></div>";
	}
		
	print ("</td></tr></table>");

   	for ($i = $row; $i < ($row + 10); $i++)
	{
		echo $fileName [$i];
	}
 }
 else
 {
  	for ($i=0; $i < $rows; $i++)
  	{
  		echo $fileName [$i];
  	}
 }
  
?>

<div class="guestbookUp">
<br><br><br><br>	
<a href="postform.php">Write</a> to a guestbook
</div>