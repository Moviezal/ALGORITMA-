# __UTS ALGORITMA__

NAMA: MUHAMMAD HAFIZH ALFAUZI

KELAS: TI.24.A5

PRODI: TEKNIK INFORMATIKA

MATA KULIAH: ALGORITMA 


# Preview

![foto](https://github.com/Moviezal/ALGORITMA-/blob/312c29c62953f9fa8605b58cc8eaa626cd9fd0e6/1.jpeg)
![foto](https://github.com/Moviezal/ALGORITMA-/blob/312c29c62953f9fa8605b58cc8eaa626cd9fd0e6/2.jpeg)
![foto](https://github.com/Moviezal/ALGORITMA-/blob/312c29c62953f9fa8605b58cc8eaa626cd9fd0e6/3.jpeg)
![foto](https://github.com/Moviezal/ALGORITMA-/blob/312c29c62953f9fa8605b58cc8eaa626cd9fd0e6/4.jpeg)


# __Penjelasan Kode__

_1. Class Barang_

Class ini digunakan untuk menyimpan informasi dasar tentang 8 yang dijual.

Method __init__ menginisialisasi setiap barang dengan atribut kode, nama, dan harga.

Setiap instance Barang akan memiliki data kode barang, nama, dan harga.


_2. Class Item Keranjang_

Class ini merepresentasikan item barang yang ditambahkan ke dalam keranjang, termasuk jumlah barang yang dibeli dan subtotalnya.

Method __init__ menerima parameter barang (objek dari class Barang) dan jumlah, lalu menghitung subtotal (harga barang dikalikan jumlah).

Objek ItemKeranjang akan disimpan dalam list items di class Keranjang.


_3. Class Keranjang_

Class ini mewakili keranjang belanja yang berisi daftar item barang yang dipilih.

Method __init__ menginisialisasi atribut items sebagai list kosong untuk menampung item belanja.

__Method tambah_barang:__

Mengecek apakah barang yang ditambahkan sudah ada dalam keranjang.

Jika barang sudah ada, maka jumlah barang diperbarui, dan subtotal dihitung ulang.

Jika barang belum ada, item baru ditambahkan ke dalam items.


__Method tampilkan daftar:__

Menampilkan daftar barang yang ada di keranjang dengan detail kode, nama, harga, jumlah, dan subtotal.

__Method hitung_total:__
Mengembalikan total harga semua item di keranjang dengan menjumlahkan subtotal dari setiap ItemKeranjang.


_4. Class Kasir_

Class ini bertindak sebagai pengelola keranjang belanja dan menyimpan daftar barang yang tersedia di toko.

Method __init__:

Membuat objek Keranjang untuk menampung item belanja.

Inisialisasi daftar_barang, yaitu dictionary yang menyimpan data beberapa barang yang dijual.


Method tambah_ke_keranjang: Menambahkan barang ke keranjang berdasarkan kode_barang yang diinput oleh pengguna.

Jika kode_barang valid, barang ditambahkan ke keranjang, dan pesan konfirmasi ditampilkan.

Jika tidak valid, pesan kesalahan ditampilkan.


Method cetak_struk: Mencetak struk belanja yang berisi tanggal transaksi, daftar barang di keranjang, total belanja, dan ucapan terima kasih.


_5. Fungsi main_

Fungsi utama yang menyediakan menu interaktif bagi pengguna.

Fungsi ini menjalankan loop yang menawarkan pilihan berikut:

1: Menampilkan daftar barang yang tersedia dan memungkinkan pengguna menambahkan barang ke keranjang dengan memilih kode dan jumlah barang.

2: Menampilkan daftar barang dalam keranjang beserta total harganya.

3: Mencetak struk lengkap dengan informasi tanggal, daftar barang, total harga, dan ucapan terima kasih.

4: Mengakhiri program dengan menampilkan pesan terima kasih.


Setiap pilihan dijalankan menggunakan if-elif, dan input digunakan untuk menerima masukan pengguna.


__Alur Penggunaan Program__

1. Saat program dijalankan, objek Kasir dibuat, dan daftar barang yang tersedia ditampilkan dalam pilihan menu.


2. Pengguna dapat:

Memilih "1" untuk menambah barang ke keranjang dengan memasukkan kode barang dan jumlah yang ingin dibeli.

Memilih "2" untuk melihat daftar barang di keranjang dan total sementara.

Memilih "3" untuk mencetak struk lengkap dengan rincian pembelian.

Memilih "4" untuk mengakhiri program.



3. Program berjalan dalam loop sampai pengguna memilih untuk keluar.

# Hasil dari Penjelasan diatas

![image](https://github.com/user-attachments/assets/ed233267-3db1-4e35-a5c8-c7bd056e694b)

__Ringkasan__

Kode ini membuat aplikasi kasir sederhana yang mengelola transaksi belanja dengan beberapa fitur dasar seperti menambahkan barang, menampilkan daftar belanja, menghitung total, dan mencetak struk.
