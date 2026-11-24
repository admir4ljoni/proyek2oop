from buku import Buku
from repositoryBuku import RepositoryBuku

class LayananBuku:
    def __init__(self, repo : RepositoryBuku):
        self.__repo = repo

    def tambah_buku(self, buku : Buku) -> bool:
        if self.__repo.ada(buku.kode):
            return False
        self.__repo.taruh(buku)
        return True

    def cari_buku(self, kode : str) -> Buku:
        return self.__repo.ambil(kode)

    def hapus_buku(self, kode : str) -> bool:
        if not self.__repo.ada(kode):
            return False
        self.__repo.hapus(kode)
        return True

    def ubah_buku(self, kode : str, judul : str, penulis : str, tahun : int) -> bool:
        if not self.__repo.ada(kode):
            return False
        buku = Buku(kode, judul, penulis, tahun)
        self.__repo.taruh(buku)
        return True

    def semua_buku(self) -> Buku :
        return self.__repo.semua()