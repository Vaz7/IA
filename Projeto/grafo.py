#LICENCIATURA EM ENGENHARIA INFORMÁTICA
#MESTRADO integrado EM ENGENHARIA INFORMÁTICA

#Inteligência Artificial
#2022/23

#Draft Ficha 1




# Biblioteca de tratamento de grafos necessária para desenhar graficamente o grafo
import networkx as nx
# Biblioteca de tratamento de grafos necessária para desenhar graficamente o grafo
import matplotlib.pyplot as plt

#biblioteca necessária para se poder utilizar o valor math.inf  (infinito)
import math
from queue import Queue

# Importar a classe nodo
from nodos import Node

#Definição da classe grafo:
#Um grafo tem uma lista de nodos,
#um dicionário:  nome_nodo -> lista de tuplos (nome_nodo,peso)
#para representar as arestas 
#uma flag para indicar se é direcionado ou não
class Graph:
    # Construtor da classe
    def __init__(self, directed=True):
        self.m_nodes = []   # lista de nodos do grafo
        self.m_directed = directed   # se o grafo é direcionado ou nao
        self.m_graph = {}   #  dicionario para armazenar os nodos, arestas  e pesos



    ##############################
    # Escrever o grafo como string
    ##############################
    def __str__(self):
        out = ""
        for key in self.m_graph.keys():
            out = out + "node " + str(key) + ": " + str(self.m_graph[key]) + "\n"
        return out

    #####################################
    # Adicionar aresta no grafo, com peso
    ####################################
    def add_edge(self, node1, coord1, node2, coord2, weight):   #node1 e node2 são os 'nomes' de cada nodo
        n1 = Node(node1, coord1)     # cria um objeto node  com o nome passado como parametro
        n2 = Node(node2, coord2)     # cria um objeto node  com o nome passado como parametro
        if (n1 not in self.m_nodes):
            self.m_nodes.append(n1)
            self.m_graph[coord1] = set()
        else:
            n1 = self.get_node_by_coord(node1, coord1)

        if (n2 not in self.m_nodes):
            self.m_nodes.append(n2)
            self.m_graph[coord2] = set()
        else:
            n2 = self.get_node_by_coord(node2, coord2)

        self.m_graph[coord1].add((node2, coord2, weight))

        # se o grafo for nao direcionado, colocar a aresta inversa
        if not self.m_directed:
            self.m_graph[coord2].add((node1, coord1, weight))

    ################################
    # Encontrar nodo pelo nome
    ################################
    def get_node_by_coord(self, name, coord):
        search_node = Node(name, coord)
        for node in self.m_nodes:
            if node == search_node:
                return node
            else:
                return None

    ###########################
    # Imprimir arestas
    ###########################
    def imprime_aresta(self):
        listaA = ""
        for nodo in self.m_graph.keys():
            for (nodo2, custo) in self.m_graph[nodo]:
                listaA = listaA + nodo + " ->" + nodo2 + " custo:" + str(custo) + "\n"
        return listaA

    ################################
    # Devolver o custo de uma aresta
    ################################
    def get_arc_cost(self, node1, node2):
        custoT=math.inf
        a=self.m_graph[node1]    # lista de arestas para aquele nodo
        for (nodo,coord,custo) in a:
            if coord==node2:
                custoT=custo

        return custoT



    ######################################
    # Dado um caminho calcula o seu custo
    #####################################
    def calcula_custo(self, caminho):
        #caminho é uma lista de nomes de nodos
        teste=caminho
        custo=0
        i=0
        while i+1 < len(teste):
             custo=custo + self.get_arc_cost(teste[i], teste[i+1])
             i=i+1
        return custo


    ################################################################################
    # Procura DFS
    ####################################################################################
    def procura_DFS(self,start, end, path=[], visited=set()):
        path.append(start)
        visited.add(start)

        if start == end:
            # calcular o custo do caminho funçao calcula custo.
            custoT= self.calcula_custo(path)
            return (path, custoT)
        for (adjacente, coord, peso) in self.m_graph[start]:
            if coord not in visited:
                resultado = self.procura_DFS(coord, end, path, visited)
                if resultado is not None:
                    return resultado
        path.pop()  # se nao encontra remover o que está no caminho......
        return None

    def procura_BFS(self, start, end):
        # definir nodos visitados para evitar ciclos
        visited = set()
        fila = Queue()

        # adicionar o nodo inicial à fila e aos visitados
        fila.put(start)
        visited.add(start)

        # garantir que o start node nao tem pais...
        parent = dict()
        parent[start] = None

        path_found = False
        while not fila.empty() and path_found == False:
            nodo_atual = fila.get()
            if nodo_atual == end:
                path_found = True
            else:
                for (adjacente, coord, peso) in self.m_graph[nodo_atual]:
                    if coord not in visited:
                        fila.put(coord)
                        parent[coord] = nodo_atual
                        visited.add(coord)

        # Reconstruir o caminho

        path = []
        if path_found:
            path.append(end)
            while parent[end] is not None:
                path.append(parent[end])
                end = parent[end]
            path.reverse()
            # funçao calcula custo caminho
            custo = self.calcula_custo(path)
        return (path, custo)

    ###########################
    # desenha grafo  modo grafico
    #########################
    def desenha(self):
        ##criar lista de vertices
        lista_v = self.m_nodes
        lista_a = []
        g=nx.DiGraph()

        #Converter para o formato usado pela biblioteca networkx
        for nodo in lista_v:
            name = nodo.getName()
            n = nodo.getCoord()
            g.add_node(n)
            for (adjacente, coord, peso) in self.m_graph[n]:
                lista1 = (n, name)
                lista2 = (coord, adjacente)
                #lista_a.append(lista)
                g.add_edge(n,coord,weight=peso)

        #desenhar o grafo
        #plt.figure(figsize=(19.2,10.8)) #1080p
        #plt.figure(figsize=(25.6,14.4)) #1440p
        plt.figure(figsize=(38.4,21.6))  #4k
        #plt.figure(figsize=(76.8,43.2))  #8k
        pos = nx.spring_layout(g,k=100000,iterations=1000)
        nx.draw_networkx(g, pos, with_labels=True, font_weight='bold')
        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

        #plt.draw()
        plt.show()
