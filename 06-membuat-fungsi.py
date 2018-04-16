def add(a, b) :
    return a + b

def substract(a, b) :
    return a - b

def sayHello(name) :
    print("Hello, my name is ", name)

def aritmatika(i, j) :
    tambah = i + j
    kurang = i - j
    kali = i * j
    bagi = i / j
    return tambah, kurang, kali, bagi

angka1 = 2
angka2 = 3
print("Hasil penjumlahan: ", add(angka1, angka2))
print("Hasil pengurangan: ", substract(angka1, angka2))
sayHello("Teguh")

print("---------- OPERASI ARITMATIKA")
bil1 = 15
bil2 = 4
mbah, rang, li, gi = aritmatika(bil1, bil2)
print("Operasi penjumlahan: ", mbah)
print("Operasi pengurangan: ", rang)
print("Operasi perkalian: ", li)
print("Operasi pembagian: ", gi)

