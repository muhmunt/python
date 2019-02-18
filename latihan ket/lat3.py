def batas():
    print("==========================================")
batas();
print("APLIKASI LAUNDRY KILOAN")
print("\nKODE LAUNDRY\t JENIS LAUNDRY\tTARIF/KILO")
print("\t\t\t1\t\tPAKAIAN\t\t\t10.000")
print("\t\t\t2\t\tSELIMUT\t\t\t20.000")
print("\t\t\t3\t\tKARPET\t\t\t30.000")
batas();

pl = int(input("Masukkan Kode Laundry = "))
batas();
if(pl == 1):
    jenis = "PAKAIAN"
    tarif = 10000
    total = 10000
elif(pl == 2):
    jenis = "SELIMUT"
    tarif = 20000
    total = 20000
elif(pl == 3):
    jenis = "KARPET"
    tarif = 30000
    total = 30000

print("Jenis Laundry= ",jenis)
print("Tarif = ",tarif)
batas();
kl = int(input("Berapa kilo anda mencuci = "))
batas();
print("TAMBAHAN")
print("\nKODE TAMBAHAN\t TAMBAHAN\tTARIF/KILO")
print("\t\t\t1\t\tGOSOK\t\t\t30.000")
print("\t\t\t2\t\tGOSOK WANGI\t\t40.000")
batas();
tbh = int(input("Masukkan kode tambahan = "))

if(tbh == 1):
    jenis = "GOSOK"
    tarif = 30000
    total2 = 30000
elif(tbh == 2):
    jenis = "GOSOK WANGI"
    tarif = 40000
    total2 = 40000
tots = total2 * kl
print("TAMBAHAN = ",jenis)
print("TARIF = ",tarif)
batas();
akhir = total*kl + tots
print("TOTAL = ",akhir)
batas();
byr = int(input("BAYAR = "))
kembalian = byr - akhir
print("Kembalian = ",kembalian)