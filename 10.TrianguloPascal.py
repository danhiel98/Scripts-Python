def trianguloPascal(filas):
	if filas == 0:
		return []
	elif filas == 1:
		return [[1]]
	
	else:
		nuevaFila = [1]
		resultado = trianguloPascal(filas-1)
		ultimaFila = resultado[-1]

		for i in range(len(ultimaFila)-1):
			nuevaFila.append(ultimaFila[i] + ultimaFila[i+1])

		nuevaFila += [1]
		resultado.append(nuevaFila)

	return resultado

cntFilas = int(input("Cantidad de filas:\n"))
for i in trianguloPascal(cntFilas):
	print(i)