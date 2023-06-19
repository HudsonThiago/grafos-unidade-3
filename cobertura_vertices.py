import copy, itertools

class grafo:
    def lerArquivo(self, file):
        with open(file, 'r') as file:
            lista = [[int(num) for num in line.split(' ')] for line in file]

            self.n = len(lista)
            self.arestas = set()
            self.vertices = set(range(self.n))
            self.listaAdj = {vertex : set() for vertex in self.vertices}

            for i in self.vertices:
                for j in self.vertices:
                    if lista[i][j] == 1:
                        self.listaAdj[i].add(j)
                        self.listaAdj[j].add(i)
                        if not (j, i) in self.arestas:
                            self.arestas.add((i, j))

    
    def cobertura(self, subconjunto):
        vertices = self.listaAdj.copy()
        for vertice in subconjunto:
            if vertice in vertices:
                for v in vertices[vertice]:
                    if v in vertices:
                        del vertices[v]
                del vertices[vertice]
        if len(vertices) == 0:
            return True
        else:
            return False

def removeVertice(grafo, vertice):
    grafoRetorno = copy.copy(grafo)
    grafoRetorno.n -= 1
    grafoRetorno.vertices.remove(vertice)
    arestas = set()
    for aresta in grafoRetorno.arestas:
        if not vertice in aresta:
            arestas.add(aresta)
    grafoRetorno.arestas = arestas
    for v in grafoRetorno.listaAdj:
        if vertice in grafoRetorno.listaAdj[v]:
            grafoRetorno.listaAdj[v].remove(vertice)
        if vertice == v:
            del v    
    return grafoRetorno  

def guloso(grafo):
    for i in range(1, grafo.n):
        for subconjunto in itertools.combinations(grafo.vertices, i):
            if grafo.cobertura(subconjunto):
                resultado = f"cobertura mínima de vértice: \n"
                for vertice in grafo.listaAdj:
                    if vertice in subconjunto:
                        resultado += f"{vertice} = {grafo.listaAdj[vertice]}\n"
                return resultado

def recursivo(grafo, k):
    if k == 0:
        return None
    else:
        aresta = next(iter(grafo.arestas))
        u = aresta[0]
        g1 = removeVertice(grafo, u)
        cobertura1 = recursivo(g1, k - 1)
        if g1.cobertura(cobertura1):
            cobertura1.add(u)
            return cobertura1
        v = aresta[1]
        g2 = removeVertice(grafo, v)
        cobertura2 = recursivo(g2, k - 1)
        if g2.cobertura(cobertura2):
            cobertura2.add(v)
            return cobertura2
        return None

g1 = grafo()
g1.lerArquivo("../grafos-unidade-3/casos de uso/grafo2.txt")

print(guloso(g1))

g2 = grafo()
g2.lerArquivo("../grafos-unidade-3/casos de uso/grafo2.txt")

print(recursivo(g2, 5))