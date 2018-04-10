# Di Python, kita tidak perlu mendefinisikan variabel
a = 1 # type number
b = "Petik dua" # type string
c = 'Petik satu' # type string
d = 1.25 # type float/double
e = False # type boolean
f = ['satu', 'dua', 3, 4.0, 'lima'] # type list
g = {'nama': 'Eko', 'umur': 29, 'tinggi': 174} # type dictionary
h = (1,2,3,4,5) # type tuple
# type array, saran: gunakan package numpy

print("Tipe variabel a adalah ", type(a))
print("Tipe variabel b adalah ", type(b))
print("Tipe variabel d adalah ", type(d))
print("Tipe variabel e adalah ", type(e))
print("Tipe variabel f adalah ", type(f))
print("Tipe variabel g adalah ", type(g))
print("Tipe variabel h adalah ", type(h))

# list dalam python
print("Data ke-3 adalah {}".format(f[2]))
print("Data ke-1 sampai ke-3 adalah {}".format(f[0:3]))
# panjang dari sebuah list
print("Panjang list f adalah {}".format(f.__len__()))

# menambahkan data dalam list
f.append(6)
print("Data di f setelah ditambahkan adalah {}".format(f))

# menghapus data dalam list
f.remove('dua')
print("Data di f setelah dihapus adalah {}".format(f))

# bentuk lain menghapus
del f[3]
print("Data di f setelah dihapus adalah {}".format(f))

# menggunakan dictionary
print("Dictionary di g adalah {}".format(g))
print("Nama dalam Dictionary g adalah {}".format(g['nama']))
# merubah nama
g['nama'] = 'Eko Teguh Widodo'
print("Dictionary di g setelah nama diubah adalah {}".format(g))
# menambah key:value
g['hobi'] = 'Coding'
print("Dictionary di g setelah menambah key:value adalah {}".format(g))
# menghapus value berdasarkan key, yg terhapus adalah key:value
del g['umur']
print("Dictionary di g setelah umur dihapus adalah {}".format(g))

# tuple untuk koordinat (x,y,z,...)
# akses per komponen
print("Tuple untuk index ke-2 adalah {}".format(h[2]))
print("Tuple untuk index ke-0 sampai index ke-3 adalah {}".format(h[:3]))
