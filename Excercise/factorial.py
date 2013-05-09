def factL(a) :
    res = 1
    while a > 0 :
        res = res * a
        a -= 1
    return res

def factR(a) :
    
    
    if a == 1 :
        print('Recursive Call on factR(' + str(a) + ')')
        return a
    else :
        print('Recursive Call on factR(' + str(a) + ')')
        return a * factR(a-1)
    


print factR(5)
