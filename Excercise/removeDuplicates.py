def removeDups(L1, L2) :
    for e1 in L1 :
        if e1 in L2 :
            L1.remove(e1)
L1 = [1,2,3,4,5,6,7]
L2 = [1,3,5,7]
