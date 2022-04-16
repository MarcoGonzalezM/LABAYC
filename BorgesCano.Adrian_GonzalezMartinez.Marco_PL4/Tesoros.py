
#tesoro = [peso, valor]

def min_difference (list):
    """
    list(elem) -> int
    OBJ: Devolver el valor mínimo que sea mayor que 0 en una lista
    https://www.geeksforgeeks.org/find-minimum-difference-pair/
    """
    arr = sorted(list)

    # Initialize difference as infinite
    diff = 10**20
 
    # Find the min diff by comparing adjacent
    # pairs in sorted array
    for i in range(len(list)-1):
        if 0 < arr[i+1][0] - arr[i][0] < diff:
            diff = arr[i+1][0] - arr[i][0]
 
    # Return min diff
    return diff


def mochila(tesoros,cap_alforja1, cap_alforja2):
    # Generar los valores de capacidad de las "submochilas"
    min_dif = min_difference(tesoros)
    minimo = min(tesoros)[0]
    tam_mochilas1 = []
    tam_mochilas2 = []
    # k Va a ser la diferencia del tamaño de las distintas "submochilas" del problema
    # La calculamos a partir del mínimo número entre la mínima diferencia de los pesos de los tesoros y el peso mínimo
    k = min(min_dif,minimo)
    i = 1
    while k*i <= cap_alforja1:
        tam_mochilas1.append(k*i)
        i+=1
    i = 1
    while k*i <= cap_alforja2:
        tam_mochilas2.append(k*i)
        i+=1


    mochila1 = []
    mochila2 = []
    for tesoro in tesoros:
        for i in range(len(tam_mochilas1)+len(tam_mochilas2)-1):
            if tesoro[0]<:



lista_tesoros = [[1,200],[1,200],[2,10],[2,10]]

print(mochila(lista_tesoros,3,3))