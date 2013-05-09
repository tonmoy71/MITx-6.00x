def search(L, e) :
    """Assumes L is a ist, the elements of which are in ascending order.
    Returns True if e is in L and otherwise."""
    
    def bSearch(L, e, low, high) :
        
        if high == low :
            
            return L[low] == e
        mid = (low+high)/2
        if L[mid] == e :
            
            return True
        elif L[mid] > e :
            if low  == mid :
                return False
            else :
                return bSearch(L, e, low, mid-1)
        else :
            return bSearch(L, e, mid+1, high)

    if len(L) == 0 :
        return False
    else :
        return bSearch(L, e, 0, len(L) - 1)


list = range(0, 10)
e = 95
print (search(list, e))
