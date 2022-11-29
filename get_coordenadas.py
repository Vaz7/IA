

filepath = 'Projeto/gigaMap.txt'
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
            tuple = (x,y,caracteres[i])
            nodos.append(tuple)
            x=x+1

        conjunto_nodos.append(nodos)
        nodos = []
        y=y+1

size_conj_nodos = len(conjunto_nodos)
for i in range(size_conj_nodos):
    print(conjunto_nodos[i])
