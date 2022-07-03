from pydoc import visiblename
from wsgiref.validate import validator


class Vertice():
    def __init__(self, nome):
        self.nome = nome
        self.vizinhos = []

class Aresta():
    def __init__(self, vini, vfim):
        self.vini = vini
        self.vfim = vfim

class Grafo():

    def __init__(self):
        self.vertices = []
        self.arestas = []

    def adicionar_vertice(self, vertice):
        vertice = Vertice(vertice)
        self.vertices.append(vertice)

    def adicionar_arestas(self, ini, fim):
        for i in range(len(self.vertices)):
            if (self.vertices[i].nome == ini):
                verticeini = self.vertices[i]
            if (self.vertices[i].nome == fim):
                verticefim = self.vertices[i]
        if (verticeini and verticefim):
            aresta = Aresta(verticeini, verticefim)
            verticeini.vizinhos.append(verticefim)
            verticefim.vizinhos.append(verticeini)
            self.arestas.append(aresta)
        else:
            return print('Um dos vertices não foi encontrado.')
    
    def list_vertices(self):
        for vertice in range(len(self.vertices)): 
            print(self.vertices[vertice].nome)
    
    def list_arestas(self):
        for aresta in range(len(self.arestas)): 
            print(f'{self.arestas[aresta].vini.nome} {self.arestas[aresta].vfim.nome}')

    def rm_vertice(self, vertice):
        vertice_del = 0
        indice = 0
        achou = False
        aresta_ini = []
        aresta_fim = []
        for i in range(len(self.vertices)):
            if (self.vertices[i].nome == vertice):
                vertice_aux = self.vertices[i]
                indice = i
                achou = True
        if (achou):
            for i in range(len(self.arestas)-1):
                if vertice_aux.nome == self.arestas[i].vini.nome:
                    aresta_fim.append(self.arestas[i].vfim.nome)
            
            for i in range(len(self.arestas)-1):
                if vertice_aux.nome == self.arestas[i].vfim.nome:
                    aresta_ini.append(self.arestas[i].vini.nome)
            
            for i in range(len(aresta_ini)):
                self.rm_aresta(aresta_ini[i], vertice_aux.nome)
            
            for i in range(len(aresta_fim)):
                self.rm_aresta(vertice_aux.nome, aresta_fim[i])
            
            self.vertices.pop(indice)
            return print('Vertice Removido!')
        else:
            print('Vertice não encontrado!')
    
    def rm_aresta(self, verticeini, verticefim):
        count=0
        for i in range(len(self.arestas)):
            if (self.arestas[i].vini.nome == verticeini and self.arestas[i].vfim.nome == verticefim):
                self.arestas.pop(i)
                count+=1
                break
        if count>=1:
            return print('Aresta removida!')
        return print('Aresta não encontrada!')
    
    def busca_aresta(self, verticeini, verticefim):
        for i in range(len(self.arestas)):
            if (self.arestas[i].vini.nome == verticeini and self.arestas[i].vfim.nome == verticefim or self.arestas[i].vini.nome == verticefim and self.arestas[i].vfim.nome == verticeini):
                return print('Aresta Encontrada!')
        return print('Aresta não encontrada!')
    
    def grau_vertice(self, vertice):
        count = 0
        for j in range(len(self.vertices)):
            for i in range(len(self.arestas)):
                if (self.arestas[i].vini.nome == vertice and self.arestas[i].vfim.nome == self.vertices[j].nome):
                    count+=1
        return count

    def grau_grafo(self):
        grau_max = int(self.grau_vertice(self.vertices[0].nome))
        grau_min = grau_max
        grau_medio = 0

        for vertice in self.vertices:
            grau_aux = int(self.grau_vertice(vertice.nome))
            grau_medio += grau_aux

            if (grau_aux > grau_max):
                grau_max = grau_aux
            if (grau_aux < grau_min):
                grau_min = grau_aux

        grau_medio /= len(self.vertices)

        print(f'Grau mínimo: {grau_min}')
        print(f'Grau médio: {grau_medio:.3}')
        print(f'Grau máximo: {grau_max}')

    def busca_vertice(self, vertice):
        for i in range(len(self.vertices)):
            if (self.vertices[i].nome == vertice):
                return self.vertices[i]

    def adjacentes(self, vertice):
        vertice_aux = self.busca_vertice(vertice)
        
        if (vertice_aux):
            for i in range(len(vertice_aux.vizinhos)):
                if (vertice_aux.vizinhos[i].nome):
                    print(vertice_aux.vizinhos[i].nome)
                else:
                    ('O vértice não possui vizinhos.')
        else:
            print('Vertice inexistente.')
        
                    
                    
        

