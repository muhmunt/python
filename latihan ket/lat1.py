print("APLIKASI WARNET")
print("\nKODE PELANGGAN\t JENIS PELANGGAN\tTARIF JAM PERTAMA\t TARIF BERIKUTNYA")
print("\t\t\t1\t\tMEMBER\t\t\t\t3000\t\t\t2000")
print("\t\t\t2\t\tNON MEMBER\t\t\t4000\t\t\t3000")
pl = int(input("Masukkan Kode Pelanggan = "))

if(pl == 1):
   jenis = "MEMBER"
   first = 3000
   nxt = 2000
elif(pl == 2):
   jenis = "NON MEMBER"
   first = 4000
   nxt = 3000

print("Jenis = ",jenis)
print("Tarif Jam Pertama = ",first)
print("Tarif Jam Berikutnya = ",nxt)
jam = int(input("\nBerapa Lama Anda Sewa = "))

if (pl == 1 and jam == 1 ):
 total = 3000
elif(pl == 2 and jam == 1):
 total = 4000
elif(pl == 1 and jam > 1):
 total = 3000+(jam - 1)*2000
elif(pl == 2 and jam > 1):
 total = 4000+(jam - 1)*3000

print("Total = ",total)

byr = int(input("Bayar = "))
kembalian = byr - total
print("Kembalian = ",kembalian)