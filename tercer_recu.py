import math
from math import sqrt
def recurrencia(n):
    if n==0:
        return 1
    elif n==1:
        return 4
    else:
        return recurrencia(n-1) + recurrencia(n-2)
    
def formula(n):
    alpha = (1 + sqrt(5)) / 2
    beta = (1 - sqrt(5)) / 2
    A = 2.06524758424986          
    B = -1.06524758424986
    return round(A * alpha**n + B * beta**n)

def recurrenciacompleta(n):
    if n==0:
        return 1
    else:
        return recurrenciacompleta(n-1) + formula(n-1)

for i in range(0,11):
    print(recurrenciacompleta(i))