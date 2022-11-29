import math

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
    print('Linhas: ' + str(i) + '\nColunas: ' + str(len(mapElem[0])))

# Função que inicializa o grafo para uma procura não informada
def setUpGraphNotInformed():
    y = 0
    x = 0
    columns = len(mapElem[0])
    rows = len(mapElem)
    print('Rows: ' + str(rows) + ' Columns: ' + str(columns))

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
    print('Rows: ' + str(rows) + ' Columns: ' + str(columns))

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
    else:
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
#setUpGraphNotInformed()
setUpGraphInformed()
setUpHeuristica()
printGraph()
print(start)
print(finish_line)
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

#print((path,low))
#print(g.procura_BFS(start,finish_line))
print(g.a_star(start, finish_line))
# perguntar ao stor sobre os pesos (se temos de contabilizar as posições entre as coordenadas que percorremos)
# perguntar ao stor como ir para o F mais próximo (e testar todas as posições entre a pos atual e o final)
