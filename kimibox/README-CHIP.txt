Setting awal CHIP

1. Colok kabel TRRS, model kabel audio headphone 3.5m ke CHIP. 
2. Di ujung satu lagi nya, Colok kabel RCA warna kuning ke TV. 
3. Colok kabel power micro USB ke USB. 
4. Port USB yang besar untuk Keyboard atau sound card
5. Setelah di colok ke TV, akan terlihat booting linux. 
6. CHIP bakal load Xfce 
7. Connect ke Wifi
8. Catat IP address CHIP


Koneksi ke CHIP tanpa TV
1. Nyalakan CHIP
2. Catat IP address CHIP. Ini bisa di dapat dari router WIFI. 
3. Dari Windows, bisa menggunkan Putty Terminal
4. Connect ke CHIP ,contoh 192.168.0.22 Port 22
5. Login: root, Password: chip
6. Ini sudah full terminal dari CHip


Koneksi ke CHIP dengan VNC
1. Setelah login ke terminal melalui Putty, execute "vncserver" dari commmand line
2. Jalankan VNCViewer dari Windows atau MAc
3. Connect ke 192.168.0.22:1
4. Password VNC: dematio


Sound recording
1. Saat ini, recording di perlukan USB sound card.
2. Colok USB Sound Card. CHIP hanya mempunyai 1 USB port. 
3. Saat production, kita bisa record langsung dengan CHIP tanpa USB SOund card. Tapi perlu modifikasi. 
4. Untuk test audio, gunakan XFCE > Multimedia > Pulse Audio Sound Control.
5. Dengan Pulse Audio, kita bisa memilih sound card mana yang di pakai. Built sound atau USB Sound card.
6. Jika program tidak ada, dapat di install dengan 
   sudo apt-get install pavucontrol
7. Untuk test recording, panggil program XFCE > Multimedia > Audacity


Informasi lebih lanjut:
http://docs.getchip.com/






 

