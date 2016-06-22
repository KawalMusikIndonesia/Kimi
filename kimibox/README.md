#Kimibox

##Requirement
1. sox: untuk sound processing: recording, check maximum amplitude
```
sudo apt-get install sox
```
2. lamme untuk konverter dari wav ke mp3
```
sudo apt-get install lamme
```
3. curl: uploader
```
sudo apt-get install curl
```

Di dalam kimibox, kita running

1. kimi.sh

##Kimi.sh

Tugasnya adalah menunggu setiap 1 menit dan rekam selama 10 detik.

Karena merekam belum bisa dilakukan (belum program di CHIP atau raspberry), maka skenario seperti berikut:

1. Tunggu selama 1 menit
2. Recording selama 10 detik dalam bentuk .wav
3. optioanl: Konvert menjadi mono dari stereo
4. konvert wav menjadi mp3 dengan lamme
5. check maximum amplitudo, jika lebih dari treshhold maka upload ke server

##Running background
kimi.sh harus running automatic setelah boot kita gunakan [supervisord](http://supervisord.org/installing.html)
###install
```
sudo pip install supervisor
```
###configuration
```
[program:kimi]
command=/home/pi/kimi.sh
```
