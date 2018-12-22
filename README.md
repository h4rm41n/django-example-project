# Administrasi
Project ini adalah contoh aplikasi administrasi surat menyurat dengan menggunakan python 3, django versi 2, bootstrap 4, dan jquery UI serta django view function base. Semoga ada yang mengembangkan menjadi lebih sempurna, baik dari user interface serta algoritma dan alur best practice dari django itu sendiri.

## Berikut ini cara instalasi
*ini ada video cara instalasi untuk windows https://www.youtube.com/watch?v=rELC-g6Yca0*

1. Clone dari repo **git clone https://github.com/h4rm41n/django-example-project**
2. Masuk ke project **cd django-example-project**
3. Membuat dan mengaktifkan environment
    * __**pip install virtualenv**__ (*bagi yang belum install virtualenv*)
    * **virtualenv env** jika terdapat dua versi python yakni python2 dan python3 bisa lebih spesifik ke versi python yang kita inginkan dengan menggunakan command **virtualenv -p python3 env**
    * **source env/bin/activate** = Linux/MAc OS
    * **env\Script\activate** = windows
4. Install django terbaru **pip install django** (file dependensi sengaja tidak diexport karena saat ini dependensi hanya django saja)
5. Migrate database
    * Silahkan menuju ke file **manage.py** dengan command **cd administrasi**
    * **python manage.py makemigrations** jika command tersebut gagal bisa tambahkan nama app di akhir (**python managae.py makemigrations surat_menyurat**), karena kita akan menuju ke file model untuk kebutuhan migrate database yang terdapat di dalam app surat_menyurat.
6. Buat user baru **python manage.py createsuperuser**
7. Jalankan server/program **python manage.py runserver**
8. Terimakasih
