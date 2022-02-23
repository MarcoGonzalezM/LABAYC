'''EJEMPLO 2'''
def m(x:list):                  # T(n) = T(n/2) + n^2 + n + 3
    n = len(x)                  # 1
    
    if n <= 1:                  # 1
        return x                # 1
    
    y = [ 0 for _ in x ]        # n
    
    for i in range(n):          # n * n * 1
        for j in range(n):      # n * 1
            y[i] += x[j]        # 1
    
    z = m( y[:n // 2] )         # T(n/2)
    
    return z

# T(n) = T(n/2) + n^2 + n + 3
# n = 2^m
# T(2^m) =  T(2^(m-1)) + 2^2m + 2^m + 3
# x^m - x^(m-1) = 2^2m + 2^m + 3 (Ec. característica)
# x^(m-1)·(x-1) = 0 (Ec. homogénea)
# 2^2m + 2^m + 3 = 0 (Ec. no homogénea)
# 4^m(m^0)+2^m(m^0)+1^m(3·m^0)
# (x-1)^2 · (x-4) · (x-2)
# (1^m·m^0·c1)+(1^m·m^1·c2)+(4^m·m^0·c3)+(2^m·m^0·c4)
# c1+c2m+4^m·c3+2^m·c4
# c1 + c2 log2(n) + 4^(log2(n))·c3 + 2^(log2(n))·c4
# c1 + c2 log2(n) + n^2·c3 + n·c4 -> O(n^2)
