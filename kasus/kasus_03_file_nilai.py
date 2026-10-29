
try:
    with open("nilai.txt", "r", encoding="utf-8") as file:
        isi = file.read()

    if isi == "":
        print("File kosong.")
    else:
        print(isi)

except FileNotFoundError:
    print("File tidak ditemukan.")
