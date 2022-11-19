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

# Tenho de adicionar cenas ao nodo para conseguir usar as fórmulas da posição/velocidade/aceleração que estão no enunciado
parseMapa()
setUpGraphNotInformed()
#setUpGraphInformed()
printGraph()
print(start)
g.desenha()
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
print(g.procura_BFS(start,(9,3)))