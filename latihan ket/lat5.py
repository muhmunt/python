def batas():
    print("============================================")
batas();
print("APLIKASI PERINGATAN BANJIR PINTU AIR CIBALOK")
batas();
print("KODE PERINGATAN\t TINGGI AIR(CM)\tSTATUS")
print("\t\t\t1\t\t400 – 600\t\tBAHAYA ")
print("\t\t\t2\t\t300 – 399\t\tAWAS ")
print("\t\t\t3\t\t200 – 299\t\tWASPADA ")
print("\t\t\t4\t\t100 – 199\t\tSIAGA ")
print("\t\t\t5\t\t50 – 99\t\t\tNORMAL ")
print("\t\t\t6\t\t1 – 49\t\t\tSURUT  ")
batas();
tg = int(input("Masukkan tinggi air = "))
if( tg == 1 ):
  sts = "BAHAYA"
elif(tg == 2):
    sts = "AWAS"
elif(tg == 3):
    sts="WASPADA"
elif(tg == 4):
    sts = "SIAGA"
elif (tg == 5):
    sts = "NORMAL"
elif (tg == 6):
    sts = "SURUT"
print("Status = ",sts)
batas();




