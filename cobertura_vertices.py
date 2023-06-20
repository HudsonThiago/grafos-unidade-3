import copy, itertools

class grafo:
    def lerArquivo(self, file):
        with open(file, 'r') as file:
            lista = [[int(num) for num in line.split(' ')] for line in file]

            self.arestas = set()
            self.vertices = set(range(len(lista)))
            self.listaAdj = {vertex : set() for vertex in self.vertices}

            for i in self.vertices:
                for j in self.vertices:
                    if lista[i][j] == 1:
                        self.listaAdj[i].add(j)
                        self.listaAdj[j].add(i)
                        if not (j, i) in self.arestas:
                            self.arestas.add((i, j))

    
    def cobertura(self, subconjunto):
        vertices = copy.deepcopy(self.listaAdj)
        if len(self.vertices) == 0 and subconjunto == None:
            return True
        if subconjunto != None:    
            for vertice in subconjunto:
                if vertice in vertices:
                    for v in vertices[vertice]:
                        if v in vertices:
                            del vertices[v]
                    if vertice in vertices:
                        del vertices[vertice]
        if len(vertices) == 0:
            return True
        else:
            return False

def guloso(grafo):
    for i in range(1, len(grafo.vertices)):
        for subconjunto in itertools.combinations(grafo.vertices, i):
            if grafo.cobertura(subconjunto):
                resultado = str()
                for vertice in grafo.listaAdj:
                    if vertice in subconjunto:
                        resultado += f"{vertice} = {grafo.listaAdj[vertice]}\n"
                return resultado

for i in range(1, 16):
    g = grafo()
    g.lerArquivo(f"../grafos-unidade-3/casos de uso/grafo{i}.txt")
    print(f"grafo {i}:\n{guloso(g)}")
