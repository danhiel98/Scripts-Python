import os

def limpiar():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    else:
        print("No se puede limpiar la pantalla")

# Se crea una lista con lo valores a 0 porque no sabemos las capacidades de las jarras
jarras = [
    [0, 0],
    [0, 0]
]

def mostrarInfo():
    if jarraGrande() == 0:
        print("_________\t")
        print("\       |\t", "_________")
        print(" |      |\t", "\       |")
    else:
        print("         \t", "_________")
        print("_________\t", "\       |")
        print("\       |\t", " |      |")
    print(" | ",jarras[0][1],"  |\t", " | ",jarras[1][1],"  |")
    print(" |      |\t", " |      |")
    print("  ------\t", "  ------")
    print("  ",jarras[0][0],"gal\t   ",jarras[1][0],"gal")

# Función que retorna el índice de la jarra más grande
def jarraGrande():
    cap1 = jarras[0][0]
    cap2 = jarras[1][0]
    if cap1 > cap2:
        return 0
    else:
        return 1

tam1 = tam2 = cantFinal = 0

# Función para obtener los datos de las jarras
def datos():
    global tam1, tam2, cantFinal
    if tam1 == 0:
        tam1 = int(input("¿De cuántos galones es la primer jarra?\n"))
        if tam1 <= 0 or tam1 >= 100:
            tam1 = 0
            print("Tamaño de jarra no válido")
            datos()
    if tam2 == 0:
        tam2 = int(input("¿De cuántos galones es la segunda jarra?\n"))
        if tam2 <= 0 or tam2 >= 100 or tam2 == tam1:
            tam2 = 0
            print("Tamaño de jarra no válido")
            datos()
    if cantFinal == 0:
        cantFinal = int(input("¿Cuántos galones de agua deben quedar en la jarra más grande?\n"))
        if (cantFinal > tam1 and cantFinal > tam2) or cantFinal <= 0:
            cantFinal = 0
            print("Cantidad final no válida")
            datos()
    
    valMin = min(tam1, tam2)
    valMax = max(tam1, tam2)
    if (valMax / valMin == 2) and (cantFinal != valMin and cantFinal != valMax):
        cantFinal = 0
        print("Cantidad final no válida")
        datos()

    jarras[0][0] = tam1
    jarras[1][0] = tam2

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

        # print("Está intentando pasar", cantidadOrigen, "galones de agua a una jarra que tiene una capacidad de ", capacidadDestino, "galones y contiene", cantidadDestino, "galones de agua")
        if cantidadOrigen >= disponibleDestino:
            jarras[jarraDestino][1] += disponibleDestino
            jarras[jarraOrigen][1] -= disponibleDestino
        else:
            jarras[jarraDestino][1] += cantidadOrigen
            jarras[jarraOrigen][1] -= cantidadOrigen
    mostrarInfo()

def completado():
    if jarras[jarraGrande()][1] == cantFinal:
        return True
    return False

def resolver():
    capMenor = 0
    capMayor = 0
    numJarraPeq = 1
    numJarraGrande = (jarraGrande() + 1)
    if (numJarraGrande == 1):
        numJarraPeq = 2
        capMenor = jarras[1][0]
        capMayor = jarras[0][0]
    else:
        capMenor = jarras[0][0]
        capMayor = jarras[1][0]

    if capMayor == cantFinal:
        llenarJarra(numJarraGrande)
    elif (capMayor / 2) == capMenor:
        llenarJarra(numJarraPeq)
        moverAgua(numJarraPeq, numJarraGrande)
    else:
        while completado() == False:
            opc = 0
            if jarras[numJarraGrande - 1][1] == 0:
                opc = 1
            elif jarras[numJarraPeq - 1][1] == capMenor:
                opc = 2
            else:
                opc = 3

            if opc == 1:
                llenarJarra(numJarraGrande)
            elif opc == 2:
                vaciarJarra(numJarraPeq)
            elif opc == 3:
                moverAgua(numJarraGrande, numJarraPeq)

def jugar():
    while completado() == False:
        limpiar()
        print("Para resolver el problema deben quedar", cantFinal,"galones de agua en la jarra más grande")
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

datos()
resolver()
# jugar()

print("Problema resuelto")