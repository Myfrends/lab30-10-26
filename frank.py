# hari pertama
hari_pertama = {"keju", "tepung", "garam", "gula", "coklat"}

# hari kedua
hari_kedua = {"garam", "gula", "coklat", "kecap"}

#hari kedua
hari_kedua.add("keju")

# menampilkan hasil
print("belanja hari pertama", hari_pertama)
print("belanja hari kedua", hari_kedua)

barang_sama = hari_pertama.intersection(hari_kedua)
print ("barang yang ada di kedua hari:", barang_sama)
barang_berbeda = hari_pertama.difference(hari_kedua)

print("barang yang hanya ada di hari pertama:", barang_berbeda)

hari_pertama.remove ("garam")
print("hari pertama", hari_pertama)
print("hari kedua", hari_kedua)

barang_berbeda = hari_kedua.difference(hari_pertama)

print("barang yang hanya dibeli di hari kedua", barang_berbeda)

barang_berbeda = hari_kedua.symmetric_difference(hari_pertama)

print("barang yang tidak ada di kedua hari", barang_berbeda)

print("semua keperluan rumah tangga hari pertama:", hari_pertama)

print("semua keperluan rumah tangga hari kedua:", hari_kedua)