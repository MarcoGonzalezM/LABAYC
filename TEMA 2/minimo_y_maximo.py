def minimo_y_maximo(candidatos):
    """
    list(COMPARABLE)--> COMPARABLE,COMPARABLE
    OBJ: obtener el minimo y el máximo de una lista
    """
    cand_max = []
    cand_min = []
    while (len(candidatos)>=2):
        if candidatos[0]>candidatos[1]:
            cand_max.append(candidatos[0])
            del(candidatos[0])
            cand_min.append(candidatos[1])
            del(candidatos[1])
        else:
            cand_max.append(candidatos[1])
            del(candidatos[1])
            cand_min.append(candidatos[0])
            del(candidatos[0])
    while(len(cand_max)>1):
        if (cand_max[1]>cand_max[0]):
            del(cand_max[0])
        else:
            del(cand_max[1])
    while(len(cand_min)>1):
        if (cand_min[1]<cand_min[0]):
            del(cand_min[0])
        else:
            del(cand_min[1])
    if (len(candidatos)>0):
        if candidatos[0]<cand_min[0]:
            return (candidatos[0],cand_max[0])
        elif candidatos[0]>cand_max:
            return (cand_min[0],candidatos[0])
    return (cand_min[0],cand_max[0])
    

#PROBADORES
lista = [3,4,54,5,7,2,8,6]
lista1 = [34,10,4,8,16,23,23,2,1,3,3,9,10,64,0,35,19,38]
(n,m) = minimo_y_maximo(lista1)
print(f"Mínimo: {minimo_y_maximo(lista1)[0]} Máximo:{minimo_y_maximo(lista1)[1]}")