from turtle import *

home()
shape("turtle")
pencolor("gray")
penup()
goto(-200,200)
pendown()

def triangulo(i = 0):
    #Izquierda
    left(60)
    forward(40)
    left(60)
    forward(40)
    right(120)
    forward(40)

    #Arriba
    left(60)
    forward(40)
    right(120)
    forward(40)
    left(60)
    forward(40)

    #Derecha
    right(120)
    forward(40)
    left(60)
    forward(40)

    i += 1
    
    if i < 6:
        triangulo(i)

triangulo()