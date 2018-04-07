import os

def limpiar():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    else:
        print("No se puede limpiar la pantalla")

misioneros = [
    [
        "Origen", [2,4,6]
    ],
    [
        "Bote", []
    ],
    [
        "Destino", []
    ]
]
canibales = [
    [
        "Origen", [1,3,5]
    ],
    [
        "Bote", []
    ],
    [
        "Destino", []
    ]
]

# 0 = Origen, 2 = Destino
ubicacionOrigen = 0
ubicacionDestino = 2
finalizado = False

def restablecer():
    ubicacionOrigen = 0
    ubicacionDestino = 2

    misioneros[0][1] = [2, 4, 6]
    canibales[0][1] = [1, 3, 5]
    for i in range(len(misioneros)):
        if i > 0:
            misioneros[i][1] = []
    
    for i in range(len(canibales)):
        if i > 0:
            canibales[i][1] = []

def mostrarInfo():
    if ubicacionOrigen == 0:
        print("Ubicación del bote: ORIGEN")
    else:
        print("Ubicación del bote: DESTINO")
    print("---------------------------------------------")
    print("ORIGEN:\t\t", "BOTE:\t\t", "DESTINO:")
    print(len(misioneros[0][1]),"misioneros\t", len(misioneros[1][1]),"misioneros\t", len(misioneros[2][1]),"misioneros")
    print(len(canibales[0][1]),"caníbales\t", len(canibales[1][1]),"caníbales\t", len(canibales[2][1]),"caníbales")
    print("---------------------------------------------")

def pasajeros():
    pasajerosBote = len(misioneros[1][1]) + len(canibales[1][1])
    return pasajerosBote

def subirMisionero():
    # print("=>Subir misionero")
    if pasajeros() < 2:
        disponibles = len(misioneros[ubicacionOrigen][1]) # La lista de los misioneros que se encuentran en la ubicación actual del bote
        if disponibles > 0:
            misioneros[1][1].append(misioneros[ubicacionOrigen][1].pop(0))
    # mostrarInfo()

def subirCanibal():
    # print("=>Subir caníbal")
    if pasajeros() < 2:
        disponibles = len(canibales[ubicacionOrigen][1]) # La lista de los canibales que se encuentran en la ubicación actual del bote
        if disponibles > 0:
            canibales[1][1].append(canibales[ubicacionOrigen][1].pop(0))
    # mostrarInfo()

def bajarMisionero():
    # print("=>Bajar misionero")
    enBote = len(misioneros[1][1])
    if enBote > 0:
        misioneros[ubicacionOrigen][1].append(misioneros[1][1].pop(0))
    # mostrarInfo()

def bajarCanibal():
    # print("=>Bajar caníbal")
    enBote = len(canibales[1][1])
    if enBote > 0:
        canibales[ubicacionOrigen][1].append(canibales[1][1].pop(0))
    # mostrarInfo()

def moverBote():
    global ubicacionOrigen, ubicacionDestino, finalizado
    
    if ubicacionOrigen == 0:
        x = "origen"
        y = "destino"
    else:
        x = "destino"
        y = "origen"
    
    if pasajeros() > 0:
        misionerosBote = len(misioneros[1][1])
        canibalesBote = len(canibales[1][1])

        if misionerosBote > 0:
            for i in range(len(misioneros[1][1])):
                misioneros[ubicacionDestino][1].append(misioneros[1][1].pop(0))
        
        if canibalesBote > 0:
            for i in range(len(canibales[1][1])):
                canibales[ubicacionDestino][1].append(canibales[1][1].pop(0))
        
        ubicacionTemporal = ubicacionOrigen
        ubicacionOrigen = ubicacionDestino
        ubicacionDestino = ubicacionTemporal
        
        print("=>Mover bote desde",x,"hacia",y,"con",misionerosBote,"misioneros y",canibalesBote,"caníbales")
        mostrarInfo()

        if verificar() == False:
            finalizado = True
            print("¡Vaya! Perdiste :(")
            restablecer()
        
        if len(misioneros[2][1]) + len(canibales[2][1]) == 6:
            finalizado = True
            print("¡Problema resuelto!")
            restablecer()

def verificar():
    misionerosOrigen = len(misioneros[0][1])
    canibalesOrigen = len(canibales[0][1])
    
    misionerosDestino = len(misioneros[2][1])
    canibalesDestino = len(canibales[2][1])

    if (misionerosOrigen > 0 and misionerosOrigen < canibalesOrigen) or (misionerosDestino > 0 and misionerosDestino < canibalesDestino):
        return False
    return True

def resolver():
    mostrarInfo()
    subirCanibal()
    subirCanibal()
    moverBote()
    subirCanibal()
    moverBote()
    subirCanibal()
    subirCanibal()
    moverBote()
    subirCanibal()
    moverBote()
    subirMisionero()
    subirMisionero()
    moverBote()
    subirCanibal()
    subirMisionero()
    moverBote()
    subirMisionero()
    subirMisionero()
    moverBote()
    subirCanibal()
    moverBote()
    subirCanibal()
    subirCanibal()
    moverBote()
    subirCanibal()
    moverBote()
    subirCanibal()
    subirCanibal()
    moverBote()

def jugar():
    while finalizado == False:
        limpiar()
        print("Origen:",ubicacionOrigen,"Destino:",ubicacionDestino)
        mostrarInfo()
        print("1. Subir misionero")
        print("2. Bajar misionero")
        print("3. Subir caníbal")
        print("4. Bajar canibal")
        print("5. Mover bote")
        opc = int(input("¿Qué desea hacer?\n"))
        if opc == 1:
            subirMisionero()
        elif opc == 2:
            bajarMisionero()
        elif opc == 3:
            subirCanibal()
        elif opc == 4:
            bajarCanibal()
        elif opc == 5:
            moverBote()

resolver()
# jugar()