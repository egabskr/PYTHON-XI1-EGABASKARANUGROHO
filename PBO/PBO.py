class Siswa:
    '''Dasar kelas untuk semua karyawan'''
    jumlah_siswa = 0

    def __init__(self, nama, kelas, umur):
        self.nama = nama
        self.kelas = kelas
        self.umur = umur
        Siswa.jumlah_siswa += 1

    def tampilkan_jumlah(self):
        print("Total siswa:", Siswa.jumlah_siswa)

    def tampilkan_profil(self):
        print("Nama :", self.nama)
        print("Kelas :", self.kelas)
        print("Umur :", self.umur)
        print()

    def tampilkan_kelas(self):
        print("Nama :", self.nama)
        print("Kelas :", self.kelas)
        print()

    def tampilkan_umur(self):
        print("Nama :", self.nama)
        print("Umur :", self.umur)
        print()

siswa1 = Siswa("Sarah", "XI MIA 10", 15)
siswa2 = Siswa("Budi", "XI IIS 13", 17)
siswa3 = Siswa("Andi", "X MIA 5", 14)

siswa1.tampilkan_profil()
siswa2.tampilkan_profil()
siswa3.tampilkan_profil()
siswa1.tampilkan_kelas()
siswa2.tampilkan_kelas()
siswa3.tampilkan_kelas()
siswa1.tampilkan_umur()
siswa2.tampilkan_umur()
siswa3.tampilkan_umur()
print("Total siswa:", Siswa.jumlah_siswa)
