from buku import Buku

class MenuConsole:
    def __init__(self, layanan):
        self.layanan = layanan

    def mulai(self):
        while True:
            print("\n=== MENU PERPUSTAKAAN ===")
            print("1. Tambah Buku")
            print("2. Cari Buku")
            print("3. Ubah Buku")
            print("4. Hapus Buku")
            print("5. Lihat Semua Buku")
            print("0. Keluar")

            pilih = input("Pilih menu: ")

            if pilih == "1":
                kode = input("Kode buku: ")
                judul = input("Judul buku: ")
                penulis = input("Penulis: ")
                tahun = input("Tahun terbit: ")

                buku = Buku(kode, judul, penulis, tahun)
                status, pesan = self.layanan.tambah_buku(buku)
                print(pesan)

            elif pilih == "2":
                kode = input("Masukkan kode buku: ")
                buku = self.layanan.cari_buku(kode)
                if buku != None:
                    print("Judul   :", buku.judul)
                    print("Penulis :", buku.penulis)
                    print("Tahun   :", buku.tahun)
                else:
                    print("Data buku tidak ditemukan.")

            elif pilih == "3":
                kode = input("Masukkan kode buku yang ingin diubah: ")
                buku = self.layanan.cari_buku(kode)
                if buku != None:
                    print("(Tekan enter jika tidak diubah)")
                    judul = input("Judul baru (" + buku.judul + "): ")
                    penulis = input("Penulis baru (" + buku.penulis + "): ")
                    tahun = input("Tahun baru (" + buku.tahun + "): ")

                    if judul == "":
                        judul = buku.judul
                    if penulis == "":
                        penulis = buku.penulis
                    if tahun == "":
                        tahun = buku.tahun

                    status, pesan = self.layanan.ubah_buku(kode, judul, penulis, tahun)
                    print(pesan)
                else:
                    print("Buku tidak ditemukan.")

            elif pilih == "4":
                kode = input("Masukkan kode buku yang ingin dihapus: ")
                buku = self.layanan.cari_buku(kode)
                if buku != None:
                    yakin = input("Hapus buku " + buku.judul + "? (y/n): ")
                    if yakin == "y" or yakin == "Y":
                        status, pesan = self.layanan.hapus_buku(kode)
                        print(pesan)
                    else:
                        print("Batal menghapus.")
                else:
                    print("Buku tidak ditemukan.")

            elif pilih == "5":
                daftar = self.layanan.semua_buku()
                if len(daftar) == 0:
                    print("Belum ada data buku.")
                else:
                    for b in daftar:
                        print(b.kode, "-", b.judul, "|", b.penulis, "(" + str(b.tahun) + ")")

            elif pilih == "0":
                print("Keluar dari program.")
                break

            else:
                print("Menu tidak tersedia.")