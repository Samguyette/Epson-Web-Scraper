<style>
.btn {
  background: #3498db;
  background-image: -webkit-linear-gradient(top, #3498db, #2980b9);
  background-image: -moz-linear-gradient(top, #3498db, #2980b9);
  background-image: -ms-linear-gradient(top, #3498db, #2980b9);
  background-image: -o-linear-gradient(top, #3498db, #2980b9);
  background-image: linear-gradient(to bottom, #3498db, #2980b9);
  -webkit-border-radius: 28;
  -moz-border-radius: 28;
  border-radius: 28px;
  font-family: Arial;
  color: #ffffff;
  font-size: 20px;
  padding: 10px 20px 10px 20px;
  #ext-decoration: none;
}

.btn2 {
  background: #3498db;
  background-image: -webkit-linear-gradient(top, #6C8EAD, #2980b9);
  background-image: -moz-linear-gradient(top, #6C8EAD, #2980b9);
  background-image: -ms-linear-gradient(top, #6C8EAD, #2980b9);
  background-image: -o-linear-gradient(top, #6C8EAD, #2980b9);
  background-image: linear-gradient(to bottom, #6C8EAD, #2980b9);
  -webkit-border-radius: 28;
  -moz-border-radius: 28;
  border-radius: 20px;
  font-family: Arial;
  color: #ffffff;
  font-size: 14px;
  #ext-decoration: none;
}

.btn:hover {
  background: #3cb0fd;
  background-image: -webkit-linear-gradient(top, #3cb0fd, #3cb0bd);
  background-image: -moz-linear-gradient(top, #3cb0fd, #3cb0bd);
  background-image: -ms-linear-gradient(top, #3cb0fd, #3cb0bd);
  background-image: -o-linear-gradient(top, #3cb0fd, #3cb0bd);
  background-image: linear-gradient(to bottom, #3cb0fd, #3cb0bd);
  text-decoration: none;
}

.btn2:hover {
  background: #3cb0fd;
  background-image: -webkit-linear-gradient(top, #3cb0fd, #3cb0bd);
  background-image: -moz-linear-gradient(top, #3cb0fd, #3cb0bd);
  background-image: -ms-linear-gradient(top, #3cb0fd, #3cb0bd);
  background-image: -o-linear-gradient(top, #3cb0fd, #3cb0bd);
  background-image: linear-gradient(to bottom, #3cb0fd, #3cb0bd);
  text-decoration: none;
}
</style>


<form method="post">
    <input class="btn" type="submit" name="P" id="P" value="Pull P-Series Data" style="height:125px; width:250px; margin-left:100px;" />
    <input class="btn" type="submit" name="T" id="T" value="Pull T-Series Data" style="height:125px; width:250px; margin-left:100px;" />
    <input class="btn" type="submit" name="PI" id="PI" value="Pull Printer and Ink Data" style="height:125px; width:250px; margin-left:100px;" />
	<br><br><br>
	<input class="btn2" type="submit" name="PID" id="PID" value="Download" style="height:25px; width:100px; margin-left:175px;" />
	<input class="btn2" type="submit" name="PID" id="PID" value="Download" style="height:25px; width:100px; margin-left:250px;" />
	<input class="btn2" type="submit" name="PID" id="PID" value="Download" style="height:25px; width:100px; margin-left:250px;" />
</form>


<?php
function pseries(){
	while (@ ob_end_flush()); // end all output buffers if any

	$proc = popen('python /var/services/web/Epson_WS/main.py P', 'r');
	echo '<pre>';
	while (!feof($proc))
	{
	    echo fread($proc, 4096);
	    @ flush();
	}
	download_file();
	echo '</pre>';
}

function tseries(){
	while (@ ob_end_flush()); // end all output buffers if any

	$proc = popen('python /var/services/web/Epson_WS/main.py T', 'r');
	echo '<pre>';
	while (!feof($proc))
	{
	    echo fread($proc, 4096);
	    @ flush();
	}
	download_file();
	echo '</pre>';
}

function printer_ink(){
	while (@ ob_end_flush()); // end all output buffers if any

	$proc = popen('python /var/services/web/Epson_WS/main.py PI', 'r');
	echo '<pre>';
	while (!feof($proc))
	{
	    echo fread($proc, 4096);
	    @ flush();
	}
	download_file();
	echo '</pre>';
}

if(array_key_exists('T',$_POST)){
  tseries();
}
if(array_key_exists('P',$_POST)){
  pseries();
}
if(array_key_exists('PI',$_POST)){
  printer_ink();
}
function download_file(){
	$files = scandir('/var/services/web/Epson_WS/data_sheets', SCANDIR_SORT_DESCENDING);
	$newest_file = $files[count($files)-3];
	echo $newest_file;
}
?>
