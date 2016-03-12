#Kimibox 

Di dalam kimibox, kita running 2 program:

1. kimibox.sh
2. kimibox_uploader.sh

##Kimibox.sh

Tugasnya adalah menunggu setiap 1 menit dan rekam selama 10 detik.

Karena merekam belum bisa dilakukan (belum program di CHIP atau raspberry), maka skenario seperti berikut:

1. Tunggu selama 1 menit
2. Recording selama 10 detik (belum dilakukan)
3. Hasil recording adalah file test3.mp3
4. Dari hasil recording ini di buat file mp3 -> <boxid><timestamp>.mp3
5. Di copy ke directpry `mp3_result` untuk siap di upload

##Kimibox_uploader.sh

Tugasnya adalah mengawasi directory dan melakukan upload. Sebelumnya install berikut:

```
sudo apt-get install inotify-tools
sudo apt-get install curl
```

Tugas dari aplikasi ini adalah:

1. Monitor directory `mp3_result` untuk semua perubahan
2. List semua files, dan upload satu per satu ke server
3. Pindahkan yg suda di upload ke directory `mp3_uploaded` -> untuk dibersihkan oleh cron nantinya

Untuk uploadnya, di lakukan ke http://kimi.jaskapital.com/upload.php

##upload.php

```php

<?php
print_r($_FILES);
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
```

