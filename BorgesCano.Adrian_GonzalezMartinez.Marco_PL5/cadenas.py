def indices_bt(min,max,longitud):
    """
    int,int,int --> list(list(int))
    OBJ: Genera todas las listas posibles de longitud dada de índices comprendidos entre el mínimo y máximo dados ordenados ascendentemente
    """
    res = []
    if longitud==1:
        for i in list(range(min,max)):
            res.append([i])
    else:
        # Dejando de iterar en max+1-longitud excluimos las soluciones que darían una lista de menos índices (no válidas para la solución)
        for i in range(min,max+1-longitud):
            # Los índices a añadir a la derecha deben ser mayores, o sino no se respeta el orden.
            for j in indices_bt(i+1,max,longitud-1):
                res.append([i]+j)
    return res

def subcadenas(cadena,n):
    """
    str, int --> list(str)
    OBJ: Encontrar todas las subcadenas de longitud n de la lista cadena, que respeten el orden de aparición
    PRE: n<=len(cadena)"""
    sol=[]
    y = len(cadena)
    indices = indices_bt(0,y,n)
    for l_ind in indices:
        subcadena = ''
        for ind in l_ind:
            subcadena += cadena[ind]
        sol.append(subcadena)
    return sol

print(subcadenas('1151451',4))