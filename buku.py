class Buku:
    def __init__(self, kode, judul, penulis, tahun):
        self.kode = kode
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun
    def to_line(self):
        return f"{self.kode | self.judul | self.penulis | self.tahun}/n"
