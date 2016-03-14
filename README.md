# KIMI Platform

Untuk penjelasan mengenai project ini, bisa dilihat di Wiki. https://github.com/KawalMusikIndonesia/Kimi/wiki

Cara running KIMI Platform (prototype):

```
$ git clone https://github.com/KawalMusikIndonesia/kimi.git
$ cd kimi
```

##Apache

Pertama kita copy directory ke /var/www/kimi

```
$ cd ~/kimi/kimiserver/www/kimi
$ mkdir /var/www/kimi
$ cp * /var/www/kimi
```

Sebelumnya harus install RabbitMQ supaya jalan. Coba lihat di petunjuk di `~/kimi/kimiserver/`.


##Kimibox

Kita running kimibox, untuk simpan mp3 dan upload.

###di terminal ssh #1
```
$ cd ~/kimi/kimibox
$ ./kimibox.sh
```
Script ini akan generate file khusus #box-timestamp.mp3 di directory `~/kimi/kimibox/mp3_result`.


###di terminal ssh #2
```
$ cd ~/kimi/kimibox
$ ./kimibox_uploader.sh
```
Script ini akan upload semua file di `~/kimi/kimibox/mp3_result` dan setelahnya memindahken ke directory `~/kimi/kimibox/mp3_uploaded`. File di directory `mp3_uploaded` setelahnya boleh di hapus.

##KimiServer

Untuk memastikan Kimi server berjalan, harus diinstall beberapa komponen, bisa di lihat di `~/kimi/kimiserver`.

Setelah itu jalankan berikut (Phyton):

```
$ cd ~/kimi/kimiserver/apps
$ python kimi_agent.py
```

