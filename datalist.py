# Latihan List

# list sesuai nomor tempat duduk 
penumpang = ["William", "Kate", "Anderson", "Jame", "Mady"]
print("a. Daftar penumpang awal  :", penumpang)

# Jones di tempat duduk terakhir (nomor 6)
penumpang.append("Jones")
print("b. Setelah Jones ikut     :", penumpang)

# Anderson digantikan Grace
penumpang[penumpang.index("Anderson")] = "Grace"
print("c. Anderson diganti Grace :", penumpang)

# apakah ada penumpang bernama Thompson
ada_thompson = "Thompson" in penumpang
print("d. Ada Thompson?          :", ada_thompson)

# e. Urutkan berdasarkan abjad 
urut_abjad = sorted(penumpang)
print("e. Urutan abjad           :", urut_abjad)
print("   Tempat duduk (asli)    :", penumpang)

# tampilkan seluruh penumpang dengan perulangan
print("f. Penumpang yang tiba di Yogyakarta:")
for nomor, nama in enumerate(penumpang, start=1):
    print(f"   {nomor}. {nama}")

# g. Kereta kembali ke Jakarta, kosongkan list
penumpang.clear()
print("g. Setelah semua turun    :", penumpang)