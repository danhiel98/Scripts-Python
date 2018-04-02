def calcularFactorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * calcularFactorial(numero-1)

if __name__ == "__main__":
    try:
        num = int(input("Introduzca un número para calcular su factorial\n"))
        if num < 0:
            print("Debe introducir un número mayor o igual a 0")
        else:
            print("El factorial de",num,"es",calcularFactorial(num))
    except:
        print("Algo salió mal")