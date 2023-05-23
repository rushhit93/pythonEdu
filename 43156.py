import turtle

#üçgenin derecesini hesaplat
#1-10 den küçükse 100 la çarp, 10-50 10,  50 takma
def tringleDraw(a):
    turtle.speed(1)
    turtle.left(53)
    turtle.forward(a)
    turtle.left(90)
    turtle.backward(160)
    turtle.left(37)
    turtle.forward(200)
    turtle.mainloop()
    return
def squareDraw(a):
    turtle.speed(1)
    turtle.forward(a)
    turtle.left(90)
    turtle.backward(a)
    turtle.right(90)
    turtle.backward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.mainloop()
    return
def circleDraw(a):
    turtle.speed(1)
    turtle.circle(a)
    turtle.mainloop()
    return


def drawShape():
    x = input("Kaç kenar gireceksiniz : ")
    if(x.isalpha()):
        print("Lütfen bir sayı girin.")
        return drawShape()
    else:
        x = int(x)
    i: int
    if (x==0):
        a = int(input("Çapı giriniz : "))
        circleDraw(a)
    elif (x==3):
        # for i in range(x):
        a = int(input('%d .deger :' % (x)))
        tringleDraw(a)
    elif(x == 4):
        a = int(input('%d .deger :' % (x)))
        squareDraw(a)
    elif(x>4):
        a = int(input('%d .deger :' % (x)))
        print(a)
    else:
        print("Geometrik şekil oluşturacak bir değer giriniz")
        drawShape()
    return


drawShape()
