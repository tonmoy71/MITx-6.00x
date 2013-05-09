import math

def isPrime(n):
    if type(n)!= int:
        raise TypeError()
    if n <= 0:
        raise ValueError()
    if n==2:
        return True
    elif n<2:
        return False
    else:
        for i in range(2, int(math.sqrt(n) + 1)):
            if n%i==0:
                return False
        return True
