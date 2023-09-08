# KALKULATOR SEDERHANA

def penambahan(aba, baa):
    return aba + baa, "+"

def perkalian(aba, baa):
    return aba * baa, "*"

def pembagian(aba, baa):
    if baa != 0:
        return aba / baa, "/"
    else:
        return "Tidak dapat melakukan pembagian oleh nol"

def pemangkatan(aba, baa):
    return aba ** baa, "^"

# aab ==> Untuk Pilihan Operasi Yang Akan Dilakukan
# abb ==> Untuk Input Nilai 1
# bba ==> Untuk Input Nilai 2
# bbb ==> Untuk Hasil
# abc ==> Untuk Tanda Operator
while True:
    print("Selamat Datang di Kalkulator Sederhana\nAnda Dapat Memilih berbagai macam pilihan operasi dibawah ini.")
    print("Pilih operasi:")
    print("1. Penambahan")
    print("2. Perkalian")
    print("3. Pembagian")
    print("4. Pemangkatan")
    print("5. Keluar")

    aab = input("Operator Yang Anda Pilih: ")
    
    if aab == "5":
        print("Program berhenti dan anda keluar")
        break

    if aab not in ["1", "2", "3", "4"]:
        print("Menu yang anda pilih tidak tersedia")
        continue

    abb = int(input("Masukkan angka pertama: "))
    bba = int(input("Masukkan angka kedua: "))
    
    if aab == "1":
        bbb, abc = penambahan(abb, bba)
    elif aab == "2":
        bbb, abc = perkalian(abb, bba)
    elif aab == "3":
        bbb, abc = pembagian(abb, bba)
    elif aab == "4":
        bbb, abc = pemangkatan(abb, bba)


    print(f"Hasil {abb} {abc} {bba} adalah: {bbb}")