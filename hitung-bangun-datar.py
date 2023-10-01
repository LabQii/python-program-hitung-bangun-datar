print("==================================")
print("NAMA : MUHAMMAD IQBAL FIRMANSYAH")
print("NIM  : 210441100084")
print("------UAS ALPRO KELAS B--------")
print("==================================")

def persegi():
    while True:
        try:
            s = int(input("Masukan Sisi : "))
        except ValueError:
            print("Input Tidak Valid ")
            continue
        else:
            luas = s * s
            keliling = 4 * s
            hasil = [luas, keliling]
        break
    return

def persegipanjang():
    while True:
        try:
            p = int(input("Masukkan Panjang : "))
            l = int(input("Masukkan Lebar : "))
        except ValueError:
            print("input tidak valid")
            continue
        else:
            luas = p * l
            keliling = 2 * (p + l)
            hasil = [luas, keliling]
        break
    return hasil

def segitiga():
    while True:
        try:
            a = int(input("Masukan alas : "))
            t = int(input("Masukan Tinggi :"))
        except ValueError:
            print("Input Tidak Valid")
            continue
        else:
            luas = 0.5 * a * t
            keliling = a + t + t
            hasil = [luas, keliling]
        break
    return hasil

def lingkaran():
    while True:
        try:
            r = int(input("Masukan Jari-Jari : "))
        except ValueError:
            print("Input Tidak valid")
            continue
        else:
            if r % 7 == 0:
                luas = 22 / 7 * r * r
                keliling = 2 * (22 / 7 * r)
                hasil = [luas, keliling]
            else:
                luas = 3.14 * r * r
                keliling = 2 * 3.14 * r
                hasil = [luas, keliling]
        break
    return hasil

def jajargenjang():
    while True:
        try:
            a = int(input("Masukan Alas : "))
            t = int(input("Masukan Tinggi : "))
        except ValueError:
            print("Input Tidak Valid")
            continue
        else:
            luas = a * t
            keliling = 2 * (a + t)
            hasil = [luas, keliling]
        break
    return hasil

def trapesium():
    while True:
        try:
            a = int(input("Masukan Sisi 1 : "))
            b = int(input("Masukkan Sisi 2 :"))
            t = int(input("Masukan Tinggi : "))
        except ValueError:
            print("Input Tidak Valid")
            continue
        else:
            luas = 1/2 * t (a+b)
            c = int(input("Masukkan Sisi 3 :"))
            d = int(input("Masukkan sisi 4 : "))
            keliling = a+b+c+d
            hasil = [luas,keliling]
        break
    return hasil

def belahketupat():
    while True:
        try:
            d1 = int(input("Masukan diagonal 1 : "))
            d2 = int(input("Masukan diagonal 2 : "))
        except ValueError:
            print("Input Tidak Valid")
            continue
        else:
            luas = 1/2 * d1*d2
            s = int(input("Masukkan Sisi :"))
            keliling = s*4
            hasil = [luas, keliling]
        break
    return hasil

def layang():
    while True:
        try:
            d1 = int(input("Masukan diagonal 1 : "))
            d2 = int(input("Masukan diagonal 2 : "))
        except ValueError:
            print("Input Tidak Valid")
            continue
        else:
            luas = 1/2 * d1*d2
            s = int(input("Masukkan Sisi :"))
            keliling = s*4
            hasil = [luas, keliling]
        break
    return hasil

confirm = "y"
while confirm == "y":

    print("1. Persegi")
    print("2. Persegipanjang")
    print("3. Jajar Genjang")
    print("4. Segitiga")
    print("5. Belah Ketupat")
    print("6. Layang- layang")
    print("7. Trapesium")
    print("8. Lingkaran")
    print("9. Ulangi")
    print("10. Exit")

    pilihan = input("Masukan Nomer Bangun Datar Yang Anda Pilih(1,2,3,4,5) : ")
    if pilihan == "1":
        hasil = persegi()
        print("Luas Pesegi : {}".format(hasil[0]))
        print("Keliling Persegi : {}".format(hasil[1]))
    elif pilihan == "2":
        hasil = persegipanjang()
        print("Luas Persegi Panjang : {}".format(hasil[0]))
        print("Keliling Persegi Panajng : {}".format(hasil[1]))
    elif pilihan == "4":
        hasil = segitiga()
        print("Luas Segitiga : {}".format(hasil[0]))
        print("Keliling Segitiga : {}".format(hasil[1]))
    elif pilihan == "8":
        hasil = lingkaran()
        print("Luas Lingkaran : {}".format(hasil[0]))
        print("Keliling Lingkaran : {}".format(hasil[1]))
    elif pilihan == "3":
        hasil = jajargenjang()
        print("Luas Jajargenjang : {}".format(hasil[0]))
        print("Keliling Jajargenjang : {}".format(hasil[1]))
    elif pilihan == "5":
        hasil = belahketupat()
        print("Luas Belah Ketupat : {}".format(hasil[0]))
        print("Keliling Belah Ketupat : {}".format(hasil[1]))
    elif pilihan == "6":
        hasil = layang()
        print("Luas Layang-layang : {}".format(hasil[0]))
        print("Keliling LAYANG-LAYANG : {}".format(hasil[1]))
    elif pilihan == "7":
        hasil = trapesium()
        print("Luas Trapesium : {}".format(hasil[0]))
        print("Keliling Trapesium : {}".format(hasil[1]))
    elif pilihan == "9":
        continue
    elif pilihan == "10":
        break
    else:
        print("Input Tidak Valid")
    confirm = input("Apakah  Anda Ingin Mencoba Lagi ? (y,t) : ")
    if confirm == "t":
        break
    elif confirm == "y":
        continue
    else:
        print("IKUTI ARAHAN DAN RULES YANG SUDAH DITENTUKAN")
print("THANK YOUU")
