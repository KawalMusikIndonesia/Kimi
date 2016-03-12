Berdasarkan penelusuran, ternyata acoustid dan musicbrainz hanya bisa digunakan untuk deteksi full song, dan bukan partial song. Padahal kita butuh deteksi partial song.

Karena itu kita coba untuk menggunakan partial recognition dengan petunjuk dari [Dejavu](https://github.com/worldveil/dejavu) yang terlihat cukup bagus.

#Setting di Debian

Dejavu ditulis menggunakan python, dan kita perlu melakukan instalasi beberapa python library beserta juga MySQL. Sayangnya, petunjuk yg tersedia adalah untuk Fedora linux, dan saya biasanya menggunakan Debian. Jadi saya coba buat instalasi menggunakan Debian.

Kita bersihkan dulu server Debian:

```
$ sudo apt-get update
$ sudo apt-get upgrade
```

##Install MySQL Server

```
$ sudo apt-get install mysql-server mysql-client
```
Untuk password mysql, kita gunakan saja `Kimi123` 

##Install Python library

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

Sampai disini harusnya sudah selesai semua, dan kita bisa lanjutkan untuk masuk ke Dejavu.

##Kimibox.py

Untuk menjalankan kimibox.py, gunakan seperti ini;

USAGE: **python kimibox.py -p <boxid> file <nama file>**

Contohnya:

`python kimibox.py -p 29102 file test2.mp3`

Result:

```
{"boxid": "3523432", "jam-kimibox": "2016/03/11 14:42:46", "fingerprint": "F846E67928F78A795958730139E8D841C039909D"}
 [x] Sent 1 message
 ```
 
 File fingerprint dari `test2.mp3` sudah dipost ke server.

