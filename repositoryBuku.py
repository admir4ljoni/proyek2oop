from buku import Buku

class RepositoryBuku:
    def __init__(self, nama_file):
        self.nama_file = nama_file
        self.data = {}

    # memuat buku
    def memuat(self):
        try: 
            with open(self.nama_file, "read") as file:
                for baris in f:
                    baris = baris.strip()
                    if baris == "":
                        continue
                    buku = Buku.dari_baris(baris)
                    self.data[buku.kode] = buku
        except FileNotFoundError:
            pass

    # menyimpan
    def simpan(self):
        with open(self.nama_file, "write") as file:
            for buku in self.data.values():
                file.write(buku.ke_baris() + "\n")

    # jika ada
    def ada(self, kode):
        return kode in self.data

    # ambil data
    def ambil(self, kode):
        return self.data.get(kode)

    # nambah buku
    def taruh(self, buku):
        self.data[buku.kode] = buku
        self.simpan()

    # hapus buku
    def hapus(self, kode):
        if kode in self.data:
            del self.data[kode]
            self.simpan()