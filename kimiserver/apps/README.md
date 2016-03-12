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

#Install Dejavu

##Setup MySQL

Kita buat table dulu di MySQL:
```
$ mysql -u root -p
Enter password: Kimi123
mysql> CREATE DATABASE IF NOT EXISTS dejavu;
exit
```

##Download Dejavu
```
$ sudo apt-get install git
$ git clone https://github.com/worldveil/dejavu.git ./dejavu
$ cd dejavu
```

##Fingerprinting
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

##Check partial lagu

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

Setelah di save. kita bisa coba recognize dengan perintah berikut:
```
$ python dejavu.py --recognize file test2.mp3
```
Voila! Sudah bisa dikenali:
```
{'song_id': 4, 'song_name': "05. You Can't Hurry Love (2016 Remastered)", 
'file_sha1': '68B132734B42FDE500E89AC1AEFFBB9F2AF4E50B', 'confidence': 157, 
'offset_seconds': 30.6039, 'match_time': 1.9697608947753906, 'offset': 659}
```

Dia bahkan kenali bahwa ini potongan lagu dari detik ke 30-an. Menarik. :-)
