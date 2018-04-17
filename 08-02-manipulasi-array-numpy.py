import numpy as np

arrA = np.array([7, -4, 0, 9, 1, -6, 5, 8, -9])
print("Array A adalah\n", arrA)

# Reshaping array
print("---------- RESHAPING ARRAY")
arrAReshaped = np.reshape(arrA, (3, 3))
arrAReshapedOtomatis = np.reshape(arrA, (3, -1))
print("Reshaping array A ukuran 3 x 3 adalah\n", arrAReshaped)
print("Reshaping array A ukuran 3 x 3 adalah\n", arrAReshapedOtomatis)

# Menghapus bagian dari array
print("---------- DELETE BAGIAN ARRAY")
arrADeleted = np.delete(arrAReshaped, 2, 1) # arr, 1 untuk kolom, 0 untuk baris, 2 => baris/kolom ke-2
print("Deleting array A yang sudah direshaping adalah\n", arrADeleted)

arrADeleted2 = np.delete(arrAReshaped, slice(1, 3), 1) # arr, 1 untuk kolom, 0 untuk baris, (1, 3) => baris/kolom ke-1 dan ke-2
print("Deleting array A yang sudah direshaping adalah\n", arrADeleted2)

# Penggabungan array
print("---------- GABUNG ARRAY")
gabungArr = np.concatenate((arrAReshaped, arrADeleted2.reshape((1, 3))), axis = 0) # axis 1 => horizontal, 0 => vertikal
print("Array gabungan adalah\n", gabungArr)

# penggabungan secara vertical => jumlah kolom harus sama
# penggabungan secara horizontal => jumlah baris harus sama

# Sorting array
print("---------- SORTING ARRAY")
sortedIndex = np.argsort(gabungArr[:, 1]) # : satu lajur baris/kolom, 1 => kolom ke-2
sortedIndex2 = np.argsort(gabungArr[0:3, 0]) # : satu lajur baris, 1 => kolom ke-2
print("Sorted index:\n", sortedIndex)
sortedArr = gabungArr[sortedIndex]
print("Hasil sorted:\n", sortedArr)

print("Sorted index 2:\n", sortedIndex2)
sortedArr2 = gabungArr[sortedIndex2]
print("Hasil sorted 2:\n", sortedArr2)

# Conditional array
print("---------- CONDITIONAL ARRAY") # boolean, true jika terpenuhi
condArr = sortedArr < 5
print("Hasil conditional array:\n", condArr)
sortedArr[condArr] = 0 # buat yang bernilai True isiannya menjadi 0
print("Conditioned array:\n", sortedArr)
