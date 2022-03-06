escaleras = [2,4,6,7,13,25,1]

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

print(tiempo)