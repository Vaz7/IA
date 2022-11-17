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

    for line in mapElem:
        for coiso in range(line):
            print(str((x,y)))
            if x-1 >= 0 and y+1 <= len(mapElem)-1:
                addToGraph(mapElem[y][x],(x,y),mapElem[y+1][x-1],(x-1,y+1))
            if x-1 >= 0 and y-1 >= 0:
                addToGraph(mapElem[y][x],(x,y),mapElem[y-1][x-1],(x-1,y-1))
            if x+1 <= len(mapElem[0])-1 and y+1 <= len(mapElem)-1:
                addToGraph(mapElem[y][x],(x,y),mapElem[y+1][x+1],(x+1,y+1))
            if x+1 <= len(mapElem[0])-1 and y-1 >= 0:
                addToGraph(mapElem[y][x],(x,y),mapElem[y-1][x+1], (x+1,y-1))
            if x+1 <= len(mapElem[0])-1:
                addToGraph(mapElem[y][x],(x,y),mapElem[y][x+1],(x+1,y))
                print('Cheguei aqui +x' + str((x,y)))
            if x-1 >= 0:
                addToGraph(mapElem[y][x],(x,y),mapElem[y][x-1],(x-1,y))
                print('Cheguei aqui -x' + str((x,y)))
            if y+1 <= len(mapElem)-1:
                addToGraph(mapElem[y][x],(x,y),mapElem[y+1][x],(x,y+1))
                print('Cheguei aqui +y' + str((x,y)))
            if y-1 >= 0:
                addToGraph(mapElem[y][x],(x,y),mapElem[y-1][x],(x,y-1))
                print('Cheguei aqui -y:' + str((x,y)))
            x += 1
        y += 1

def addToGraph(elem1,coord1,elem2,coord2):
    if elem2 == 'X':
        g.add_edge(elem1, coord1, elem2, coord2, 25)
    else:
        g.add_edge(elem1, coord1, elem2, coord2, 1)


def printGraph():
    lista = g.m_nodes
    for nodo in lista:
        coord = nodo.getCoord()
        print('Nodo ' + str(coord) + ' conhece:')
        for (adjacente, coord2, peso) in g.m_graph[str(coord)]:
            print('Sou o nodo:' + adjacente + ' estou na coord: ' + (coord2) + ' peso: ' + str(peso))

parseMapa()
setUpGraph()
printGraph()