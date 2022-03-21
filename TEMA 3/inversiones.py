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

def mergesort(c):
    n = len(c)
    if n <=1:
        return c, 0
    a = mergesort(c[:n//2])
    b = mergesort(c[n//2:])
    l = a[0]
    r = b[0]
    contador = a[1] + b[1]

    res = []
    while len(l) >0 and len(r) >0: 
        if l[0] <= r[0]:
            res.append(l[0])
            l = l[1:]
        else:
            contador += len(l)
            res.append(r[0])
            r = r[1:]
    # Restantes (l o r va a ser [])
    res += l + r
    return res, contador

print(mergesort([1,90,52,26,7,2,46,78,3,7,12,74,26,78]))

Cliente1 = [1, 2, 3, 4, 5, 6, 7, 8]
Cliente2 = [6, 4, 3, 1, 8, 7, 2, 5]
Cliente3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Cliente4 = [7, 13, 2, 19, 10, 4, 9, 20, 1, 5, 15, 17, 6, 18, 3, 14, 16, 8, 12, 11]

print(burbuja(Cliente2))
print(burbuja(Cliente4)[1])
print(mergesort(Cliente2))
print(mergesort(Cliente4)[1])

print(mergesort([9,1,3,4,2,10,6,5,8,7]))
print(mergesort([4,1,7,3,2,9,5]))