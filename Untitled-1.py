rahasia=10
i= int(input(" masukan angka tebakan :"))
while i != rahasia:
    print("tebakan salah")
    if i<rahasia:
        print("angka terlalu kecil")
    else:
        print("angka terlalu besar")
    i=int(input("masukan angga tebakan:"))
    print("angka tebakan benar")