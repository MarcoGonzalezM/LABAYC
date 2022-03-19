# El número de inversiones se puede obtener mediante la ordenación por burbuja, por que al ir ordenando los elementos, 
# cada intercambio ocurre si un elemento con menor valor está situado después de uno con mayor valor. La solución
# implementada utiliza el método de ordenación por burbuja calculando el total de intercambios que ocurren.

def burbuja(c):
    contador = 0
    n = len(c)
    if n <=1:
        return c, contador
    else:
        for i in range(n-1):
            if c[i]>c[i+1]:
                contador+=1
                c[i],c[i+1] = c[i+1],c[i]
        # Reducción del problema: Mediante la ordenación por burbuja, el último elemento de la lista ya queda ordenado
        # por lo que sólo queda ordenar la lista excluyendo el último elemento de la lista
        r = burbuja(c[:-1])
        return r[0]+[c[-1]],r[1]+contador

Cliente1 = [1, 2, 3, 4, 5, 6, 7, 8]
Cliente2 = [6, 4, 3, 1, 8, 7, 2, 5]
Cliente3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Cliente4 = [7, 13, 2, 19, 10, 4, 9, 20, 1, 5, 15, 17, 6, 18, 3, 14, 16, 8, 12, 11]

print(burbuja(Cliente2)[1])
print(burbuja(Cliente4)[1])
#print(burbuja([9,1,3,4,2,10,6,5,8,7]))