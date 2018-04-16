# For Loop
# range(x,y,z) => x start, y stop, z increment

print("---------- INCREMENT FOR LOOP")
for i in range(0, 5, 1) :
    print("Nilai i: ", i)

print("---------- DEFAULT INCREMENT FOR LOOP")
# Default increment adalah 1
for i2 in range(0, 5) :
    print("Nilai i2: ", i2)

print("---------- CUSTOM INCREMENT FOR LOOP")
# Custom increment
for j in range(0, 10, 3) :
    print("Nilai j: ", j)

print("---------- DECREMENT FOR LOOP")
# Decrement
for k in range(5, 0, -1) :
    print("Nilai k: ", k)

print("---------- INCREMENT WHILE LOOP")
# While Loop
p = 0
while (p < 5) :
    print("Nilai p: ", p)
    p = p + 1 # Membuat iterator sendiri
    # bisa menggunakan p += 1

print("---------- CUSTOM INCREMENT WHILE LOOP")
# Custom Increment
q = 0
while (q < 10) :
    print("Nilai q: ", q)
    q = q + 2 # Membuat iterator sendiri
    # bisa menggunakan q += 2

print("---------- DECREMENT WHILE LOOP")
# Decrement
r = 5
while (r > 0) :
    print("Nilai r: ", r)
    r = r - 1 # Membuat iterator sendiri
    # bisa menggunakan r -= 1

