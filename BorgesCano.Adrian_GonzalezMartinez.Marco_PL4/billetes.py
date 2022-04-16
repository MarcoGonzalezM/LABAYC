def combinacion(a,b):
    # Si uno de los candidatos a combinar no ofrece solución, la combinación tampoco.
    if a==0 or b==0:
        return 0
    c = []
    for i in range(len(a)):
        c.append([a[i][0],a[i][1]+b[i][1]])
    return c

def num_monedas(candidato):
    tot= 0
    for i in range(len(candidato)):
        tot+=candidato[i][1]
    return tot

def mejor_candidato(candidatos,c):
    # Descartar candidatos no válidos, aquellos que no ofrezcan solución (0s) o aquellos que usen más monedas de las que se dispone
    i = 0
    while i < len(candidatos):
        valido = True
        if candidatos[i]==0:
            valido=False
        else:
            for j in range(len(c)):
                if candidatos[i][j][1]>c[j]:
                    valido=False
        if not(valido):
            del(candidatos[i])
        else:
            i+=1
    #Comparar los dos primeros candidatos hasta que sólo quede el que utilice menos monedas
    while len(candidatos)>1:
        if num_monedas(candidatos[1])>=num_monedas(candidatos[0]):
            del(candidatos[1])
        else:
            del(candidatos[0])
    if len(candidatos)>0:
        return candidatos[0]
    else:
        return 0

def billetes(d, v, c):
    """
    int, list(int), list(int) --> bool, string
    """
    cantidades_a_devolver = list(range(1,d+1)) # Se crea una lista de aquellas cantidades para las que se va a buscar una solución al problema
    
    # Inicialización de la tabla de la solución
    sol = []
    for i in range(len(v)):
        sol_fil = []
        for j in range(len(cantidades_a_devolver)):
            sol_fil.append(0)
        sol.append(sol_fil)
    
    for i in range(len(v)):
        for j in range(len(cantidades_a_devolver)):
            if v[i]==cantidades_a_devolver[j]:
                # Usar 1 billete del valor de billetes nuevo que se está evaluando, siempre será la solución óptima para devolver esa misma cantidad
                # Sea un ejemplo: devolver 5 Euros con billetes de 5 Euros -> Se usa 1 Billete de 5 Euros
                celda=[]
                for val in v:
                    celda.append([val,0])
                celda[i]=[v[i],1]
                sol[i][j]=celda
            else:
                # Candidatos es la lista de opciones a elegir para la nueva celda que se está evaluando
                candidatos = []
                # Añadir a los candidatos la solución para devolver la cantidad requerida con las monedas anteriores
                candidatos.append(sol[i-1][j])
                # Añadir a los candidatos las combinaciones de soluciones cuya cantidad a devolver sumen la cantidad requerida
                for k in range(j//2+1):
                    candidatos.append(combinacion(sol[i][k],sol[i][j-k-1]))
                    sol[i][j]=mejor_candidato(candidatos,c)

    # print(sol) # Descomentar para visualizar la tabla completa
    return sol[-1][-1]

print(billetes(11,[1,3,5],[15,5,5]))
print(billetes(11,[1,3,5],[3,5,2]))
print(billetes(201,[1,20,50,100],[1,10,5,1]))