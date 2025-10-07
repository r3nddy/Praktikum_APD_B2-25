# ulangi = 10
# for i in range (ulangi):
#     print(f'Perulangan ke {i}')

# angka = [2, 5, 8, 12, 15, 7, 20]

# print("Mencari angka pertama yang lebih besar dari 10...")

# for n in angka:
#     print(f"Sekarang memeriksa angka: {n}")
#     if n > 10:
#         print(f"Angka {n} lebih besar dari 10, Perulangan berhenti.")
#         break
# print("Program selesai.")


# for i in range(1, 10):
#     for j in range(1, 10):
#         print("*", end=" ")
#     print("")

jawab = 'ya'
hitung = 0
while(jawab == 'ya'):
    hitung += 1
    jawab = input("Ulang lagi? ")
print(f"Total perulangan: {hitung}")