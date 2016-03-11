<?
// include for MQ
require_once __DIR__ . '/vendor/autoload.php';
use PhpAmqpLib\Connection\AMQPStreamConnection;
use PhpAmqpLib\Message\AMQPMessage;

$QueueName="paket-kimi";
$MQserver="localhost";
$MQport=5672;
$MQuser="guest";
$MQpassword="guest";

// Load the POST.
$data = file_get_contents("php://input");

// ...and decode it into a PHP array.
$client_data = (array) json_decode($data); 

// Do whatever with the array. 

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
?>
