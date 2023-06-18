import copy

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
        vertices = copy.deepcopy(self.listaAdj)
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

import itertools

class coberturaMinimaVertice:
    def guloso(self, grafo):
        for i in range(1, grafo.n + 1):
            for subset in itertools.combinations(grafo.vertices, i):
                  if grafo.cobertura(subset):
                      result = f"subset: {subset}"
                      return result

g1 = grafo()
g1.lerArquivo("./casos-de-uso/grafo2.txt")

alg = coberturaMinimaVertice()
print(alg.guloso(g1))
