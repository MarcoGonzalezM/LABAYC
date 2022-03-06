from cmath import inf

def menor_arista(aristas):
    menor=inf
    for i in range(len(aristas)):
            if aristas[i][2]<menor:
                menor = aristas[i]
    return menor

def prim (grafo):
    #Interpretar candidatos Convertimos el grafo a una lista de nodos y una lista de aristas
    nodos_candidatos = []
    aristas_candidatos = []
    for i in range(len(grafo)):
        nodos_candidatos.append(i)
        for j in range(i):
            if grafo[i][j]>0:
                aristas_candidatos.append([i,j,grafo[i][j]])

    nodos_solucion = []
    aristas_solucion = []

    #Obtener arista mínima, eliminarla de candidatos y añadirla a la solución
    arista = menor_arista(aristas_candidatos)
    aristas_solucion.append(arista)
    aristas_candidatos.remove(arista)

    #En cuanto el árbol contenga todos los nodos, será un árbol generador del grafo
    while nodos_solucion!=nodos_candidatos:
        #Obtener arista mínima
        

    #recorrer el grafo en busca de la menor arista
    x, y= menor_arista(grafo)
    #borrar arista
    peso = grafo[x][y]
    grafo[x][y]=0
    grafo[y][x]=0
    #comprobar conexo a solución y no ciclo
    if x in nodos_solucion ^ y in nodos_solucion:
        if not(x in nodos_solucion): nodos_solucion.append(x)
        if not(y in nodos_solucion): nodos_solucion.append(y)
        aristas_solucion.append([x,y,peso])

grafo1=[[0,4],[4,0]]
print(range(len(grafo1)))