def recurrencia(n):
    if n == 1:
        return 1
    else:
        return 2 * recurrencia(n - 1)+1
    
def formula(n):
    return 2**n - 1

for i in range(1,11):
    print(recurrencia(i),formula(i))