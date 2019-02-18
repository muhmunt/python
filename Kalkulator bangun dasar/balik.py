def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

s = input("Masukkan kata : ")
print ("dibalik : ",end="")
print (reverse(s))
