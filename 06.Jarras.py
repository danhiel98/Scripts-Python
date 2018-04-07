import os

def limpiar():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    else:
        print("No se puede limpiar la pantalla")

# El primer valor es la capacidad de la jarra
# Mientras que el segundo es la cantidad de agua que contiene (todo en galones)
jarras = [
    [4, 0],
    [3, 0]
]

def mostrarInfo():
    print("_________\t")
    print("\       |\t", "_________")
    print(" |      |\t", "\       |")
    print(" | ",jarras[0][1],"  |\t", " | ",jarras[1][1],"  |")
    print(" |      |\t", " |      |")
    print("  ------\t", "  ------")

def llenarJarra(jarra):
    print("Llenar la jarra", jarra)
    jarra -= 1
    if jarra < 0 or jarra > (len(jarras) - 1):
        print("Error, la jarra no existe")
    else:
        capacidad = jarras[jarra][0] #La capacidad de la jarra
        jarras[jarra][1] = capacidad #La cantidad que contendrá la jarra será según su capacidad
    mostrarInfo()

def vaciarJarra(jarra):
    print("Vaciar la jarra", jarra)
    jarra -= 1
    if jarra < 0 or jarra > (len(jarras) - 1):
        print("Error, la jarra no existe")
    else:
        jarras[jarra][1] = 0
    mostrarInfo()
    
def moverAgua(jarraOrigen, jarraDestino):
    print("Mover agua desde la jarra", jarraOrigen,"hacia la jarra", jarraDestino)
    jarraOrigen -= 1
    jarraDestino -= 1
    if (jarraOrigen < 0 or jarraOrigen > (len(jarras) - 1)) or (jarraDestino < 0 or jarraDestino > (len(jarras) - 1)):
        print("Error, alguna de las jarras no existe")
    else:
        capacidadOrigen = jarras[jarraOrigen][0]
        cantidadOrigen = jarras[jarraOrigen][1]
        
        capacidadDestino = jarras[jarraDestino][0]
        cantidadDestino = jarras[jarraDestino][1]
        disponibleDestino = capacidadDestino - cantidadDestino

        # print("Está intentndo pasar", cantidadOrigen, "galones de agua a una jarra que tiene una capacidad de ", capacidadDestino, "galones y contiene", cantidadDestino, "galones de agua")
        if cantidadOrigen >= disponibleDestino:
            jarras[jarraDestino][1] += disponibleDestino
            jarras[jarraOrigen][1] -= disponibleDestino
        else:
            jarras[jarraDestino][1] += cantidadOrigen
            jarras[jarraOrigen][1] -= cantidadOrigen
    mostrarInfo()

#Resolverlo automáticamente
def resolver():
    print("Pasos para resolver el problema")
    llenarJarra(1)
    moverAgua(1, 2)
    vaciarJarra(2)
    moverAgua(1, 2)
    llenarJarra(1)
    moverAgua(1, 2)

#Resolverlo manualmente
def jugar():
    while jarras[0][1] != 2:
        limpiar()
        print("OPCIONES:")
        print("1. Llenar una jarra")
        print("2. Vaciar una jarra")
        print("3. Mover el agua hacia otra jarra")
        mostrarInfo()
        opc = int(input("¿Qué desea hacer?\n"))
        if opc == 1:
            x = int(input("Introduzca el número de la jarra que desea llenar: "))
            llenarJarra(x)
        elif opc == 2:
            x = int(input("Introduzca el número de la jarra que desea vaciar: "))
            vaciarJarra(x)
        elif opc == 3:
            x1 = int(input("Introduzca el número de la jarra de origen: "))
            x2 = int(input("Introduzca el número de la jarra de destino: "))
            moverAgua(x1, x2)
        else:
            print("Opción inválida")

resolver()
# jugar()
print("Problema resuelto")