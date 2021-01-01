# TanyaAja - Software Penjawab Semua Pertanyaan Anda

Ini adalah project akhir dari tugas kuliah yang mungkin punya potensi untuk dikembangkan di kemudian hari. Dari judulnya saja sudah mencerminkan isi dari software ini yaitu adalah TanyaAja.

Singkatnya, ini adalah sebuah software yang akan menjawab pertanyaan Anda tentang tema-tema tertentu yang bisa anda ubah sesuai dengan mood anda (dan pastinya anda juga yang harus menyediakan jawabannya).

> Loh? Katanya software pintar ini bisa menjawab pertanyaan, kok malah saya yang harus menyediakan jawabannya

Yah... Tentu saja dong. Kan komputer kalo tidak diberitahu mana yang boleh dijawab hanya akan menyebabkan kegaduhan saja (karena mereka akan menjawab sesuka prosesor mereka). So, anda bisa menyediakan jawabannya sehingga kalian bisa memanfaatkan software sederhana ini untuk beberapa fungsi seperti:

* Customer service
* Tanya jawab dengan murid
* Bot discord

Dan lain sebagainya.

Oke, daripada banyak bacot, lebih baik kali ini kita gunakan untuk penjelasan installasinya.

## Installasi

Installasi nya cukup mudah karena kita juga menggunakan npm ala python untuk menampung depedency nya.

1. Seperti biasa, kalian harus menginstall pip terlebih dahulu
Untuk system operasi berbasis ArchLinux
`sudo pacman -S python-pip`
2. Setelah itu kalian install pipenv untuk project managernya
`pip install pipenv`
3. Kemudian kalian bisa clone repository ini
4. Setelah itu depedency nya bisa kalian install dengan perintah
`pipenv install`
5. Setelah itu kalian bisa melakukan run dengan perintah
`pipenv run python Weighting.py`
6. Query atau pertanyaan bisa kalian masukkan dengan perintah
`pipenv run python Relevance.py`

Gimana? Apakah terlalu mbulet? Mungkin akan di update untuk kedepannya biar bisa menjadi lebih user friendly
