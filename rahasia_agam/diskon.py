total = int(input("Masukkan Nilai :"))
bayar = total
if total > 1100000:
    print("Anda mendapat diskon 10%")

    diskon = total * 10/100
    bayar = total - diskon

    print("Total Bayar : ",bayar)

else:
    print ("total belanjaan anda : ",total)