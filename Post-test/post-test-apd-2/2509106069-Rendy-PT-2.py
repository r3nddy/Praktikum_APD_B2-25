nama = input("Nama : ")
nim = int(input("NIM : "))

harga = int(input("Masukkan harga: "))

pecel_lele = float(harga + (harga * 5 / 100))
mie_ayam   = float(harga + (harga * 8 / 100))
nasi_padang = float(harga + (harga * 10 / 100))


print()
print("=== Selamat Datang Di Warung makan ===")
print(f"No  Menu          Harga     Pajak  Total")
print("------------------------------------------")
print(f"{1}  Pecel Lele     Rp{harga}   5%     Rp{(pecel_lele)}")
print(f"{2}  Mie Ayam       Rp{harga}   8%     Rp{(mie_ayam)}")
print(f"{3}  Nasi Padang    Rp{harga}   10%    Rp{(nasi_padang)}")

print("\n")
print(f"{nama} dengan NIM : {nim} ingin membeli Pecel Lele maka ia harus membayar Rp.{pecel_lele} (sudah termasuk pajak)")
print(f"{nama} dengan NIM : {nim} ingin membeli Mie Ayam maka ia harus membayar Rp.{mie_ayam} (sudah termasuk pajak)")
print(f"{nama} dengan NIM : {nim} ingin membeli Nasi Padang maka ia harus membayar Rp.{nasi_padang} (sudah termasuk pajak)")
print("\n")