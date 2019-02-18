print("1.Mobil")
print("2.Motor")
m=(input("Jenis Kendaraan ="))
n=int (input("Lama Waktu ="))
if(m=="a"):
    total=2000+(n*500)
    print("Total = ",total)
else:
    total=1000+(n*300)
    print("Total = ", total)