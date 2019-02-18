print("a=sabun  rp.1000")
print("b=shampo rp.2000")
print("c=gayung rp.3000")
print("d=ember  rp.4000")
print("e=baskom rp.5000")
i=(input("Barang Yang Dibeli : "))
j=int(input("Jumlah :"))
if(i=="a"):
    h=1000;
elif(i=="b"):
    h=2000;
elif(i=="c"):
    h=3000;
elif(i=="d"):
    h=4000;
elif(i=="e"):
    h=5000;
tot=j*h
print("Total Belanja =",tot)
b=int(input("Bayar = "))
c=b-tot
print("Kembali =",c)