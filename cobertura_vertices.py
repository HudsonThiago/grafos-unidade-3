caminhoGrafo2 = "./casos de uso/grafo2.txt"


def lerGrafo(caminhoGrafo):
    arquivo = open(caminhoGrafo, "r")

    arquivo.seek(0, 0)

    grafo = []

    for i in arquivo.readlines():
        verticesAdjacentes = list(map(int, i.split()))
        grafo.append(verticesAdjacentes)

    arquivo.close()

    return grafo


grafo2 = lerGrafo(caminhoGrafo2)

print(grafo2)
