# program CRUD "Manajemen Listing Properti"
# Nama : Rendy
# NIM : 2509106069

import os
import time
from prettytable import PrettyTable
import pwinput

# (username, password, level_akses)
data_pengguna = [
    ("rendy", "admin123", "admin"),
    ("user1", "user123", "user")
]

# [id, nama, lokasi, tipe listing, harga]
daftar_properti = [
    ["R001", "Krusty Krab", "Bikini Bottom", "Restoran", 5000000],
    ["R002", "Rumah Upin & Ipin", "Kampung Durian Runtuh", "Rumah", 350000],
    ["R003", "Superlab Gustavo Fring", "Albuquerque, New Mexico", "Laboratorium", 12000000]
]

while True:
    os.system("cls || clear")
    print("🏠  SISTEM MANAJEMEN LISTING PROPERTI  🏠.")
    tabel_menu = PrettyTable()
    tabel_menu.field_names = ["No", "🧭 Menu Utama"]
    tabel_menu.align = "l" 
    tabel_menu.hrules = 1
    tabel_menu.add_row(["1", "🔑 Login"])
    tabel_menu.add_row(["2", "📝 Register"])
    tabel_menu.add_row(["3", "🚪 Keluar"])
    print(tabel_menu)

    opsi = input("Pilih Menu : ")

    # Kesempatan Login 3x
    if opsi == "1":
        os.system("cls || clear")
        print("=== LOGIN ===")
        percobaan = 0
        berhasil = False

        while percobaan < 3 and not berhasil:
            username = input("Masukkan Username: ").lower()
            password = pwinput.pwinput(prompt="Masukkan Password: ",mask="*")

            level_akses = None
            for u in data_pengguna:
                if u[0] == username and u[1] == password:
                    level_akses = u[2]
                    break

            if level_akses:  # login berhasil
                berhasil = True
            else:
                percobaan += 1
                sisa = 3 - percobaan
                if sisa > 0:
                    print(f"Username atau password salah! Sisa percobaan: {sisa}")
                else:
                    print("Username atau password salah 3 kali. Silakan tunggu 5 menit sebelum mencoba lagi.")
                    time.sleep(300)

        if berhasil:
            #ADMIN
            if level_akses == "admin":
                while True:
                    os.system("cls || clear")

                    print("=" * 60)
                    print("  MENU ADMIN ".center(60))
                    print("=" * 60)

                    tabel_admin = PrettyTable()
                    tabel_admin.field_names = ["No", "Pilihan Menu"]
                    tabel_admin.align = "l"
                    tabel_admin.hrules = 1
                    tabel_admin.add_row(["1", "Lihat Semua Properti"])
                    tabel_admin.add_row(["2", "Tambah Properti"])
                    tabel_admin.add_row(["3", "Update Properti"])
                    tabel_admin.add_row(["4", "Hapus Properti"])
                    tabel_admin.add_row(["5", "Logout"])
                    
                    print(tabel_admin)

                    opsi_admin = input("Pilih menu: ")

                    # Read
                    if opsi_admin == "1":
                        os.system("cls")
                        print("=== Daftar Properti ===")
                        if len(daftar_properti) == 0:
                            print("Belum ada Properti")
                        else:
                            tabel = PrettyTable()
                            tabel.field_names = ["No", "ID", "Nama", "Lokasi", "Tipe Listing", "Harga (Rp)"]
                            tabel.hrules = 1
                            for i in range(len(daftar_properti)):
                                id, nama, lokasi, tipe_listing, harga = daftar_properti[i]
                                tabel.add_row([i+1, id, nama, lokasi, tipe_listing, f"{harga:,}"])
                            print(tabel)
                        input("\nTekan Enter untuk kembali...")

                    # Create
                    elif opsi_admin == "2":
                        os.system("cls")
                        print("=== TAMBAH PROPERTI ===")
                        id = f"R{len(daftar_properti) + 1:03d}" # otomatis buat id
                        nama = input("Nama Properti: ")
                        lokasi = input("Lokasi: ")
                        tipe_listing = input("Tipe listing: ")
                        harga = input("Harga (angka): ")

                        if harga.isdigit():
                            daftar_properti.append([id, nama, lokasi, tipe_listing, int(harga)])
                            print("Properti berhasil ditambahkan!")
                        else:
                            print("Harga harus berupa angka!")

                        input("Tekan Enter untuk kembali...")

                    # Update
                    elif opsi_admin == "3":
                        os.system("cls || clear")
                        print("=== UPDATE DATA PROPERTI ===")
                        tabel_update = PrettyTable()
                        tabel_update.field_names = ["No", "ID", "Nama Properti", "Lokasi", "Tipe Listing", "Harga (Rp)"]
                        tabel_update.align = "l"
                        tabel_update.hrules = 1

                        for i in range(len(daftar_properti)):
                            id, nama, lokasi, tipe_listing, harga = daftar_properti[i]
                            tabel_update.add_row([i+1, id, nama, lokasi, tipe_listing, f"{harga:,}"])
                        print(tabel_update)

                        pilih = input("Nomor properti yang ingin diupdate: ")

                        if pilih.isdigit() and 1 <= int(pilih) <= len(daftar_properti):
                            id_baru = int(pilih) - 1
                            id, nama_lama, lokasi_lama, tipe_listing_lama, harga_lama = daftar_properti[id_baru]
                            print("Kosongkan jika tidak ingin mengubah.")
                            nama_baru = input(f"Nama baru ({nama_lama}): ")
                            lokasi_baru = input(f"Lokasi baru ({lokasi_lama}): ")
                            tipe_listing_baru = input(f"Tipe listing baru ({tipe_listing_lama}): ")
                            harga_baru = input(f"Harga baru ({harga_lama}): ")

                            if nama_baru != "":
                                daftar_properti[id_baru][1] = nama_baru
                            if lokasi_baru != "":
                                daftar_properti[id_baru][2] = lokasi_baru
                            if tipe_listing_baru != "":
                                daftar_properti[id_baru][3] = tipe_listing_baru
                            if harga_baru != "":
                                if harga_baru.isdigit():
                                    daftar_properti[id_baru][4] = int(harga_baru)
                                else:
                                    print("Harga harus angka, tidak diubah.")
                            print("Data berhasil diperbarui.")
                        else:
                            print("Nomor tidak valid!")
                        input("Tekan Enter untuk kembali...")

                    # Delete
                    elif opsi_admin == "4":
                        os.system("cls")
                        print("=== HAPUS PROPERTI ===")
                        tabel_hapus = PrettyTable()
                        tabel_hapus.field_names = ["No", "ID", "Nama Properti", "Lokasi", "Tipe Listing", "Harga (Rp)"]
                        tabel_hapus.align = "l"
                        tabel_hapus.hrules = 1

                        for i in range(len(daftar_properti)):
                            id, nama, lokasi, tipe_listing, harga = daftar_properti[i]
                            tabel_hapus.add_row([i+1, id, nama, lokasi, tipe_listing, f"{harga:,}"])
                        print(tabel_hapus)

                        pilih = input("Nomor properti yang ingin dihapus: ")

                        if pilih.isdigit() and 1 <= int(pilih) <= len(daftar_properti):
                            del daftar_properti[int(pilih)-1]
                            print("Data berhasil dihapus.")
                        else:
                            print("Nomor tidak valid!")
                        input("Tekan Enter untuk kembali...")

                    # Logout
                    elif opsi_admin == "5":
                        break
                    else:
                        print("Pilihan tidak valid!")
                        input("Tekan Enter untuk lanjut...")

            # USER
            elif level_akses == "user":
                while True:
                    os.system("cls")
                    print("=== MENU USER ===")

                    tabel_user = PrettyTable()
                    tabel_user.field_names = ["No", "Pilihan Menu"]
                    tabel_user.align = "l"
                    tabel_user.hrules = 1

                    tabel_user.add_row(["1", "Lihat Semua Properti"])
                    tabel_user.add_row(["2", "Logout"])
                    print(tabel_user)

                    pilih_user = input("Pilih menu: ")

                    if pilih_user == "1":
                        os.system("cls")
                        print("=== DAFTAR PROPERTI ===")
                        if len(daftar_properti) == 0:
                            print("Belum ada properti.")
                        else:
                            tabel_user_properti = PrettyTable()
                            tabel_user_properti.field_names = ["No", "ID", "Nama Properti", "Lokasi", "Tipe Listing", "Harga (Rp)"]
                            tabel_user_properti.align = "l"
                            tabel_user_properti.hrules = 1

                            for i in range(len(daftar_properti)):
                                id, nama, lokasi, tipe_listing, harga = daftar_properti[i]
                                tabel_user_properti.add_row([i+1, id, nama, lokasi, tipe_listing, f"{harga:,}"])
                            print(tabel_user_properti)
                        input("\nTekan Enter untuk kembali...")

                    elif pilih_user == "2":  
                        break

    # Register
    elif opsi == "2":
        os.system("cls")
        print("=== REGISTER PENGGUNA BARU ===")
        username = input("Masukkan username: ")
        password = pwinput.pwinput(prompt="Masukkan Password: ",mask="*")

        sudah_ada = False
        for u in data_pengguna:
            if u[0] == username:
                sudah_ada = True
                break

        if sudah_ada:
            print("Username sudah digunakan!")
        else:
            data_pengguna.append((username, password, "user"))
            print("Registrasi berhasil! Silakan login.")
        input("Tekan Enter untuk lanjut...")

    # keluar program
    elif opsi == "3":
        print("Terima kasih telah menggunakan Program ini!")
        break
    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk lanjut...")
