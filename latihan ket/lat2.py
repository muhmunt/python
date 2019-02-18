def batas():
    print("==========================================")
batas();
print("APLIKASI CUCI MOTOR DAN MOBIL")
print("\nKODE KENDARAAN\t JENIS KENDARAAN\tTARIF")
print("\t\t\t1\t\tMOTOR\t\t\t10.000")
print("\t\t\t2\t\tMOBIL\t\t\t20.000")
print("\t\t\t3\t\tTRUCK\t\t\t30.000")
batas();

pl = int(input("Masukkan Kode Kendaraan = "))

if(pl == 1):
    jenis = "MOTOR"
    tarif = 10000
    total = 10000
elif(pl == 2):
    jenis = "MOBIL"
    tarif = 20000
    total = 20000
elif(pl == 3):
    jenis = "TRUCK"
    tarif = 30000
    total = 30000


batas();
print("Jenis Kendaraan= ",jenis)
print("Tarif = ",tarif)
batas();
print("Total = ",total)
batas();
byr = int(input("Bayar = "))
batas();
kembalian = byr - total
print("kembalian = ",kembalian)
batas();