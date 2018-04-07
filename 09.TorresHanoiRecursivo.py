import os
import random

def limpiar():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    else:
        print("No se puede limpiar la pantalla")

cantDiscos = 0
movimientos = 0
torresDiscos = [
    [
        "Uno",
        []
    ],
    [
        "Dos",
        []
    ],
    [
        "Tres",
        []
    ]
]

def datos():
    global cantDiscos
    cantDiscos = int(input("¿Cuántos discos desea usar? [1-8]\n"))
    if cantDiscos > 0 and cantDiscos <= 8:
        for i in range(cantDiscos):
            torresDiscos[0][1].append(i + 1)
    else:
        print("Cantidad ingresada no válida. Vuelva a intentarlo")
        datos()
    
def mostrarInfo():
    # limpiar()
    for i in range(len(torresDiscos)):
        print("Torre", torresDiscos[i][0])
        for x in range(len(torresDiscos[i][1])):
            num = torresDiscos[i][1][x]
            if num == 1:
                print("                 XX")
            elif num == 2:
                print("               XXXXXX")
            elif num == 3:
                print("             XXXXXXXXXX")
            elif num == 4:
                print("           XXXXXXXXXXXXXX")
            elif num == 5:
                print("         XXXXXXXXXXXXXXXXXX")
            elif num == 6:
                print("       XXXXXXXXXXXXXXXXXXXXXX")
            elif num == 7:
                print("     XXXXXXXXXXXXXXXXXXXXXXXXXX")
            elif num == 8:
                print("   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("   ----------------------------------\n")
    print("========================================")

def resolver(altura, origen, destino, intermedio):
    if altura >= 1:
        resolver(altura-1,origen,intermedio,destino)
        moverDisco(origen,destino)
        resolver(altura-1,intermedio,destino,origen)

def moverDisco(desde, hacia):
    global movimientos
    movimientos += 1
    print("Movimiento", movimientos)
    # print("mover disco de",desde,"a",hacia)
    torresDiscos[hacia][1].append(torresDiscos[desde][1].pop(0))
    torresDiscos[hacia][1].sort()
    mostrarInfo()


datos()
o, a, d = 0, 1, 2
resolver(cantDiscos, o, d, a)
