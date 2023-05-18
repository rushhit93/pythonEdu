
# Girilen ABC... gibi n digit string için A+B+C+... şeklinde hesaplanması.
# örn: 123 sayısı için 6 dönmeli

# 1-1000 arasında basamaklarının sayı değerleri toplamı o sayıya tam bölünebilen sayıları listeleyiniz.
# örn: 123/6=20,5 NOK
# 126/9=14 OK
def n_digit_sum (val):
    i: int
    valSum=0
    liste = list(map(int, str(val)))

    for i in range(0, len(str(val)), 1):
        valSum = valSum + int(liste[i])
        # val = list(map(int, str(i)))
        # valSum = sum(val)
    print (valSum)
    return

def ebob_sum():
    i: int
    for i in range(1, 1000, 1):
        res = list(map(int, str(i)))
        Sum = sum(res)
        a = i / Sum
        a = str(a)
        foo = a.rsplit('.')
        a = int(foo[1])
        if (a > 0):
            print('%s this number %d ' % ('OK', i))
        else:
            print('%s this number %d ' % ('NOK', i))

def ebob_sum_second():
    i: int
    for i in range(1, 1000, 1):
        res = list(map(int, str(i)))
        Sum = sum(res)
        a = i % Sum
        if (a == 0):
            print('%s this number %d ' % ('OK', i))
        else:
            print('%s this number %d ' % ('NOK', i))

n_digit_sum(int(input("Sayi Girin : ")))
#ebob_sum()
ebob_sum_second()


