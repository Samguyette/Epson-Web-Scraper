<h4>Created by: Intern Sam<h4>
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

<html>
	<body background="back.png">
	<img src="logo.png"
       width="150"
       height="100">
</html>


<form method="post">
    <input class="btn" type="submit" name="P" id="P" value="Pull P-Series Data" onclick="move()" style="height:125px; width:250px; margin-left:450px;" />
    <input class="btn" type="submit" name="T" id="T" value="Pull T-Series Data" onclick="move()"style="height:125px; width:250px; margin-left:100px;" />
    <input class="btn" type="submit" name="PI" id="PI" value="Pull Printer and Ink Data" onclick="move()" style="height:125px; width:250px; margin-left:100px;" />
</form>
<br><br> ALLOW 10 MINUTE RUN TIME AFTER START. <br><br>

<html>
<style>
#myProgress {
  width: 100%;
  background-color: #ddd;
}

#myBar {
  width: 0%;
  height: 30px;
  background-color: #4CAF50;
}
</style>
<body>

<div id="myProgress">
  <div id="myBar"></div>
</div>

<script>
function move() {
  var elem = document.getElementById("myBar");
  var width = 1;
  var id = setInterval(frame, 10);
  function frame() {
    if (width >= 100) {
      clearInterval(id);
    } else {
      width = width + Math.random()/290;
      elem.style.width = width + '%';
    }
  }
}
</script>


<?php
function pseries(){
	echo "Fake loading bar, real data.";
	ob_start();
	passthru('python /var/services/web/Epson_WS/main.py P');
	$output = ob_get_clean();
	echo "<pre>";
	echo $output;
	$date = date("Y-m-d");
	$outputfile= $date . "_P-Series.xlsx";
	echo "<BR><a href=\"Epson_WS/data_sheets/";
	echo $outputfile;
	echo "\">";
	echo $outputfile;
	echo "</a>";
	passthru('python /var/services/web/Epson_WS/email_sender.py P');
	ob_end_flush();
}
function tseries(){
	echo "Fake loading bar, real data.";
	ob_start();
	passthru('python /var/services/web/Epson_WS/main.py T');
	$output = ob_get_clean();
	echo "<pre>";
	echo $output;
	$date = date("Y-m-d");
	$outputfile= $date . "_T-Series.xlsx";
	echo "<BR><a href=\"Epson_WS/data_sheets/";
	echo $outputfile;
	echo "\">";
	echo $outputfile;
	echo "</a>";
	passthru('python /var/services/web/Epson_WS/email_sender.py T');
	ob_end_flush();
}
function printer_ink(){
	echo "Fake loading bar, real data.";
	ob_start();
	passthru('python /var/services/web/Epson_WS/main.py PI');
	$output = ob_get_clean();
	echo "<pre>";
	echo $output;
	$date = date("Y-m-d");
	$outputfile= $date . "_Printer_and_Ink.xlsx";
	echo "<BR><a href=\"Epson_WS/data_sheets/";
	echo $outputfile;
	echo "\">";
	echo $outputfile;
	echo "</a>";
	passthru('python /var/services/web/Epson_WS/email_sender.py PI');
	ob_end_flush();
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
?>

</body>
</html>
