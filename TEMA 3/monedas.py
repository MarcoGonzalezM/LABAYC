def bascula (lista1,lista2):
    """
    list(num),list(num)-->bool
    OBJ: determinar si el peso de ambos fragmentos es igual o no
    """
    return sum(lista1)==sum(lista2) #O(n)

def moneda_falsa(lista):
    """
    list(num)-->bool
    True si la moneda falsa es de mayor peso, false si menor
    OBJ: Determinar si la moneda falsa de un conjunto es mayor o menor
    """
    k = len(lista)//2
    parte1 = lista[0:k]
    parte2 = lista[k:2*k]
    parte3 = lista[2*k:]
    
    a=sum(parte1)
    b=sum(parte2)
    if a==b:
        return True
    elif a<b:
        return moneda_falsa(parte1+parte3)
    else:
        return moneda_falsa(parte2+parte3)


    
print(moneda_falsa([1,2,2,2,2,2,2,2,2,2]))