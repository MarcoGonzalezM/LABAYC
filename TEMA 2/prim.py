from cmath import inf

def arista_conexa(arista,nodos):
    return arista[0] in nodos or arista[1] in nodos

def menor_arista_conexa(aristas,nodos):
    menor=[0,0,inf]
    for i in range(len(aristas)):
            if aristas[i][2]<menor[2] and arista_conexa(aristas[i], nodos):
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

    #Escoger el primer nodo (según Prim vale cualquiera, escogemos el primero en la lista de nodos)
    nodos_solucion.append(nodos_candidatos[0])

    #En cuanto el árbol contenga todos los nodos, será un árbol generador del grafo
    while nodos_solucion!=nodos_candidatos:

        #Obtener arista mínima y eliminarla de candidatos y añadirla a la solución
        arista = menor_arista_conexa(aristas_candidatos,nodos_solucion)
    
        aristas_candidatos.remove(arista)
        #Comprobar que la arista a añadir no genera ciclo
        if not arista[0] in nodos_solucion or not arista[1] in nodos_solucion:
            if not(arista[0] in nodos_solucion): nodos_solucion.append(arista[0])
            if not(arista[1] in nodos_solucion): nodos_solucion.append(arista[1])
            aristas_solucion.append(arista)

    #Convertir a matriz de adyacencia
    arbol = []
    for i in range(len(nodos_solucion)): 
        lista_aux = []
        for i in range(len(nodos_solucion)):
            lista_aux.append(0)
        arbol.append(lista_aux)
            
    for arista in aristas_solucion:
        arbol[arista[0]][arista[1]]=arista[2]
        arbol[arista[1]][arista[0]]=arista[2]

    return arbol

grafo1=[[0,1,0,5],[1,0,4,5],[0,4,0,2],[5,5,2,0]]
print(prim(grafo1))