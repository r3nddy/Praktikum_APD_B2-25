# nilai =  input(int("Masukkan nilai : "))

# if nilai >= 80:
#     print("A")
# elif nilai >= 70:
#     print("B")
# elif nilai >= 60:
#     print("C")
# else:
#     print("Tidak lulus")

# Menggunakan Ternary Operator
# nilai = 70
# status = "Lulus" if nilai >= 60 else "Tidak Lulus"
# print(status)

# 2. Niffari baru saja membuka sebuah toko pakaian dan memberikan diskon 'Grand
# Opening' dengan ketentuan; Jika total belanja lebih dari Rp.100.000,00 mendapat diskon
# 20%, jika total belanja lebih dari Rp.50.000,00 diskon 10%, kurang dari ketentuan di atas
# pembeli tidak mendapatkan diskon dan tidak berlaku kelipatan. Terapkan IF/ELIF/ELSE ke
# dalam kasus di atas!

total_belanja = int(input("Masukkan angka : "))

if total_belanja > 100000:
    diskon = 0.2
elif total_belanja > 50000:
    diskon10 = 0.1
harga_akhir = total_belanja - (total_belanja * diskon)

print(f"total bayar anda setelah diskon {harga_akhir}")

