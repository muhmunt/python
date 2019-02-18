bindo = int(input("Indonesia = "))
mtk = int(input("Matematika = "))
inggris = int(input("Inggris = "))
produktif = int(input("Produktif = "))
print("A.SangatBaik")
print("B.Baik")
print("C.Cukup")
print("D.Buruk")
sikap=(input("Pilih Sikap = "))
if(bindo and mtk and inggris and produktif>=75 and sikap=="A"or sikap=="B"):
        print("LULUS")
else:
    print("Tidak LULUS")