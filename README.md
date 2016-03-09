# KIMI Platform

Untuk penjelasan mengenai project ini, bisa dilihat di Wiki.

## Kimibox

Box yang bertugas melaporkan lagu yg sedang di putar. Box ini akan mengambil suara dari mic setiap 1 menit dan membuat fingerprint untuk dikirimkan.

Yang sudah dibuat:

1. Baca dari file dan buat fingerprint (python)
2. Kirim fingerprint ke server (php)

TODO: 

1. Di server akan dikirimkan ke Queue untuk di proses (php). Mungkin akan menggunakan rabbitmq (rabbitmq.com), supaya mudah di distribusikan ke banyak server.
2. Membuat program untuk listen ke queue dimana paket dikirimkan, dan melakukan identifikasi lagu.
 

