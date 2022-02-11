def divisores(n):
    """
    int -> list(int)
    OBJ: calcular los divisores de un número
    """
    if n==1: return [1]
    i=1
    k=n//i
    divisores = []
    while i<k:
        if n%i==0: 
            divisores.append(i)
            if i!=n/i:
                divisores.append(n//i)
        k=n//i
        i+=1
    return divisores

def esprimo(n):
    """
    int -> bool
    OBJ: decir si un número es primo o no
    """
    ldivisores=divisores(n)
    return len(ldivisores)==2 and ldivisores[0]!=ldivisores[1]

def esperf(n):
    """
    int -> bool
    OBJ: decir si un número es perfecto o no
    """
    return sum(divisores(n))==2*n

for j in range(100):
    print(j,divisores(j))
    print(j,esprimo(j))
    print(j,esperf(j))
    