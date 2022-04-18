def torneo(n,vc,d):
    """
    int, list(int), int --> double
    OBJ: Devuelve la cantidad que ganaría Javi Potter en caso de que ganen los Grifos a partir de la cantidad apostada d,
    los valores de calidad vc, y el número de partidos necesarios para ganar
    """
    p = []
    for v in vc:
        p.append(v/100)
    
    tabla = []
    for i in range(n+1):
        tabla_i = []
        for j in range(n+1):
            tabla_j = []
            for k in range(n+1):
                tabla_k=[]
                for l in range(n+1):
                    tabla_k.append(0)
                tabla_j.append(tabla_k)
            tabla_i.append(tabla_j)
        tabla.append(tabla_i)

    # La probabilidad de que en un momento dado del torneo (Al comienzo)
    # todos los equipos tengan 0 victorias es de 1 ó 100%
    tabla[0][0][0][0] = 1

    for i in range(n+1):
        for j in range(n+1):
            for k in range(n+1):
                for l in range(n+1):
                    if i<n and j<n and k<n and l<n:
                        tabla[i][j][k][l+1] = p[3]*tabla[i][j][k][l]
                        tabla[i][j][k+1][l] = p[2]*tabla[i][j][k][l]
                        tabla[i][j+1][k][l] = p[1]*tabla[i][j][k][l]
                        tabla[i+1][j][k][l] = p[0]*tabla[i][j][k][l]

    acumulador = 0
    for j in range(n+1):
        for k in range(n+1):
            for l in range(n+1):
                acumulador += tabla[n][j][k][l]

    return d/acumulador
    
print(torneo(2,[40,20,15,25],10))