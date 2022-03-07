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

#PROBADORES
escaleras = [2,4,6,7,13,25,1]
escaleras1 = [4,24,8,6,9,1,12,35,5]
print("Tiempo mínimo en fundir todas las escaleras: ",tiempo_min_fundicion(escaleras))
print("Tiempo mínimo en fundir todas las escaleras: ",tiempo_min_fundicion(escaleras1))