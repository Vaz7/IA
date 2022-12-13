import math
from copy import deepcopy

from colorama import Fore

from grafo import Graph
from nodos import Node
from math import sqrt

mapElem = {}
g = Graph()
finish_line = set()

def parseMapa():
    i = 0
    with open('mapa.txt') as f:
        contents = f.readlines()
        for content in contents:
            content = content.strip('\n')
            mapElem[i] = content.split(" ")
            i += 1
    #print('Linhas: ' + str(i) + '\nColunas: ' + str(len(mapElem[0])))

def desenhaMapa(resultado):
    lista_resultado=resultado[0]

    filepath = 'mapa.txt'


    with open(filepath) as fp:
        lines = fp.readlines()

        conjunto_nodos = []
        nodos=[]
        y=0

        for line in lines:
            x=0
            line = line.strip('\n')
            caracteres = line.split(" ")
            size = len(caracteres)
            i=0

            for i in range(size):
                caracter = caracteres[i]
                nodos.append(caracter)
                x=x+1

            conjunto_nodos.append(nodos)
            nodos = []
            y=y+1

    linha=""

    for i in range(y):
        print(Fore.WHITE)
        for j in range(x):
            if (j,i) in lista_resultado:
                print(Fore.GREEN + conjunto_nodos[i][j] + " " + Fore.WHITE,end="")

            else:
                print(conjunto_nodos[i][j] + " ",end="")

    print(" ")

# Função que inicializa o grafo para uma procura não informada
def setUpGraphNotInformed():
    y = 0
    x = 0
    columns = len(mapElem[0])
    rows = len(mapElem)
    #print('Rows: ' + str(rows) + ' Columns: ' + str(columns))

    for i in range(rows):
        for j in range(columns):
            if x+1 < columns:
                addToGraph(mapElem[y][x],(x,y),mapElem[y][x+1],(x+1,y))
                if y+1 < len(mapElem)-1:
                    addToGraph(mapElem[y][x],(x,y),mapElem[y+1][x+1],(x+1,y+1))
                if y-1 >= 0:
                    addToGraph(mapElem[y][x],(x,y),mapElem[y-1][x+1],(x+1,y-1))
            if x-1 >= 0:
                addToGraph(mapElem[y][x],(x,y),mapElem[y][x-1],(x-1,y))
                if y+1 < len(mapElem)-1:
                    addToGraph(mapElem[y][x],(x,y),mapElem[y+1][x-1],(x-1,y+1))
                if y-1 >= 0:
                    addToGraph(mapElem[y][x],(x,y),mapElem[y-1][x-1],(x-1,y-1))
            if y+1 < len(mapElem)-1:
                addToGraph(mapElem[y][x],(x,y),mapElem[y+1][x],(x,y+1))
            if y-1 >= 0:
                addToGraph(mapElem[y][x],(x,y),mapElem[y-1][x],(x,y-1))
            x += 1
        x = 0
        y += 1

# Função que inicializa o grafo para uma procura informada
def setUpGraphInformed():
    y = 0
    x = 0
    aux = 0
    temp = 0
    columns = len(mapElem[0])
    rows = len(mapElem)
    #print('Rows: ' + str(rows) + ' Columns: ' + str(columns))

    for i in range(rows):
        for j in range(columns):
            for k in range(rows):
                for n in range(columns):
                    if (aux, temp) != (x, y) and aux <= columns-1:
                        addToGraph(mapElem[y][x],(x,y),mapElem[temp][aux],(aux,temp))
                    aux += 1
                aux = 0
                temp += 1
            temp = 0
            x += 1
        x = 0
        y += 1

def addToGraph(elem1,coord1,elem2,coord2):
    if elem1 == 'P':
        global start
        start = coord1
    if elem1 == 'F':
        finish_line.add(coord1)
    if elem2 == 'X':
        g.add_edge(elem1, coord1, elem2, coord2, 25)
    elif elem2 == '-' or elem2 == 'F':
        g.add_edge(elem1, coord1, elem2, coord2, 1)


def getDist(coord):
    x, y = coord
    dist = 0

    for (a, b) in finish_line:
        current = sqrt((a-x)**2 + (b-y)**2)
        if dist == 0 or current < dist:
            dist = current

    return dist


