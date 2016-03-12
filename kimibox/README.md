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



