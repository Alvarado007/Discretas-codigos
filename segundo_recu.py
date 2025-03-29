def recurrencia(n):
    if n == 0:
        return 2
    elif n == 1:
        return 5
    else:
        return -2 * recurrencia(n - 1)+ 15*recurrencia(n - 2)

def formula(n):
    return 1/8*(-5)**n +15/8*(3)**n

for i in range(1,11):
    print(recurrencia(i),formula(i))