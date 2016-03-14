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

Untuk melakukan instalasi Kimiserver, kita menggunakan open source project Dejavu

###Setting di Debian

Dejavu ditulis menggunakan python, dan kita perlu melakukan instalasi beberapa python library beserta juga MySQL. Sayangnya, petunjuk yg tersedia adalah untuk Fedora linux, dan saya biasanya menggunakan Debian. Jadi saya coba buat instalasi menggunakan Debian.

Kita bersihkan dulu server Debian:

```
$ sudo apt-get update
$ sudo apt-get upgrade
```

###Install MySQL Server

```
$ sudo apt-get install mysql-server mysql-client
```
Untuk password mysql, kita gunakan saja `Kimi123` 

###Install Python library

Jika kita belum punya pip (python installer), kita install terlebih dulu:
```
$ sudo apt-get install python-pip python-dev build-essential 
```
Kita install semua python library yg dibutuhkan:
```
$ sudo apt-get install python-scipy
$ sudo apt-get install python-matplotlib
$ sudo apg-get install ffmpeg
$ sudo apt-get install portaudio19-dev
```
Setelah itu kita gunakan pip untuk install yg lainnya:
```
$ sudo pip install PyAudio
$ sudo pip install pydub
```
Untuk project ini, kita juga perlu install library untuk access RabbitMQ
```
$ sudo pip install pika
```
Sampai disini harusnya sudah selesai semua, dan kita bisa lanjutkan untuk install MySQL

###Setup MySQL

Kita buat table dulu di MySQL:
```
$ mysql -u root -p
Enter password: Kimi123
mysql> CREATE DATABASE IF NOT EXISTS dejavu;
exit
```

###Fingerprinting
Di dalam directory `dejavu` ada directory `mp3` tempat musik yg mau kita fingerprint untuk masuk ke database. 

**Kita copy semua files mp3 yg mau kita fingerprinting dan kita masukkan ke sana.**

Kemudian kita buat file python untuk fingerprinting:

```
nano kimi_fp.py
```
Ini isinya:
```
from dejavu import Dejavu

print "Kimi Fingerprint"
print "Masukkan file mp3 di directory mp3 untuk di ambil fingerprint"
print "---------"

config = {
     "database": {
         "host": "127.0.0.1",
         "user": "root",
         "passwd": "Kimi123",
         "db": "dejavu",
     }
}

djv = Dejavu(config)

djv.fingerprint_directory("mp3", [".mp3"], 3)

print "Selesai. Total fingerprint:"
print djv.db.get_num_fingerprints()
```
Kemudian kita jalankan program di atas:
```
$ python kimi_fp.py
```
Untuk fingerprintnya makan waktu cukup lumayan untuk yg ngga sabaran, jadi mungkin testing dengan 5 lagu saja. Juga, program ini cukup smart untuk tinggal meneruskan kalau sudah ada di database. Jadi kalau di break dan dilanjutkan, dia akan continue.

O iya, ada beberapa lagu yg kena `divide by zero`, kurang tahu juga apakah tetap masuk atau tidak, belum di cek.

###Check partial lagu

Notifikasi datang ke aplikasi `kimi_agent.py` melalui RabbitMQ yg dikirim oleh PHP.

Untuk cek partial lagu, coba potong saja lagu mp3, di atas 6 detik (saya coba 10 detik). Tentu lagu yg dipotong harus ada di dalam database.

Saya copy dari laptop dan masukkan ke dalam server. Filenya cukup kecil, saya ambil quality yg paling jelek. Kalo lagi iseng, bisa juga rekam pakai hape dan save sebagai mp3 untuk kemudian di copy ke linux mesin ini.
```
-rw-r--r-- 1 root root 126509 Mar  8 23:47 test2.mp3
```

Sebelum recognize, kita set dulu confignya.
```
$ nano dejavu.cnf
```
Dan masukkan isinya:
```
{
    "database": {
        "host": "127.0.0.1",
        "user": "root",
        "passwd": "Kimi123",
        "db": "dejavu"
    }
}
```


Setelah itu jalankan berikut (Phyton):

```
$ cd ~/kimi/kimiserver/apps
$ python kimi_agent.py
```

Semua lagu yg di kirim dari kimibox akan langsung dikenali.
