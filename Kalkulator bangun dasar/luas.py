def luas_lingkaran():
    print("Menghitung Luas Lingkaran")
    jari = int(input("Masukkan jari - jari = "))
    luas = 22/7 * jari * jari
    print ("Luas = ",luas)

def persegi():
    print("Menghitung Luas Persegi")
    sisi = int(input("Masukkan Sisi = "))
    luas = sisi * sisi
    print    ("Luas = ",luas)

def segitiga():
    print("Menghitung Luas Segitiga")
    alas = int(input("Masukkan Alas = "))
    tinggi = int(input("Masukkan Tinggi"))
    luas = 1/2 * alas * tinggi
    print("Luas = ",luas)

def segsiku():
    print("Menghitung Luas Segitiga Siku - siku")
    alas = int(input("Masukkan alas = "))
    tinggi = int(input("Masukkan tinggi"))
    luas = 1/2 * alas * tinggi
    print("Luas = ",luas)

def fibonaci():
    for i in range(10):
        print(('*' * (1 + 2 * i)).center(1 + 2 * 10))


print("1. Menghitung Luas Lingkaran")
print("2. Menghitung Luas Persegi")
print("3. Menghitung Luas Segitiga")
print("4. Menghitung Luas segitiga siku-siku")
print("5. Segitiga Fibonaci")

pilihan = int(input("Silahkan pilih : "))
if pilihan == 1:
    luas_lingkaran()
elif pilihan == 2:
    persegi()
elif pilihan == 3:
    segitiga()
elif pilihan == 4:
    segsiku()
elif pilihan == 5:
    fibonaci()
else :
    print("Pilihan salah")



