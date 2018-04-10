# Output
print("print Output dengan print()")

# Output dengan variabel
a = 10
b = 1000
print("Nilai a adalah: ", a)
print('Nilai b adalah: ' + str(b))

# Input
nama = input("Masukkan nama Anda: ")
print("Nama Anda adalah ", nama)

# Operasi
c = 50
d = 15

e = c + d
f = c - d
g = c * d
h = c / d
i = c ** d

# Print Format
# Old '%s %s' % ('satu', 'dua')
# New '{} {}'.format('satu', 'dua')
# Old '%d %d' % (1,2)
# New '{} {}'.format(1,2)

print("Hasil penjumlahan {} + {} adalah {}".format(c, d, e))
print("Hasil pengurangan {} - {} adalah {}".format(c, d, f))
print("Hasil perkalian {} * {} adalah {}".format(c, d, g))
print("Hasil pembagian {} / {} adalah {}".format(c, d, h))
print("Hasil perpangkatan {} ^ {} adalah {}".format(c, d, i))
