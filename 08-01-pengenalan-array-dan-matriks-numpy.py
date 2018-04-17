import numpy as np # panggil dengan np

# mendefinisikan array pada numpy
print("---------- MENDEFINISIKAN ARRAY DAN MATRIKS")
arrOne = np.array([1, 2, 3, 4, 5])
print("Nilai array satu dimensi:\n", arrOne)

arrTwo = np.array([[1, 2, 3], [4, 5, 6]]) # terdiri dari 2 baris dan 3 kolom
print("Nilai array dua dimensi:\n", arrTwo)

matriks = np.matrix([[1, 2, 3], [4, 5, 6]]) # untuk operasi aljabar linear
print("Isi dari matriks:\n", matriks)

arrN = np.array([[[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]], [[5, 5, 5], [6, 6, 6]]])
print("Nilai array N dimesi:\n", arrN)

np1 = np.full((2, 3), 5) # 2 baris, 3 kolom, dengan isinya 5
print("Nilai dari np1:\n", np1)

# melihat deskripsi dari data array:
# bentuk (size), min, max, std, var
print("---------- MELIHAT DESKRIPSI SUATU ARRAY")
print("Ukuran dari array dua dimensi: ", arrTwo.shape)
print("Ukuran dari array dua dimensi untuk baris: ", arrTwo.shape[0]) # kolom menggunakan shape[1]

print("Ukuran dari array N dimensi: ", arrN.shape)
print("Nilai min dari array dua dimensi: ", arrTwo.min()) # untuk max ganti min() dengan max()
print("Nilai standar deviasi dari array dua dimensi: ", arrTwo.std())
print("Nilai variansi dari array dua dimensi: ", arrTwo.var())

# indexing dari array numpy
print("Array dua dimensi:\n", arrTwo)
print("Tes indexing untuk baris ke-1 kolom ke-2 array numpy: ", arrTwo[1, 2])
print("Tes indexing untuk melihat baris ke-1 kolom ke-1 sampai ke-3: ", arrTwo[1, 1:3])
print("Tes indexing untuk melihat semua komponen di baris ke-1: ", arrTwo[1, :])

print("---------- OPERASI ALJABAR LINIER DENGAN MATRIKS")
matriks2 = np.matrix([[2, 6, 9], [0, -1, 4]])
print("Matriks1 adalah\n", matriks)
print("Matriks2 adalah\n", matriks2)
matriks3 = np.add(matriks, matriks2)
print("Hasil penjumlahan matriks1 dan matriks2 adalah\n", matriks3)
# untuk pengurangan gunakan perintah np.substract(m1, m2)
# untuk transpose matriks, gunakan .T
print("Transpose matriks:\n", matriks3.T)
# untuk inverse matriks, harus dalam ukuran baris dan kolom yang sama
matriks4 = np.dot(matriks.T, matriks2)
print("Matriks4 adalah\n", matriks4)
print("Inverse matriks:\n", np.linalg.inv(matriks4))
