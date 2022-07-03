from turtle import clear
from Grafo import Grafo
from collections import defaultdict

vertices = ['1', '2', '3', '4', '5', '6']

grafo = Grafo()

for i in range(len(vertices)):
    grafo.adicionar_vertice(vertices[i])

# grafo.list_vertices()

grafo.adicionar_arestas('1', '2')
grafo.adicionar_arestas('1', '3')
grafo.adicionar_arestas('2', '3')
grafo.adicionar_arestas('2', '4')
grafo.adicionar_arestas('3', '4')
grafo.adicionar_arestas('4', '5')
grafo.adicionar_arestas('5', '6')
grafo.adicionar_arestas('6', '3')

# grafo.list_arestas()

grafo.rm_vertice('2')
grafo.list_vertices()

# grafo.rm_aresta('4', '5')
grafo.list_arestas()

# grafo.busca_aresta('4', '3')

grafo.adjacentes('6')

# print(grafo.grau_vertice('1'))

# grafo.grau_grafo()
