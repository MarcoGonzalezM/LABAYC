def moneda_falsa(lista):
    """
    list(num)-->bool
    True si la moneda falsa es de mayor peso, False si menor, None si todos los elementos son iguales
    OBJ: Determinar si la moneda falsa de un conjunto es mayor o menor
    PRE: len(lista)>=3
    """
    # Casos base (Cuándo ya no se puede dividir más se calculan los problemas pequeños por una aproximación lineal)
    n = len(lista)                                                       
    if (n==6):
        return moneda_falsa(lista[0:3]) and moneda_falsa(lista[3:6])
    elif (n==5):
        return moneda_falsa(lista[0:3]) and moneda_falsa(lista[2:5])
    elif (n==4):
        return moneda_falsa(lista[0:3]) and moneda_falsa(lista[1:4])
    elif (n==3):
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
    #Caso general
    elif (n>6):
        # División del problema en 3 partes (Debido a que las dos partes a introducir en la báscula deben tener el mismo número de elementos)
        k = n//3                        # División entera y Asignación: 2
        parte1 = lista[0:k]             # Asignación: 1
        parte2 = lista[k:2*k]           # Multiplicación y Asignación: 2
        parte3 = lista[2*k:]            # Multiplicación y Asignación: 2
        
        a=sum(parte1)                   # Asignación y Función sum: 1+n
        b=sum(parte2)                   # Asignación y Función sum: 1+n
        # Si las dos primeras parte estaban en equilibrio, la moneda estará en la tercera parte
        if a==b:                        # Comparación: 1
            return moneda_falsa(parte3) # Función recursiva: T(n//3)
        # Si por el contrario, estaban desequilibradas, estará en la primera o segunda parte
        else:
            return moneda_falsa(parte1+parte2) # Función recursiva: T(2*n//3)

    #Análisis de la recursividad:
    #T(n) = k * T(n/b) + f(n) = 2 * T(n/n//3) + f(n)
        
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