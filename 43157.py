#Girilen değerlerin büyükten küçüğe ve küçükten büyüğe sıralandığı program.

def sorting_bigToSmall():
    i: int
    x: int
    temp = 0
    print ("Girilen değerler arası boşluk bırakın !!!")
    x = input("Büyükten küçüğe sıralanacak değerleri girin : ")
    liste = list(x.rsplit(' '))
    # print(type(liste))
    # print(liste[0])
    #print(len(liste))
    liste_int = list(map(int, liste))
    for y in range (len(liste) -1, 0, -1):
        for i in range(y):
            if liste_int[i] < liste_int[i+1]:
                temp = liste_int[i]
                liste_int[i] = liste_int[i+1]
                liste_int[i+1] = temp

    print(liste_int)
    return
sorting_bigToSmall()