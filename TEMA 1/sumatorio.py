def sumatorio (n):
    """
    int --> int
    OBJ: calcular el sumatorio de 1 hasta n
    PRE: n>=1
    """
    if n==1:                        # 1 Comparación
        return 1                    # 1 Devolución
    else:
        return n+(sumatorio(n-1))   # 2 + T(n-1)

# T(n) = 3 + T(n-1)