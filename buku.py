class Buku:
    def __init__(self, kode, judul, penulis, tahun):
        self.__kode = kode
        self.__judul = judul
        self.__penulis = penulis
        self.__tahun = tahun
    def to_line(self):
        return f"{self.__kode} | {self.__judul} | {self.__penulis} | {self.__tahun}\n"

    def from_line(self, line):
        bersih = line.strip()
        bagian = bersih.split(" | ")
        return Buku(bagian[0], bagian[1], bagian[2], bagian[3])

    def __str__(self):
        return f"{self.__kode} | {self.__judul} | {self.__penulis} | {self.__tahun}"



