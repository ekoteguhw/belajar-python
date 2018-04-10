nilaiUjian = 84
keaktifanKelas = 35

if (nilaiUjian > 80) :
    if (keaktifanKelas > 80) :
        print("Nilai bagus dan aktif di kelas.")
    else :
        print("Nilai bagus tapi tidak aktif di kelas.")
elif (nilaiUjian < 50) :
    if (keaktifanKelas > 80) :
        print("Nilai tidak bagus tapi aktif di kelas.")
    else :
        print("Nilai tidak bagus dan tidak aktif di kelas.")
else :
    if (keaktifanKelas > 80) :
        print("Nilai cukup bagus dan aktif di kelas.")
    else :
        print("Nilai cukup bagus tapi tidak aktif di kelas.")
