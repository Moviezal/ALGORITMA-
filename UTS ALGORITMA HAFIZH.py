from datetime import datetime

class Barang:
    def __init__(self, kode, nama, harga):  # Ganti _init_ menjadi __init__
        self.kode = kode
        self.nama = nama
        self.harga = harga

class ItemKeranjang:
    def __init__(self, barang, jumlah):  # Ganti _init_ menjadi __init__
        self.barang = barang
        self.jumlah = jumlah
        self.subtotal = barang.harga * jumlah

class Keranjang:
    def __init__(self):  # Ganti _init_ menjadi __init__
        self.items = []
        
    def tambah_barang(self, barang, jumlah):
        # Cek apakah barang sudah ada di keranjang
        for item in self.items:
            if item.barang.kode == barang.kode:
                item.jumlah += jumlah
                item.subtotal = item.barang.harga * item.jumlah
                return
        
        # Jika barang belum ada, tambahkan sebagai item baru
        item_baru = ItemKeranjang(barang, jumlah)
        self.items.append(item_baru)
    
    def tampilkan_daftar(self):
        print("\nDaftar Belanja:")
        print("=" * 50)
        print("Kode\tNama\t\tHarga\tJumlah\tSubtotal")
        print("-" * 50)
        for item in self.items:
            print(f"{item.barang.kode}\t{item.barang.nama}\t\t{item.barang.harga}\t{item.jumlah}\t{item.subtotal}")
    
    def hitung_total(self):
        return sum(item.subtotal for item in self.items)

class Kasir:
    def __init__(self):  # Ganti _init_ menjadi __init__
        self.keranjang = Keranjang()
        # Daftar barang yang tersedia (simulasi database)
        self.daftar_barang = {
            "A001": Barang("A001", "Sirup", 12000),
            "A002": Barang("A002", "Susu", 18000),
            "A003": Barang("A003", "Teh", 5000),
        }
    
    def tambah_ke_keranjang(self, kode_barang, jumlah):
        if kode_barang in self.daftar_barang:
            barang = self.daftar_barang[kode_barang]
            self.keranjang.tambah_barang(barang, jumlah)
            print(f"Berhasil menambahkan {jumlah} {barang.nama} ke keranjang")
        else:
            print("Barang tidak ditemukan!")
    
    def cetak_struk(self):
        print("\n" + "=" * 50)
        print("STRUK BELANJA")
        print("Tanggal:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("=" * 50)
        
        self.keranjang.tampilkan_daftar()
        
        total = self.keranjang.hitung_total()
        print("-" * 50)
        print(f"Total Belanja: Rp {total}")
        print("=" * 50)
        print("Terima kasih telah berbelanja!")
        print("=" * 50)

# Contoh penggunaan
def main():
    kasir = Kasir()
    
    while True:
        print("\nMenu:")
        print("1. Tambah Barang")
        print("2. Lihat Keranjang")
        print("3. Cetak Struk")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == "1":
            print("\nDaftar Barang Tersedia:")
            for kode, barang in kasir.daftar_barang.items():
                print(f"{kode} - {barang.nama} (Rp {barang.harga})")
            kode = input("Masukkan kode barang: ")
            jumlah = int(input("Masukkan jumlah: "))
            kasir.tambah_ke_keranjang(kode, jumlah)
            
        elif pilihan == "2":
            kasir.keranjang.tampilkan_daftar()
            print(f"Total: Rp {kasir.keranjang.hitung_total()}")
            
        elif pilihan == "3":
            kasir.cetak_struk()
            
        elif pilihan == "4":
            print("Terima Kasih!")
            break
            
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
