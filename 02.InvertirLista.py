listaInvertida = []
def invertirLista(lista):
    if len(lista) == 0:
        return listaInvertida
    else:
        return listaInvertida + [lista.pop(len(lista) - 1)] + invertirLista(lista)

letras = ["a","b","c","d","e"]
print("Lista invertida:\n", invertirLista(letras))
