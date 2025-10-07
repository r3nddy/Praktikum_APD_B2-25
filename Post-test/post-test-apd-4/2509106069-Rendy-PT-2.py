print("=" * 50)
print("==== Selamat Datang Di Toko Furnitur Infordeh ====")
print("=" * 50)

username_saya = "Rendy"
password_saya = "2509106069"

validasi = False

for percobaan in range(3):
    sisa_percobaan = 2 - percobaan

    print(f"\nPercobaan login ke-{percobaan + 1}")
    print(f"Sisa percobaan: {sisa_percobaan}")
    username = input("Masukkan Username Anda : ")
    password = input("Masukkan Password Anda : ")

    if username == username_saya and password == password_saya:
        validasi = True
        print(f"\nHalo, {username_saya} selamat datang di Toko Furnitur Infordeh")
        break
    else:
        print("Login gagal! Username atau Password Salah")

        if percobaan == 2:
            print("Anda gagal login 3 kali.Akun Anda terblokir")
            break
        else:
            print(f"Anda masih memiliki {sisa_percobaan} percobaan lagi")

if validasi:
    total_bayar = 0
    daftar_beli = ""
    jumlah_barang = 0
    nama_pembeli = username_saya

    while True:
        print("\n" + "=" * 50)
        print("             DAFTAR PRODUK ")
        print("=" * 50)
        print("| No |       Nama Barang       |   Harga/Unit   |")
        print("|----|-------------------------|----------------|")
        print("| 1  | Sofa                    | Rp 500,000     |")
        print("| 2  | Meja Belajar            | Rp 250,000     |")
        print("| 3  | Rak Lemari              | Rp 150,000     |")
        print("| 4  | Keluar / Selesai        |                |")
        print("=" * 50)

        pilihan = int(input("pilih opsi (1-4): "))

        if pilihan == 1:
            barang = "sofa"
            harga = 500000
        elif pilihan == 2:
            barang = "meja belajar"
            harga = 250000
        elif pilihan == 3:
            barang = "rak lemari"
            harga = 150000
        elif pilihan == 4:
            print("\nSelesai berbelanja.")
            break
        else:
            print("Pilihan tidak valid!, Silahkan pilih 1-4.")
            continue

        while True:
            jumlah_input = input(f"Masukkan jumlah {barang} yang ingin dibeli: ")

            if not jumlah_input.isdigit():
                print("jumlah barang berupa angka")
                continue

            jumlah = int(jumlah_input)

            if jumlah <= 0:
                print("Jumlah barang harus lebih dari 0")
                continue
            else:
                break

        # Hitung total untuk barang
        total_barang = 0
        print(f"Perhitungan {barang}")
        for i in range (jumlah):
            total_barang += harga
            print(f"unit {i+1}: Rp {harga:,} -> Subtotal: Rp {total_barang:,}")

        # menyimpan data pembelian
        daftar_beli += f"{barang:15} x {jumlah:2} unit = Rp {total_barang:,}\n"
        total_bayar += total_barang
        jumlah_barang += 1

        print(f"{barang} berhasil ditambahkan ke keranjang!")
        print(f"Total sementara: Rp {total_bayar:,}")

    # perhitungan diskon dan bonus
    if jumlah_barang > 0:
        diskon = 0
        bonus = "-"
        total_sesudah_diskon = total_bayar

        if total_bayar >= 700000:
            diskon = total_bayar * 0.2
            total_sesudah_diskon = total_bayar - diskon
        elif total_bayar >= 500000:
            diskon = total_bayar * 0.08
            total_sesudah_diskon = total_bayar - diskon
        elif total_bayar >= 150000:
            bonus = "Kitchen Set"

        # tampilan struk
        print("\n" + "=" * 50)
        print("  STRUK PEMBELIAN TOKO FURNITUR INFORDEH  ")
        print("=" * 50)
        print(f"Nama Pembeli : {nama_pembeli}")
        print(f"Total Barang : {jumlah_barang} unit")
        print("-" * 50)
        print("| Nama Barang     | Jumlah |     Total Harga |")
        print("|-----------------|--------|-----------------|")
        print(daftar_beli, end="")
        print("-" * 50)
        print(f"SUB TOTAL         : Rp {total_bayar:,.0f}")

        if diskon > 0:
            if total_bayar >= 700000:
                print(f"Diskon (20%)   : Rp {diskon:,.0f}")
            else:
                print(f"diskon (8%)    : Rp {diskon:,.0f}")

        if bonus != "-":
            print(f"Bonus     : {bonus}")

        print(f"Total Bayar   : {total_sesudah_diskon:,.0f}")