nama: str = "Rendy"
umur: int  = 18 
print(f"Halo nama saya {nama}")

print(f"""
baris 1
baris 2
baris 3
baris 4
""")

print(f"""Halo nama saya : {nama} 
umur saya : {umur}""")


# daftar = []

# while True:

#     x = str(input("Masukkan elemen : "))
#     daftar.append(x)
#     print(daftar)

#     if x == "0":
#         break

pemakaian = int(input("Masukkan jumlah pemakaian listrik (kWh) : "))
tarif = 1200
total_biaya = pemakaian * tarif
print(f"total tagihan : Rp {total_biaya}")