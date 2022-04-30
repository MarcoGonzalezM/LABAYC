def indices_bt(min,max,longitud):
    """
    int,int,int --> list(list(int))
    OBJ: Genera todas las listas posibles de longitud dada de índices comprendidos entre el mínimo y máximo dados ordenados ascendentemente
    """
    res = []
    # Caso de partida
    if longitud==1:
        for i in list(range(min,max)):
            res.append([i])
    # Caso general
    else:
        # Dejando de iterar en max+1-longitud excluimos las soluciones que darían una lista de menos índices (no válidas para la solución)
        for i in range(min,max+1-longitud):                 # Coste: nT(n) + 2n2 + 2n + 2
            # Los índices a añadir a la derecha deben ser mayores, o sino no se respeta el orden.
            for j in indices_bt(i+1,max,longitud-1):            # Coste: 2 + T(n) + 2n
                res.append([i]+j)                                   #Coste: 2
    return res                                              # Coste: 1

def subcadenas(cadena,n):
    """
    str, int --> list(str)
    OBJ: Encontrar todas las subcadenas de longitud n de la lista cadena, que respeten el orden de aparición
    PRE: n<=len(cadena)"""
    sol=[]                                      # Coste: 1
    y = len(cadena)                             # Coste: 1
    indices = indices_bt(0,y,n)                 # Coste: 1 + T(0,y,n)
    for l_ind in indices:                       # Coste: n(2n+1)
        subcadena = ''                              # Coste: 1
        for ind in l_ind:                           # Coste: 2n
            subcadena += cadena[ind]                    # Coste: 2
        sol.append(subcadena)                   # Coste: 1
    return sol                                  # Coste: 1

print(subcadenas('1151451',4))

# Coste de indices_bt: nT(n-1) + 2n2 + 2n + 3
# Coste de subcadenas: indices_bt + 2n2 + n + 5 