def inversiones(preferencias1,preferencias2):
    """
    list(num),list(num)-->int
    
    """

def burbuja(c):
    n = len(c)
    if n <=1:
        return c
    else:
        for i in range(n-1):
            if c[i]>c[i+1]:
                c[i],c[i+1] = c[i+1],c[i]
        return burbuja(c[:-1])+[c[-1]]


def mergesort(c):
    n = len(c)
    if n <=1:
        return c, 0

    # División del problema en las dos mitades de la lista   
    a = mergesort(c[:n//2])
    b = mergesort(c[n//2:])
    l = a[0]
    r = b[0]
    contador = a[1]+b[1]

    res = []
    
    while len(l) >0 and len(r) >0: 
        if l[0] <= r[0]:
            res.append(l[0])
            l = l[1:]
        else:
            contador +=1             #En este caso al añadirse un elemento de la lista derecha, mientras quedaban elementos de la lista izquierda existe una inversión
            res.append(r[0])
            r = r[1:]
    # Restantes (l o r va a ser [])
    res += l + r
    return res, contador

print(burbuja([9,1,3,4,2,10,6,5,8,7]))