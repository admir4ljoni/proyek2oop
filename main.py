from repositoryBuku import RepositoryBuku
from perpustakaan import LayananBuku
from menu_console import MenuConsole

if __name__ == "__main__":
    repo = RepositoryBuku("storageBooks.txt")
    repo.memuat()  # wajib: muat data lama dulu, kalau tidak file ketimpa saat simpan pertama
    MenuConsole(LayananBuku(repo)).mulai()
