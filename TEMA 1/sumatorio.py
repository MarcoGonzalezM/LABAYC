def sumatorio (n):
    """
    int --> int
    OBJ: calcular el sumatorio de 1 hasta n
    PRE: n>=1
    """
    # Caso de partida: El sumatorio de 1 hasta 1, trivialmente es 1
    if n==1:                        # 1 Comparación
        return 1                    # 1 Devolución
    # Caso general: El sumatorio de 1 hasta n es equivalente a la suma de n más el sumatorio de 1 hasta n - 1
    # Se puede desglosar según la progresión de la suma de los n primeros de la siguiente forma: 
    # 1 + 2 + ... + n-1 + n
    else:
        return n+(sumatorio(n-1))   # 2 + T(n-1)

# T(n) = 3 + T(n-1)