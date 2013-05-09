import random
def genEven():
    '''
    Generates a random number x, where 0 <= x < 100
    '''
    # Your code here
    randEven = []
    for i in range(100):
        if (i%2 == 0):
            randEven.append(i)
    return random.choice(randEven)
