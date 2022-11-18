from grafo import Graph
from nodos import Node

mapElem = {}
g = Graph()

def parseMapa():
    i = 0
    with open('mapa.txt') as f:
        contents = f.readlines()
        for content in contents:
            content = content.strip('\n')
            mapElem[i] = content.split(" ")
            i += 1
    print('Linhas: ' + str(i) + '\nColunas: ' + str(len(mapElem[0])))

def setUpGraph():
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

def addToGraph(elem1,coord1,elem2,coord2):
    if elem1 == 'P':
        global start
        start = coord1
    if elem2 == 'X':
        g.add_edge(elem1, coord1, elem2, coord2, 25)
    else:
        g.add_edge(elem1, coord1, elem2, coord2, 1)


def printGraph():
    lista = g.m_nodes
    for nodo in lista:
        coord = nodo.getCoord()
        print('Nodo ' + str(coord) + ' conhece:')
        print(g.m_graph[coord])

parseMapa()
setUpGraph()
printGraph()
print(start)
g.desenha()
print(g.procura_DFS(start,(35,10),path=[],visited=set()))