# El número de inversiones se puede obtener mediante la ordenación por burbuja, por que al ir ordenando los elementos, 
# cada intercambio ocurre si un elemento con menor valor está situado después de uno con mayor valor. La solución
# implementada utiliza el método de ordenación por burbuja calculando el total de intercambios que ocurren.

def burbuja(c):                             #Operación: Coste
    contador = 0                            #Asignación: 1
    n = len(c)                              #Asignación y función len(): n+1
    if n <=1:                               #Condicional y comparación: 1
        return c, contador                  #Retorno: 2
    else:
        for i in range(n-1):                #Bucle y resta: 1+n*CosteBucle
            if c[i]>c[i+1]:                 #Comparación y suma: 2  
                contador+=1                 #Asignación y suma: 2
                c[i],c[i+1] = c[i+1],c[i]   #Asignación y sumas: 4
        # Reducción del problema: Mediante la ordenación por burbuja, el último elemento de la lista ya queda ordenado
        # por lo que sólo queda ordenar la lista excluyendo el último elemento de la lista
        r = burbuja(c[:-1])                 #Asignación y llamada recursiva: 1+T(n-1)
        return r[0]+[c[-1]],r[1]+contador   #Retorno y sumas: 4

        #Análisis de la recursividad:
        # 1+n+1+1+max(2,1+n*max(2+2+4,0)+1+T(n-1)+4) = 3+n+max(2,6+n*max(8,0)+T(n-1)) = 
        # = 3+n+6+8n+T(n-1) = 9+9n+T(n-1)
        # T(n) = 9+9n + 9+9(n-1) + 9+9(n-2) + 9+9(n-3) + ...
        #Se puede apreciar que la expresión recursiva representa el sumatorio desde 1 hasta n,
        # cuyo coste es de O(n^2).  


Cliente1 = [1, 2, 3, 4, 5, 6, 7, 8]
Cliente2 = [6, 4, 3, 1, 8, 7, 2, 5]
Cliente3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Cliente4 = [7, 13, 2, 19, 10, 4, 9, 20, 1, 5, 15, 17, 6, 18, 3, 14, 16, 8, 12, 11]

print(burbuja(Cliente2)[1])
print(burbuja(Cliente4)[1])
#print(burbuja([9,1,3,4,2,10,6,5,8,7]))