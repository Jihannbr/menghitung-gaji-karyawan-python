#Program Gaji Karyawan.py
#menampilkan pilihan golongan
print("Program Gaji Mingguan Karyawan")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Anda termasuk golongan mana?")
print("  Golongan -> 1")
print("  Golongan -> 2")
print("  Golongan -> 3")
print("  Golongan -> 4")
#input golongan dan jam kerja
gol = int(input("Masukkan Golongan Anda = "))
jamkerja = int(input("Jumlah Jam Kerja = "))

#gaji berdasarkan golongan
if gol == 1:
    upah = 3000
elif gol == 2:
    upah = 3500
elif gol == 3:
    upah = 4000
else:
    upah = 4500
    
#jam kerja
if jamkerja <= 40:
    gaji = jamkerja * upah
else:
    gaji = (40 * upah) + ((jamkerja - 40) * 1.5 * upah)

#output gaji mingguan yang diterima
print("Gaji Mingguan yang Anda terima sebesar Rp", gaji)
