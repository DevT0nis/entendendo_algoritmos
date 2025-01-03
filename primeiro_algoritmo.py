def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else: 
            baixo = meio + 1
    return None

minha_lista = [1, 15, 30, 50, 100]

print(pesquisa_binaria(minha_lista, 15))
print(pesquisa_binaria(minha_lista, 100))