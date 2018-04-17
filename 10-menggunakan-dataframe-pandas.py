# Mampu menghandle berbagai jenis tipe data
import pandas as pd

# Membaca file dengan pandas
print("---------- MEMBACA FILE")
path = 'file_campuran.txt'
data_campuran = pd.read_csv(path, delimiter=',')
data_campuran_noheader = pd.read_csv(path, delimiter=',', header=1)
print("Data campuran:\n", data_campuran)
print("Shape: ", data_campuran.shape)
print("Data campuran:\n", data_campuran_noheader)

# indexing pada dataframe
print("---------- INDEXING")
print("data baris pertama:\n", data_campuran.iloc[0, :]) # baris ke-1 untuk semua kolom
print("data baris pertama dengan menampilkan umur:\n", data_campuran.iloc[0, 2]) # baris ke-1 untuk kolom ke-3
print("tampilkan semua nama:\n", data_campuran['Nama'])

# menghapus data
print("---------- DELETE DATA")
deletedData = data_campuran.drop('No', axis=1) # axis 1 untuk kolom, 0 untuk baris
print("Deleted data:\n", deletedData)

# membuat dataframe sendiri
newDF = pd.DataFrame([['Hana', 1, 'Lampung']], columns=('Nama', 'Umur', 'Asal'))
print('DF baru:\n', newDF)

# menggabungan dua df
gabungDF = pd.concat([deletedData, newDF], ignore_index=True) #index sudah terupdate dg ignore_index
print("Gabungan DF:\n", gabungDF)

# menghapus data duplikat => preprocessing
noDup = gabungDF.drop_duplicates()
print("Data no duplicate:\n", noDup)

# normalisasi [0, 1]
# rumus normalisasi = (nilai - min) / (max - min)
min = noDup['Umur'].min()
max = noDup['Umur'].max()
normalizeData = noDup.copy()
normalizeData['Umur'] = (noDup['Umur'] - min) / (max - min)
print("Hasil normalisasi adalah\n", normalizeData)
