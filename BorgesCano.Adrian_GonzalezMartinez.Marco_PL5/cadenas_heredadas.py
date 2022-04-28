def letra_a_indice(letra):
    return ord(letra)-97

def herencia(M_sust, cadena, indice):
    x = cadena[indice]
    y = cadena[indice+1]
    z = M_sust[letra_a_indice(x)][letra_a_indice(y)]
    cadena = cadena[0:indice]+ z + cadena[indice+2:]
    return cadena

def desarrollo_herencia(M_sust, cadena, caracter):
    # Caso de partida
    if len(cadena)==2:
        if herencia(M_sust,cadena,0)==caracter:
            return [[0]]
        else: 
            return []
    #Caso general
    else:
        sol=[]
        for i in range(len(cadena)-1):
            des_herencia = desarrollo_herencia(M_sust,herencia(M_sust,cadena,i),caracter)
            if des_herencia != []:
                for lista_herencia in des_herencia:
                    sol.append([i]+lista_herencia)
    return sol

def explicar_herencia(M_sust,cadena,desarrollo):
    if len(desarrollo)==1:
        return cadena + ' -> ' + herencia(M_sust,cadena,desarrollo[0])
    return cadena + ' -> ' + explicar_herencia(M_sust,herencia(M_sust,cadena,desarrollo[0]),desarrollo[1:])

matriz = [['b','b','a','d'],['c','a','d','a'],['b','a','c','c'],['d','c','d','b']]
des_her = desarrollo_herencia(matriz,'acabada','d')
for i in range(5):
    print(explicar_herencia(matriz,'acabada',des_her[i]))