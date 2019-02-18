diskon = 0
qty = int(input("Banyak barang?"))
harga = int(input("Harga barang?"))

jumlah = qty * harga

if jumlah > 100000:
    diskon = jumlah*0.1
    bayar = jumlah - diskon

    print("-------------------------------")
    print("Anda berhak mendapat  diskon =Rp. ",diskon,"(10% dari total harga)")
    print("Total bayar = Rp. ",bayar)

else:
    nodiskon = jumlah-0
    print("Total bayar,",nodiskon)
    print("Anda tidak mendapatkan diskon")