# El número de inversiones se puede obtener mediante la ordenación por mergesort, por que al ir ordenando los elementos, 
# cada intercambio ocurre si un elemento con menor valor está situado después de uno con mayor valor. La solución
# implementada utiliza el método de ordenación por mergesort calculando el total de intercambios que ocurren.

def mergesort(c):
    n = len(c) #n + 1
    
    # Caso base (Cuándo ya no se puede dividir más se calculan los problemas pequeños por una aproximación lineal)
    if n <=1:
        return c, 0

    # Caso general
    # División del problema, resolvemos el problema primero para la parte izquierda y derecha de la lista y después lo mezclaremos
    a = mergesort(c[:n//2]) # 2 + T(n/2)
    b = mergesort(c[n//2:]) # 2 + T(n/2)
    l = a[0]
    r = b[0]
    contador = a[1] + b[1]

    res = []
    while len(l)>0 and len(r)>0: # (2n+1) n/2 = max(len(l), len(r))
        if l[0] <= r[0]:
            res.append(l[0])
            l = l[1:]
        else:
            #Si un elemento menor está situado después de uno mayor, hay una inveersión por cada elemento en la lista izquierda.
            contador += len(l) # n · n/2
            res.append(r[0])
            r = r[1:]
    # Restantes (l o r va a ser [])
    res += l + r
    return res, contador

    # Análisis de la recursividad:
    # Según el método maestro
    # T(n) = k * T(n/b) + f(n)              k = 2, b = 2, f(n) = 3/2(n^2), p=2  k<b^p
    # T(n) = 2 · T(n/2) + 3(n^2)/2 => T(n) = O(n^2)

print(mergesort([1,90,52,26,7,2,46,78,3,7,12,74,26,78]))

Cliente1 = [1, 2, 3, 4, 5, 6, 7, 8]
Cliente2 = [6, 4, 3, 1, 8, 7, 2, 5]
Cliente3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Cliente4 = [7, 13, 2, 19, 10, 4, 9, 20, 1, 5, 15, 17, 6, 18, 3, 14, 16, 8, 12, 11]

print(mergesort(Cliente2)[1])
print(mergesort(Cliente4)[1])

print(mergesort([9,1,3,4,2,10,6,5,8,7])[1])
print(mergesort([4,1,7,3,2,9,5])[1])