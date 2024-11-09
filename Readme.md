__UTS ALGORITMA__

NAMA: MUHAMMAD HAFIZH ALFAUZI

KELAS: TI.24.A5

PRODI: TEKNIK INFORMATIKA

MATA KULIAH: ALGORITMA 

__Penjelasan Kode Python__

1. Class Barang

Class ini digunakan untuk menyimpan informasi dasar tentang barang yang dijual.

Method __init__ menginisialisasi setiap barang dengan atribut kode, nama, dan harga.

Setiap instance Barang akan memiliki data kode barang, nama, dan harga.


2. Class ItemKeranjang

Class ini merepresentasikan item barang yang ditambahkan ke dalam keranjang, termasuk jumlah barang yang dibeli dan subtotalnya.

Method __init__ menerima parameter barang (objek dari class Barang) dan jumlah, lalu menghitung subtotal (harga barang dikalikan jumlah).

Objek ItemKeranjang akan disimpan dalam list items di class Keranjang.


3. Class Keranjang

Class ini mewakili keranjang belanja yang berisi daftar item barang yang dipilih.

Method __init__ menginisialisasi atribut items sebagai list kosong untuk menampung item belanja.

Method tambah_barang:

Mengecek apakah barang yang ditambahkan sudah ada dalam keranjang.

Jika barang sudah ada, maka jumlah barang diperbarui, dan subtotal dihitung ulang.

Jika barang belum ada, item baru ditambahkan ke dalam items.


Method tampilkan_daftar: Menampilkan daftar barang yang ada di keranjang dengan detail kode, nama, harga, jumlah, dan subtotal.

Method hitung_total: Mengembalikan total harga semua item di keranjang dengan menjumlahkan subtotal dari setiap ItemKeranjang.


4. Class Kasir

Class ini bertindak sebagai pengelola keranjang belanja dan menyimpan daftar barang yang tersedia di toko.

Method __init__:

Membuat objek Keranjang untuk menampung item belanja.

Inisialisasi daftar_barang, yaitu dictionary yang menyimpan data beberapa barang yang dijual.


Method tambah_ke_keranjang: Menambahkan barang ke keranjang berdasarkan kode_barang yang diinput oleh pengguna.

Jika kode_barang valid, barang ditambahkan ke keranjang, dan pesan konfirmasi ditampilkan.

Jika tidak valid, pesan kesalahan ditampilkan.


Method cetak_struk: Mencetak struk belanja yang berisi tanggal transaksi, daftar barang di keranjang, total belanja, dan ucapan terima kasih.


5. Fungsi main

Fungsi utama yang menyediakan menu interaktif bagi pengguna.

Fungsi ini menjalankan loop yang menawarkan pilihan berikut:

1: Menampilkan daftar barang yang tersedia dan memungkinkan pengguna menambahkan barang ke keranjang dengan memilih kode dan jumlah barang.

2: Menampilkan daftar barang dalam keranjang beserta total harganya.

3: Mencetak struk lengkap dengan informasi tanggal, daftar barang, total harga, dan ucapan terima kasih.

4: Mengakhiri program dengan menampilkan pesan terima kasih.


Setiap pilihan dijalankan menggunakan if-elif, dan input digunakan untuk menerima masukan pengguna.


Alur Penggunaan Program

1. Saat program dijalankan, objek Kasir dibuat, dan daftar barang yang tersedia ditampilkan dalam pilihan menu.


2. Pengguna dapat:

Memilih "1" untuk menambah barang ke keranjang dengan memasukkan kode barang dan jumlah yang ingin dibeli.

Memilih "2" untuk melihat daftar barang di keranjang dan total sementara.

Memilih "3" untuk mencetak struk lengkap dengan rincian pembelian.

Memilih "4" untuk mengakhiri program.



3. Program berjalan dalam loop sampai pengguna memilih untuk keluar.



Ringkasan

Kode ini membuat aplikasi kasir sederhana yang mengelola transaksi belanja dengan beberapa fitur dasar seperti menambahkan barang, menampilkan daftar belanja, menghitung total, dan mencetak struk.
