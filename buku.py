class Buku:
    def __init__(self, kode, judul, penulis, tahun):
        self.kode = kode
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun
    
    def ke_baris(self):
        return f"{self.kode} | {self.judul} | {self.penulis} | {self.tahun}\n"

    @staticmethod
    def dari_baris(baris):
        hapus = baris.strip()
        bagian = hapus.split(" | ")
        return Buku(bagian[0], bagian[1], bagian[2], int(bagian[3]))


    



