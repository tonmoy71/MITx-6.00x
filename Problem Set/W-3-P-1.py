def evaluatePoly(poly, x) :
    poly = [-12]
    x = 3.7
    i = 0
    res = 0

    for e in poly :
        res = res + e*x**i
        i +=1
    return res
