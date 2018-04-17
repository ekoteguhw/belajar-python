# Case study: menghitung BMI, Berat badan ideal

# entitas (nama, jk => 'pria/wanita', berat => kg, tinggi => cm)
class pasien:
    jumlahPasien = 0
    # initialize => constructor
    def __init__(self, nama, jk, berat, tinggi):
        self.nama = nama
        self.jk = jk
        self.berat = berat
        self.tinggi = tinggi
        pasien.jumlahPasien += 1

    def getPasien(self):
        print("---------- INFO PASIEN")
        print("Nama: ", self.nama)
        print("Jenis Kelamin: ", self.jk)
        print("Berat badan: {} kg".format(self.berat))
        print("Tinggi badan: {} cm".format(self.tinggi))

    def hitungBMI(self):
        BMI = self.berat/((self.tinggi/100)**2)
        print("BMI: ", BMI)
        if (BMI < 18.5) :
            print("Kekurangan berat badan.")
        elif (BMI >= 18.5 and BMI < 24.9) :
            print("Berat badan ideal.")
        elif (BMI >= 24.9 and BMI < 29.9) :
            print("Kelebihan berat badan.")
        else :
            print("Kegemukan (obesitas).")

    def beratBadanIdeal(self):
        if(self.jk == 'pria') :
            idealP = (self.tinggi - 100) - (10/100 * (self.tinggi - 100))
            print("Berat badan ideal seharunya adalah {} kg".format(idealP))
        else :
            idealW = (self.tinggi - 100) - (15/100 * (self.tinggi - 100))
            print("Berat badan ideal seharunya adalah {} kg".format(idealW))

# instance
pasien1 = pasien("Teguh", "pria", 78, 174)
# panggil method
pasien1.getPasien()
pasien1.hitungBMI()
pasien1.beratBadanIdeal()

pasien2 = pasien("Ina", "wanita", 62, 163)
pasien2.getPasien()
pasien2.hitungBMI()
pasien2.beratBadanIdeal()

print("---------- END")
print("Jumlah pasien yang sudah diinput adalah ", pasien.jumlahPasien)


# DEBUG ERROR => dengan menggunakan PyCharm
# Kondisi 1
# misalkan baris ke-37 titik dua (:) dihapus, makan ketika program dijalankan akan error
# dengan informasi syntax error, diberikan informasi line ke berapa yang error
# Kondisi 2
# misalkan baris ke-28 and diganti dengan or, makan ketika program dijalankan tidak error
# akan tetapi hasilnya salah, maka errornya lebih kepada logic error
# Gunakan fitur debug, step in, step out, step over



