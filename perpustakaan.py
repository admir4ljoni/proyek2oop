from buku import Buku
from repositoryBuku import RepositoryBuku

class LayananBuku:
    def __init__(self, repo : RepositoryBuku):
        self.__repo = repo

    def tambah(self, buku : Buku) -> bool:
        if self.__repo.ada(buku.kode):
            return False
        self.__repo.taruh(buku)
        self.__repo.simpan()
        return True

    def cari(self, kode : str) -> Buku:
        return self.__repo.ambil(kode)

    def hapus(self, kode : str) -> bool:
        if not self.__repo.ada(kode):
            return False
        self.__repo.hapus(kode)
        self.__repo.simpan()
        return True

    def ubah(self, kode : str, judul : str, penulis : str, tahun : int) -> bool:
        if not self.__repo.ada(kode):
            return False
        buku = Buku(kode, judul, penulis, tahun)
        self.__repo.taruh(buku)
        self.__repo.simpan()
        return True

if __name__ == "__main__":
    from types import SimpleNamespace

    class GudangPalsu:
        def __init__(self):
            self.data = {}
            self.jumlah_simpan = 0

        def ada(self, kode):
            return kode in self.data

        def ambil(self, kode):
            return self.data.get(kode)

        def taruh(self, buku):
            self.data[buku.kode] = buku

        def buang(self, kode):
            del self.data[kode]

        def simpan(self):
            self.jumlah_simpan += 1

    gudang = GudangPalsu()
    layanan = LayananBuku(gudang)
    buku = SimpleNamespace(kode="B001", judul="Dasar Python", penulis="Andi", tahun=2020)

    print("1. tambah baru       :", layanan.tambah(buku))
    print("2. tambah duplikat   :", layanan.tambah(buku))
    print("3. cari ada          :", layanan.cari("B001").judul)
    print("4. cari tidak ada    :", layanan.cari("B999"))
    print("5. ubah ada          :", layanan.ubah("B001", "Python Lanjut", "Andi", 2023))
    print("   judul sekarang    :", layanan.cari("B001").judul)
    print("6. ubah tidak ada    :", layanan.ubah("B999", "X", "Y", 2000))
    print("7. hapus ada         :", layanan.hapus("B001"))
    print("   cari setelah hapus:", layanan.cari("B001"))
    print("8. hapus tidak ada   :", layanan.hapus("B001"))
    print("Jumlah simpan        :", gudang.jumlah_simpan)