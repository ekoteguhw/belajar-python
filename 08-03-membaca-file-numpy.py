import numpy as np

# membaca file
print("---------- MEMBACA FILE")
path = 'file_angka.txt'
file_angka1 = np.loadtxt(path, delimiter=',')
# skiprows melewati baris bertama, skiprows=2 => dua baris pertama tidak terbaca
file_angka2 = np.loadtxt(path, delimiter=',', skiprows=1)
print("Data dalam file_angka.txt adalah\n", file_angka1)
print("Data dalam file_angka.txt adalah\n", file_angka2)
