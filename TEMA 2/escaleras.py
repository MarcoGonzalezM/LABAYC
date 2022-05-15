def tiempo_min_fundicion(escaleras):
    """
    list -> list
    OBJ: Hallar el tiempo mínimo de fundición entre todas las escaleras.
    """
    tiempo = 0
    while len(escaleras)>1:
        menor1 = escaleras[0]
        for escalera in escaleras:
            if escalera < menor1:
                menor1 = escalera
        escaleras.remove(menor1)
        menor2 = escaleras[0]
        for escalera in escaleras:
            if escalera < menor2:
                menor2 = escalera
        escaleras.remove(menor2)
        tiempo+=menor1+menor2
        escaleras.append(menor1+menor2)
    return tiempo

def tiempo_min_fundicion2(escaleras):
    """
    list -> list
    OBJ: Hallar el tiempo mínimo de fundición entre todas las escaleras.
    """
    tiempo:int = 0
    fundidas = []
    while len(escaleras)+len(fundidas)>1:
        menores = []
        for i in range(2):
            if len(fundidas)>0 and len(escaleras)>0:
                if escaleras[0]<fundidas[0]:
                    menores.append(escaleras.pop(0))
                else: 
                    menores.append(fundidas.pop(0))
            elif len(fundidas)>0:
                menores.append(fundidas.pop(0))
            elif len(escaleras)>0:
                menores.append(escaleras.pop(0))
        fundidas.append(sum(menores))
        tiempo+=fundidas[-1]
    return tiempo

#PROBADORES
escaleras = [2,4,6,7,13,25,1]
escaleras.sort()
print("Tiempo mínimo en fundir todas las escaleras: ",tiempo_min_fundicion2(escaleras))
escaleras1 = [4,24,8,6,9,1,12,35,5]
escaleras1.sort()
print("Tiempo mínimo en fundir todas las escaleras: ",tiempo_min_fundicion2(escaleras1))