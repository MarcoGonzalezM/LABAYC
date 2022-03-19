def moneda_falsa(lista):
    """
    list(num)-->bool
    True si la moneda falsa es de mayor peso, False si menor, None si todos los elementos son iguales
    OBJ: Determinar si la moneda falsa de un conjunto es mayor o menor
    PRE: len(lista)>=3
    """
    if (len(lista)==6):
        return moneda_falsa(lista[0:3]) and moneda_falsa(lista[3:6])
    elif (len(lista)==5):    
        return moneda_falsa(lista[0:3]) and moneda_falsa(lista[2:5])
    elif (len(lista)==4):
        return moneda_falsa(lista[0:3]) and moneda_falsa(lista[1:4])
    elif (len(lista)==3):
        if lista[0]<lista[1]:
            if lista[0]==lista[2]:
                return True
            else:
                return False
        elif lista[0]>lista[1]:
            if lista[0]==lista[2]:
                return False
            else:
                return True
        else:
            if lista[0]<lista[2]:
                return True
            elif lista[0]>lista[2]:
                return False
            else:
                return None
    elif (len(lista)>6):
        k = len(lista)//3
        parte1 = lista[0:k]
        parte2 = lista[k:2*k]
        parte3 = lista[2*k:]
        
        a=sum(parte1)
        b=sum(parte2)
        if a==b:
            return moneda_falsa(parte3)
        else:
            return moneda_falsa(parte1+parte2)
        
caso_1 = []
for i in range(27):
    if i ==5:
        caso_1.append(2)
    else:
        caso_1.append(1)

caso_2 = []
for i in range(38):
    if i ==25:
        caso_2.append(1)
    else:
        caso_2.append(2)

print(moneda_falsa(caso_1))
print(moneda_falsa(caso_2))
#print(moneda_falsa([1,2,2,2,2,2,2,2,2,2]))
#print(moneda_falsa([2,2,3,2,2]))