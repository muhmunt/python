gaji = 10000000
berkeluarga = True
punya_rumah = True

if gaji > 3000000:
    print ("Gaji sudah diatas UMR")
    if berkeluarga:
        print("Wajib ikutan asuransi dan menabung untuk pensiun")
    else :
        print("Tidak perlu ikutan asuransi")

    if punya_rumah:
        print("Wajib bayar pajak rumah")
    else:
        print("Tidak wajib bayar pajak rumah")
else:
    print("Gaji sebelum UMR")