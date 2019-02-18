def batas():
    print("==========================================")
batas();
print("APLIKASI PENGHITUNG BERAT BADAN DEWASA")
brt = int(input("MASUKKAN BERAT BADAN ANDA = "))

if( brt < 80 ):
  ket = "IDEAL"
elif(brt<125):
    ket = "GEMUK"
elif(brt<150):
    ket="OBESITAS"
elif(brt>=150):
    ket = "BERAT BADAN BERLEBIH"
batas();
print("KETERANGAN = ",ket)
