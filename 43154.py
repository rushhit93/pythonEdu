sayi = int(input("Asal Sayı: "))
x=0
i: int
if (sayi == 0):
    print("Sayı Sıfırdır")
elif (sayi<=1):
    print("Sayı 1 veya 1'den küçüktür.")
elif (sayi>1) :

    for i in range(2, sayi , 1):
        mod = sayi % i
        if (mod == 0):
            x=x+1
    if (x >= 1):
        print("asal değildir")
    else :
        print("asaldır")