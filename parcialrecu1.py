def recurrencia(n):
    if n == 0:
        return 5
    elif n == 1:
        return 1
    elif n == 2:
        return -1
    else:
        return 3*recurrencia(n-1)-4*recurrencia(n-3)+n**2
    
def formula(n):
    return 4/3*(-1)**n - 25/3*(2)**n +1*n*(2)**n +1/2*n**2+ 9/2*n + 12

for i in range(0,11):
    print(recurrencia(i),formula(i))