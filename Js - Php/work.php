<?php
	//$_REQUEST[] array is used to place instead to $_POST[] array or $_GET[] array.
	//in simple it holds any type of method's data

	$first = $_REQUEST['first'];
	$last = $_REQUEST['last'];
	
	echo "The given details are :- \n Firsname : $first \n Lastname : $last";
?>