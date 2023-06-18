class grafo:
    def lerArquivo(self, file):
        with open(file, 'r') as file:
            list = [[int(num) for num in line.split(' ')] for line in file]

            self.n = len(list)
            self.m = 0
            self.vertices = range(self.n)
            self.listaAdj = {vertex : set() for vertex in self.vertices}

            for i in self.vertices:
                for j in self.vertices:
                    if list[i][j] == 1:
                        self.listaAdj[i].add(j)
                        self.listaAdj[j].add(i)
                        if i < j:
                            self.m += 1
    
    def cobertura(self, subconjunto):
        vertices = self.listaAdj
        for vertice in subconjunto:
            if vertice in vertices:
                for v in vertices[vertice]:
                    if v in vertice:
                        del vertice[v]
                del vertices[vertice]
        if len(vertices) == 0:
            return True
        else:
            return False

import itertools

class coberturaMinimaVertice:
    def guloso(self, graph):
        for i in range(graph.n):
            for subset in itertools.combinations(graph.vertices, i):
                if graph.cobertura(subset):
                    result = "subset: {subset}"
                    return result

g1 = grafo()
g1.lerArquivo("./casos-de-uso/grafo1.txt")

alg = coberturaMinimaVertice()
alg.guloso(g1)
