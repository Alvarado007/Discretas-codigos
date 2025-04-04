def recurrencia(n):
    if n == 0:
        return 5
    else:
        return 3* recurrencia(n - 1) + 5*(7)**n
    
def formula(n):
    return -15/4*(3)**n + 35/4*(7)**n

for i in range(0,11):
    print(recurrencia(i),formula(i))