from repositoryBuku import RepositoryBuku
from perpustakaan import LayananBuku
from menu_console import MenuConsole

if __name__ == "__main__":
    repo = RepositoryBuku("database.txt")
    repo.memuat() 
    MenuConsole(LayananBuku(repo)).mulai()
