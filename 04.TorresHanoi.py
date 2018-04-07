import os
import random

def limpiar():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    else:
        print("No se puede limpiar la pantalla")

movimientos = 0
discos = 3 #Por defecto se usarán tres discos
#Son tres torres, cada una tiene una cantidad de discos asignada
torres = [
    ["Uno", discos],
    ["Dos", 0],
    ["Tres", 0]
]
#Arreglo que contendrá los discos según torre
discosTorres = [
    [
        torres[0][0],
        []
    ],
    [
        torres[1][0],
        []
    ],
    [
        torres[2][0],
        []
    ]
]

#Asignar la cantidad de discos en la torre 1
for i in range(discos):
    discosTorres[0][1] += [i + 1]

def mostrarInfo():
    # limpiar()
    for i in range(len(torres)):
        print("Torre", torres[i][0])
        for x in range(len(discosTorres[i][1])):
            num = discosTorres[i][1][x]
            if num == 1:
                print("                   XX")
            elif num == 2:
                print("                 XXXXXX")
            elif num == 3:
                print("               XXXXXXXXXX")
        print("   ----------------------------------\n")
    print("========================================")

def moverDisco(origen, destino):
    valid = True #Para verificar si el movimiento es válido
    global movimientos
    origen -= 1
    destino -= 1
    cantOrigen = torres[origen][1] #Para verificar si hay discos en la torre de origen
    if cantOrigen == 0 or (origen < 0 or origen > 2 or destino < 0 or destino > 2):
        valid = False
    else:
        cantDestino = torres[destino][1] #Para verificar si hay discos en la torre de destino
        tamOrigen = discosTorres[origen][1][0]
        if cantDestino > 0:
            tamDestino = discosTorres[destino][1][0]
            if tamOrigen > tamDestino:
                valid = False
        if valid:
            if origen != destino:
                movimientos += 1
                torres[origen][1] = cantOrigen - 1
                discoMovido = discosTorres[origen][1].pop(0)

                torres[destino][1] = cantDestino + 1
                discosTorres[destino][1].append(discoMovido)
                discosTorres[destino][1].sort() #Ordena los discos según tamaño
            mostrarInfo()
        else:
            print("Movimiento inválido")


mostrarInfo()

def resolver():
    moverDisco(1, 3)
    moverDisco(1, 2)
    moverDisco(3, 2)
    moverDisco(1, 3)
    moverDisco(2, 1)
    moverDisco(2, 3)
    moverDisco(1, 3)
    
def jugar():
    while torres[2][1] < 3:
        origen = int(input("Origen\n"))
        destino = int(input("Destino\n"))
        moverDisco(origen, destino)

resolver()
# jugar()
print("¡Juego finalizado en", movimientos, "movimientos!")