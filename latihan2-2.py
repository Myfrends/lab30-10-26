import math

print("=== PROGRAM LINGKARAN ===")
print("1. Menghitung Keliling Lingkaran")
print("2. Menghitung Luas Lingkaran")

pilihan = int(input("Masukkan pilihan (1/2): "))
r = float(input("Masukkan jari-jari lingkaran: "))

if pilihan == 1:
    keliling = 2 * math.pi * r
    print("Keliling Lingkaran =", keliling)

elif pilihan == 2:
    luas = math.pi * r * r
    print("Luas Lingkaran =", luas)

else:
    print("Pilihan tidak tersedia!")