def setUpHeuristica():
    for nodo in g.m_nodes:
        coord = nodo.getCoord()
        name = nodo.getName()
        h = getDist(coord)
        if (name != 'F'):
            h = getDist(coord)
            g.add_heuristica(coord, name, h)
        else:
            g.add_heuristica(coord,name,0)

def printGraph():
    lista = g.m_nodes
    for nodo in lista:
        coord = nodo.getCoord()
        print('Nodo ' + str(coord) + ' conhece:')
        print(g.m_graph[coord])

# Tenho de adicionar cenas ao nodo para conseguir usar as fórmulas da posição/velocidade/aceleração que estão no enunciado
parseMapa()
setUpGraphNotInformed()
#print(g.m_nodes)
#setUpGraphInformed()
#setUpHeuristica()
#printGraph()
#print(start)
#print(finish_line)
#print(g.procura_DFS(start,finish_line,path=[],visited=set()))
#g.desenha()
#print(g.procura_BFS(start,(9,3),path=[],visited=set()))
#não ligar a isto (cenas para testar consistência do algoritmo
#low = 0
##path = []
#for i in range(10000):
#    (current, custo) = g.procura_BFS(start, (9, 3))
#    if i == 0:
#        low = custo
#        path = current
#    if custo < low:
#        low = custo
#        path = current

def multiplayer(players):
    nodos = []
    paths = []
    prevs = []
    finished = []
    costs = []
    newMap = deepcopy(mapElem)

    for i in range(players):
        nodos.append(start)
        prevs.append((0, 0))
        costs.append(0)
        paths.append([])
        paths[i].append(nodos[i])

    while len(finished) != players:
        for j in range(players):
            if j not in finished:
                global g
                g = Graph()
                setUpGraphNotInformed()
                res, cost = g.procura_BFS(nodos[j], finish_line)
                prevs[j] = nodos[j]
                nodos[j] = res[1]
                costs[j] += g.get_arc_cost(prevs[j],nodos[j])
                paths[j].append(nodos[j])

                if nodos[j] not in finish_line:
                    x, y = nodos[j]
                    mapElem[y][x] = 'O'
                else:
                    finished.append(j)

                a, b = prevs[j]
                mapElem[b][a] = newMap[b][a]

    for k in range(players):
        print('Player ' + str(k) + ':\n' + 'Path: ' + ''.join(str(e) + ' ' for e in paths[k]) + '\nCost:' + str(costs[k]))

multiplayer(5)
#nodo1 = start
#ant1 = None
#nodo2 = start
#ant2 = None
#newMap = deepcopy(mapElem)
#path1 = []
#path2 = []
#
#path1.append(nodo1)
#path2.append(nodo2)
#
#while nodo1 not in finish_line and nodo2 not in finish_line:
#    g = Graph()
#    setUpGraphNotInformed()
#    res1, cost1 = g.procura_BFS_NotHitting(nodo1,finish_line)
#    ant1 = nodo1
#    nodo1 = res1[1]
#    path1.append(nodo1)
#    if nodo1 not in finish_line:
#        x1, y1 = nodo1
#        mapElem[y1][x1] = 'O'
#        a1, b1 = ant1
#        mapElem[b1][a1] = newMap[b1][a1]
#    else:
#        a1, b1 = ant1
#        mapElem[b1][a1] = newMap[b1][a1]
#        ant1 = None
#    g = Graph()
#    setUpGraphNotInformed()
#    res2, cost2 = g.procura_BFS_NotHitting(nodo2,finish_line)
#    ant2 = nodo2
 #   nodo2 = res2[1]
 #   path2.append(nodo2)
 #   if nodo1 not in finish_line:
 #       x2, y2 = nodo2
 #       mapElem[y2][x2] = 'O'
 #       a2, b2 = ant2
 #       mapElem[b2][a2] = newMap[b2][a2]
 #   else:
 #       a2, b2 = ant2
 #       mapElem[b2][a2] = newMap[b2][a2]
 #       ant2 = None
#
#    print(g.m_graph[nodo1])
#    print(g.m_graph[nodo2])
#
#print(path1)
#print(path2)

#print((path,low))
#print(g.procura_BFS(start,finish_line))
#print(g.a_star(start, finish_line))
# perguntar ao stor sobre os pesos (se temos de contabilizar as posições entre as coordenadas que percorremos)
# perguntar ao stor como ir para o F mais próximo (e testar todas as posições entre a pos atual e o final)
