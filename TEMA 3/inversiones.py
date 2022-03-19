def inversiones(preferencias1,preferencias2):
    """
    list(num),list(num)-->int
    
    """

def mergesort(c):
    n = len(c)
    if n <=1:
        return c
    
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
            contador +=1
            res.append(r[0])
            r = r[1:]
    # Restantes (l o r va a ser [])
    res += l + r
    return res, contador