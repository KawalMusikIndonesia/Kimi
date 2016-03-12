<?php
#print_r($_FILES);
#print_r($_POST);
// include for MQ
require_once __DIR__ . '/vendor/autoload.php';
use PhpAmqpLib\Connection\AMQPStreamConnection;
use PhpAmqpLib\Message\AMQPMessage;

$QueueName="paket-kimi";
$MQserver="localhost";
$MQport=5672;
$MQuser="guest";
$MQpassword="guest";

$namafile=$_POST["namafile"];

$client_data=[];

$client_data['filename']=$namafile;
// added server parameter
$client_data['client-ip']=$_SERVER['REMOTE_ADDR'];
$client_data['user-agent']=$_SERVER['HTTP_USER_AGENT'];
$jam_server=date("Y/m/d") . " " . date("H:i:s");
$client_data['jam-server'] = $jam_server;

$paket_kimi_server=json_encode($client_data);

//print $paket_kimi_server;
// send paket kimi ke MQ
$connection = new AMQPStreamConnection($MQserver, $MQport, $MQuser, $MQpassword);
$channel = $connection->channel();

$channel->queue_declare($QueueName, false, false, false, false);

$msg = new AMQPMessage($paket_kimi_server);
$channel->basic_publish($msg, '', $QueueName);

echo " [x] Sent 1 message\n";

$channel->close();
$connection->close();

// .. finished sending to MQ


$target_dir = "uploads/";
$target_file = $target_dir . basename($_FILES["kimi"]["name"]);
$uploadOk = 1;
$imageFileType = pathinfo($target_file,PATHINFO_EXTENSION);
// Check if image file is a actual image or fake image
$allowed =  array('mp3');
$filename = $_FILES['kimi']['name'];
$ext = pathinfo($filename, PATHINFO_EXTENSION);
if(!in_array($ext,$allowed) ) {
    echo 'error';
    echo "Sorry, only mp3 file allowed.";
    $uploadOk=0;
}


// Check if file already exists
if (file_exists($target_file)) {
    echo "Sorry, file already exists.";
    $uploadOk = 0;
}
// Check file size
if ($_FILES["kimi"]["size"] > 500000) {
    echo "Sorry, your file is too large.";
    $uploadOk = 0;
}
// Check if $uploadOk is set to 0 by an error
if ($uploadOk == 0) {
    echo "Sorry, your file was not uploaded.";
// if everything is ok, try to upload file
} else {
    if (move_uploaded_file($_FILES["kimi"]["tmp_name"], $target_file)) {
        echo "The file ". basename( $_FILES["kimi"]["name"]). " has been uploaded.";
    } else {
        echo "Sorry, there was an error uploading your file.";
	echo "error desc " . $_FILES["userfile"]["error"];
    }
}
?>
