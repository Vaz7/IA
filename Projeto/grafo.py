# LICENCIATURA EM ENGENHARIA INFORMÁTICA
# MESTRADO integrado EM ENGENHARIA INFORMÁTICA

# Inteligência Artificial
# 2022/23

# Draft Ficha 1


# Biblioteca de tratamento de grafos necessária para desenhar graficamente o grafo
import networkx as nx
# Biblioteca de tratamento de grafos necessária para desenhar graficamente o grafo
import matplotlib.pyplot as plt

# biblioteca necessária para se poder utilizar o valor math.inf  (infinito)
import math
from queue import Queue

# Importar a classe nodo
from nodos import Node
from math import sqrt


# Definição da classe grafo:
# Um grafo tem uma lista de nodos,
# um dicionário:  nome_nodo -> lista de tuplos (nome_nodo,peso)
# para representar as arestas
# uma flag para indicar se é direcionado ou não
class Graph:
    # Construtor da classe
    def __init__(self, directed=True):
        self.m_nodes = []  # lista de nodos do grafo
        self.m_directed = directed  # se o grafo é direcionado ou nao
        self.m_graph = {}  # dicionario para armazenar os nodos, arestas  e pesos
        self.m_h = {}  # dicionário para armazenar heuristica para cada nodo
        self.rows = 0
        self.columns = 0

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
    def add_edge(self, node1, coord1, node2, coord2, weight):  # node1 e node2 são os 'nomes' de cada nodo
        n1 = Node(node1, coord1)  # cria um objeto node  com o nome passado como parametro
        n2 = Node(node2, coord2)  # cria um objeto node  com o nome passado como parametro
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
        custoT = math.inf
        a = self.m_graph[node1]  # lista de arestas para aquele nodo
        for (nodo, coord, custo) in a:
            if coord == node2:
                custoT = custo
        return custoT

    ######################################
    # Dado um caminho calcula o seu custo
    #####################################
    def calcula_custo(self, caminho):
        # caminho é uma lista de nomes de nodos
        teste = caminho
        custo = 0
        i = 0
        while i + 1 < len(teste):
            custo = custo + self.get_arc_cost(teste[i], teste[i + 1])
            i = i + 1
        return custo

    ################################################################################
    # Procura DFS
    ####################################################################################
    def procura_DFS(self, start, end, path=[], visited=set(), seen=[]):
        path.append(start)
        visited.add(start)

        if start in end:
            # calcular o custo do caminho funçao calcula custo.
            custoT = self.calcula_custo(path)
            return (path, custoT,seen)
        for (adjacente, coord, peso) in self.m_graph[start]:
            if coord not in visited:
                seen.append(coord)
                resultado = self.procura_DFS(coord, end, path, visited, seen)
                if resultado is not None:
                    return resultado
        path.pop()  # se nao encontra remover o que está no caminho......
        return None

    def getNodo(self, coord):
        for nodo in self.m_nodes:
            if nodo.getCoord() == coord:
                return nodo

    #####################################################
    # Procura BFS em que o carro pode bater
    ######################################################

    def procura_BFS(self, start, end):
        # definir nodos visitados para evitar ciclos
        visited = set()
        fila = Queue()
        custo = math.inf
        seen = []

        # adicionar o nodo inicial à fila e aos visitados
        fila.put(start)
        visited.add(start)

        # garantir que o start node nao tem pais...
        parent = dict()
        parent[start] = None

        path_found = False
        while not fila.empty() and path_found == False:
            nodo_atual = fila.get()
            seen.append(nodo_atual)

            nodo = self.getNodo(nodo_atual)

            if nodo_atual in end:
                path_found = True
            else:
                for (adjacente, coord, peso) in self.m_graph[nodo_atual]:
                    if coord not in visited:
                        if nodo.getName() != 'X' or nodo.getName() == 'X' and adjacente != 'X':
                            fila.put(coord)
                            parent[coord] = nodo_atual
                            visited.add(coord)

        # Reconstruir o caminho

        path = []
        if path_found:
            path.append(nodo_atual)
            while parent[nodo_atual] is not None:
                path.append(parent[nodo_atual])
                nodo_atual = parent[nodo_atual]
            path.reverse()
            # funçao calcula custo caminho
            custo = self.calcula_custo(path)
        return (path, custo, seen)

    #####################################################
    # Procura BFS em que o carro nunca bate
    ######################################################
    def procura_BFS_NotHitting(self, start, end):
        # definir nodos visitados para evitar ciclos
        visited = set()
        fila = Queue()
        custo = math.inf

        # adicionar o nodo inicial à fila e aos visitados
        fila.put(start)
        visited.add(start)

        # garantir que o start node nao tem pais...
        parent = dict()
        parent[start] = None

        path_found = False
        while not fila.empty() and path_found == False:
            nodo_atual = fila.get()

            nodo = self.getNodo(nodo_atual)

            if nodo_atual in end:
                path_found = True
            else:
                for (adjacente, coord, peso) in self.m_graph[nodo_atual]:
                    if coord not in visited:
                        if nodo.getName() != 'X':
                            fila.put(coord)
                            parent[coord] = nodo_atual
                            visited.add(coord)

        # Reconstruir o caminho

        path = []
        if path_found:
            path.append(nodo_atual)
            while parent[nodo_atual] is not None:
                path.append(parent[nodo_atual])
                nodo_atual = parent[nodo_atual]
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
        g = nx.DiGraph()

        # Converter para o formato usado pela biblioteca networkx
        for nodo in lista_v:
            name = nodo.getName()
            n = nodo.getCoord()
            g.add_node(n)
            for (adjacente, coord, peso) in self.m_graph[n]:
                lista1 = (n, name)
                lista2 = (coord, adjacente)
                # lista_a.append(lista)
                g.add_edge(n, coord, weight=peso)

        # desenhar o grafo
        # plt.figure(figsize=(19.2,10.8)) #1080p
        # plt.figure(figsize=(25.6,14.4)) #1440p
        plt.figure(figsize=(38.4, 21.6))  # 4k
        # plt.figure(figsize=(76.8,43.2))  #8k
        pos = nx.spring_layout(g, k=100000, iterations=1000)
        nx.draw_networkx(g, pos, with_labels=True, font_weight='bold')
        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

        # plt.draw()
        plt.show()

    #############################################
    # Adiciona heuristica a nodo
    #############################################

    def add_heuristica(self, coord, name, estima):
        n1 = Node(name, coord)
        if n1 in self.m_nodes:
            self.m_h[coord] = estima

    ###################################################
    # Devolve vizinhos de um nó
    ###################################################

    def getNeighbours(self, nodo):
        lista = []
        for (adjacente, coord, peso) in self.m_graph[nodo]:
            lista.append((coord, peso))
        return lista

    def getNeighboursV(self, nodo, velocidade, end):
        lista = []
        vc, vl = velocidade
        x, y = nodo

        #print(nodo)
        for (adjacente, coord, peso) in self.m_graph[nodo]:
            #if coord == (x + vc + 1, y + vl + 1) or \
            #        coord == (x + vc + -1, y + vl + 1) or \
            #        coord == (x + vc + -1, y + vl + 0) or \
            #        coord == (x + vc + 1, y + vl + 0) or \
            #        coord == (x + vc + -1, y + vl + -1) or \
            #        coord == (x + vc + 0, y + vl + -1) or \
            #        coord == (x + vc + 0, y + vl + 1) or \
            #        coord == (x + vc + 1, y + vl + -1):
            #    lista.append((coord, peso))
            cx, cy = coord
            #if (x + vc + 1) >= cx >= (x + vc + -1) and cy == (y + vl + 1) or \
            #   (x + vc + 1) >= cx >= (x + vc + -1) and cy == (y + vl + 0) or \
            #   (x + vc + 1) >= cx >= (x + vc + -1) and cy == (y + vl + -1):
            if cx >= self.columns:
                cx = self.columns - 1
            if cx < 0:
                cx = 0
            if cy >= self.rows:
                cy = self.rows - 1
            if cy < 0:
                cy = 0

            #if (cx - 1, cy) in end:
            #    lista.append(((cx - 1, cy), 1))
            #if (cx, cy - 1) in end:
            #    lista.append(((cx, cy - 1), 1))
            #if (cx - 1, cy - 1) in end:
            #    lista.append(((cx - 1, cy - 1), 1))
            #if (cx + 1, cy) in end:
            #    lista.append(((cx + 1, cy), 1))
            #if (cx, cy + 1) in end:
            #    lista.append(((cx, cy + 1), 1))
            #if (cx + 1, cy + 1) in end:
            #    lista.append(((cx + 1, cy + 1), 1))
            #if (cx + 1, cy - 1) in end:
            #    lista.append(((cx + 1, cy - 1), 1))
            #if (cx - 1, cy + 1) in end:
            #    lista.append(((cx - 1, cy + 1), 1))

            for finish in end:
                fx, fy = finish
                if (x + -abs(vc) + -1) <= fx <= (x + abs(vc) + 1) and (y + -abs(vl) + -1) <= fy <= (y + abs(vl) + 1):
                    lista.append((finish, 1))

            if (x + abs(vc) + -1) <= cx <= (x + abs(vc) + 1) and (y + abs(vl) + -1) <= cy <= (y + abs(vl) + 1) or \
               (x + abs(vc) + -1) <= cx <= (x + abs(vc) + 1) and (y + -abs(vl) + -1) <= cy <= (y + -abs(vl) + 1) or \
               (x + -abs(vc) + -1) <= cx <= (x + -abs(vc) + 1) and (y + abs(vl) + -1) <= cy <= (y + abs(vl) + 1) or \
               (x + -abs(vc) + -1) <= cx <= (x + -abs(vc) + 1) and (y + -abs(vl) + -1) <= cy <= (y + -abs(vl) + 1):
                lista.append((coord, peso))

        # TODO: Avaliar se esta lista está a ser bem construída
        #print(lista)

        return lista

    #############################################
    # Pesquisa informada A* (a estrela)
    #############################################
    def a_star(self, start, end, wall):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = {start}
        closed_list = set([])
        nodo_ant = start
        seen = []

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}  ##  g é apra substiruir pelo peso  ???

        g[start] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start] = []
        n = None
        while len(open_list) > 0:
            # find a node with the lowest value of f() - evaluation function
            hit = False
            calc_heurist = {}
            flag = 0
            for v in open_list:
                if n == None:
                    n = v
                else:
                    flag = 1
                    calc_heurist[v] = g[v] + self.getH(v)
            if flag == 1:
                min_estima = self.calcula_est(calc_heurist)
                n = min_estima
            if n == None:
                print('Path does not exist!')
                return None
            seen.append(n)
            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n in end:
                reconst_path = []

                while parents[n]:
                    parents[n].reverse()
                    p = parents[n].pop()
                    reconst_path.append(n)
                    n = p

                reconst_path.append(start)

                reconst_path.reverse()

                # print('Path found: {}'.format(reconst_path))
                return (reconst_path, self.calcula_custo(reconst_path), seen)

            if n in wall:
                hit = True
                # print(nodo_ant)
                # print(n)
                # temp = n
                open_list.remove(n)
                closed_list.add(n)
                parents[nodo_ant].append(n)
                # nodo_ant = temp
                n = nodo_ant
                # closed_list.add(nodo_ant)
                open_list.add(n)

            if n != start and hit == False:
                # print(n)
                # if speed[n][0] > 5:
                #    speed[n] = (5, speed[n][1])
                # if speed[n][1] > 5:
                #    speed[n] = (speed[n][0], 5)
                # if speed[n][0] < -5:
                #    speed[n] = (-5, speed[n][1])
                # if speed[n][1] < -5:
                #    speed[n] = (speed[n][0], -5)
                nodo_ant = n

            # print(n)
            # print(speed[n])

            # for all neighbors of the current node do
            for (m, weight) in self.getNeighboursV(n, (0, 0), end):  # definir função getneighbours  tem de ter um par nodo peso
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = []
                    parents[m].append(n)
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m].append(n)

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None

    #############################################
    # Pesquisa gulosa
    #############################################
    def checkNeighbours(self, nodo, list):

        x, y = nodo

        for (adjacente, coord, peso) in self.m_graph[nodo]:
            cx, cy = coord

            if adjacente != 'X' and x-1 <= cx <= x+1 and y-1 <= cy <= y+1 and coord in list:
                #print('Cheguei aqui!')
                return True

        return False

    def greedy(self, start, end, wall, vel):
        # open_list é uma lista de nodos visitados, mas com vizinhos
        # que ainda não foram todos visitados, começa com o  start
        # closed_list é uma lista de nodos visitados
        # e todos os seus vizinhos também já o foram
        open_list = set([start])
        closed_list = set([])
        nodo_ant = start
        speed = {}
        speed[start] = vel
        seen = []

        # parents é um dicionário que mantém o antecessor de um nodo
        # começa com start
        parents = {}
        parents[start] = []
        #parents[start].append(start)

        while len(open_list) > 0:
            n = None
            hit = False

            # encontraf nodo com a menor heuristica
            for v in open_list:
                if n == None or self.m_h[v] < self.m_h[n]:
                    n = v

            if n == None:
                print('Path does not exist!')
                return None
            seen.append(n)
            # se o nodo corrente é o destino
            # reconstruir o caminho a partir desse nodo até ao start
            # seguindo o antecessor
            if n in end:
                reconst_path = []

                while parents[n]:
                    parents[n].reverse()
                    p = parents[n].pop()
                    reconst_path.append(n)
                    n = p

                reconst_path.append(start)

                reconst_path.reverse()

                return (reconst_path, self.calcula_custo(reconst_path), seen)

            if n in wall:
                hit = True
                #print(nodo_ant)
                #print(n)
                #temp = n
                open_list.remove(n)
                closed_list.add(n)
                parents[nodo_ant].append(n)
                #nodo_ant = temp
                if self.checkNeighbours(n, open_list):
                    speed[n] = (0, 0)
                n = nodo_ant
                #closed_list.add(nodo_ant)
                open_list.add(n)

            #print(n)
            #print(open_list)

            if n != start and hit == False:
                x, y = n
                #print(n)
                a, b = parents[n][len(parents[n])-1]
                vc, vl = (x - a, y - b)
                speed[n] = (speed[parents[n][len(parents[n])-1]][0] + vc, speed[parents[n][len(parents[n])-1]][1] + vl)
                nodo_ant = n
                #print(nodo_ant)
            #print(n)
            #print(speed[n])

            # para todos os vizinhos  do nodo corrente
            for (m, weight) in self.getNeighboursV(n, speed[n], end):
                # Se o nodo corrente nao esta na open nem na closed list
                # adiciona-lo à open_list e marcar o antecessor
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = []
                    parents[m].append(n)

            # remover n da open_list e adiciona-lo à closed_list
            # porque todos os seus vizinhos foram inspecionados
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None
    def calcula_est(self, estima):
        l = list(estima.keys())
        min_estima = estima[l[0]]
        node = l[0]
        for k, v in estima.items():
            if v < min_estima:
                min_estima = v
                node = k
        return node

    ##########################################
    #    A*
    ##########################################

    def procura_aStar(self, start, end, wall, vel):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = {start}
        closed_list = set([])
        nodo_ant = start
        speed = {}
        speed[start] = vel
        seen = []

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}  ##  g é apra substiruir pelo peso  ???

        g[start] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start] = []
        n = None
        while len(open_list) > 0:
            # find a node with the lowest value of f() - evaluation function
            hit = False
            calc_heurist = {}
            flag = 0
            for v in open_list:
                if n == None:
                    n = v
                else:
                    flag = 1
                    calc_heurist[v] = g[v] + self.getH(v)
            if flag == 1:
                min_estima = self.calcula_est(calc_heurist)
                n = min_estima
            if n == None:
                print('Path does not exist!')
                return None
            seen.append(n)
            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n in end:
                reconst_path = []

                while parents[n]:
                    parents[n].reverse()
                    p = parents[n].pop()
                    reconst_path.append(n)
                    n = p

                reconst_path.append(start)

                reconst_path.reverse()

                # print('Path found: {}'.format(reconst_path))
                return (reconst_path, self.calcula_custo(reconst_path), seen)

            if n in wall:
                hit = True
                # print(nodo_ant)
                # print(n)
                # temp = n
                open_list.remove(n)
                closed_list.add(n)
                parents[nodo_ant].append(n)
                # nodo_ant = temp
                if self.checkNeighbours(n, open_list):  # TODO: Rever esta função!
                    speed[n] = (0, 0)
                n = nodo_ant
                # closed_list.add(nodo_ant)
                open_list.add(n)

            if n != start and hit == False:
                x, y = n
                #print(n)
                a, b = parents[n][len(parents[n])-1]
                vc, vl = (x - a, y - b)
                speed[n] = (speed[parents[n][len(parents[n])-1]][0] + vc, speed[parents[n][len(parents[n])-1]][1] + vl)
                #if speed[n][0] > 5:
                #    speed[n] = (5, speed[n][1])
                #if speed[n][1] > 5:
                #    speed[n] = (speed[n][0], 5)
                #if speed[n][0] < -5:
                #    speed[n] = (-5, speed[n][1])
                #if speed[n][1] < -5:
                #    speed[n] = (speed[n][0], -5)
                nodo_ant = n

            #print(n)
            #print(speed[n])

            # for all neighbors of the current node do
            for (m, weight) in self.getNeighboursV(n, speed[n], end):  # definir função getneighbours  tem de ter um par nodo peso
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = []
                    parents[m].append(n)
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m].append(n)

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None

    ###################################3
    # devolve heuristica do nodo
    ####################################

    def getH(self, nodo):
        if nodo not in self.m_h.keys():
            return 1000
        else:
            return (self.m_h[nodo])
