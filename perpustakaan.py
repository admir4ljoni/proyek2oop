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
