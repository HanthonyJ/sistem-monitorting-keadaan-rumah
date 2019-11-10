# sistem-monitorting-keadaan-rumah
rancang bangun sebuah alat yang dapat digunakan sebagai alat monitoring keadaan rumah jarak jauh. alat ini dibangun dengan menggunakan raspberry pi 3, sensor gerak infra merah, sensor pintu, picamera dan kamera usb universal
alat ini dapat memberikan notifikasi kepada pengguna lewat telegram dan dapat digunakan untuk streaming keadaan rumah dengan menggunakan browser
notifikasi dikirm ke bot telegram berupa teks dan gambar.
sistem akan mengirim pesan teks ketika sensor pintu mendeteksi ada pergerakan pintu.
sistem akan mengambil gambar (picamera) dan mengirim gambar ketika sensor gerak mendeteksi ada pergerakan manusia
streaming (usb camera) dapat menggunakan browser

library yang perlu diinstal antara lain:
telepot, untuk menggunakan telegram bot sebagai penerima pesan teks dan gambar
gpio, untuk mengaktifkan fungsi pin gpio pada raspberry pi
motion,digunakan untuk menjalankan webstreaming
future, digunakan supaya sistem dapat mengirim gambar secara otomatis dan langsung ketika picamera telah mengambil gambar 
