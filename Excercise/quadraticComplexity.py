def isSubset(L1, L2) :      ## if L1 is a subset of L2, print True, otherwise False
    for e1 in L1 :
        matched = False
        for e2 in L2 :
            if e1 == e2 :
                matched = True
                break
        if not matched :
            return False
    return True

## isSubset([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7, 8])

def intersect(L1, L2) :
    tmp = []
    for e1 in L1 :
        for e2 in L2 :
            if e1 == e2 :
                tmp.append(e1)
    res = []
    for e in tmp :
        if not(e in res) :
            res.append(e)
    return res

print intersect([1, 1, 2], [1, 2, 3, 4])
