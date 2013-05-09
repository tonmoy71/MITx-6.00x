def isIn(a, s) :
    '''
    a is a character, or, singleton string.
    s is a string, sorted in alphabetical order.
    '''
    if len(s) == 0 :
        return False
    elif len(s) == 1 :
        return a == s
    else :
        test = s[len(s)/2]
        if test == a :
            return true
        elif a < test :
            return isIn(a, s[:len(s)/2])
        else :
            return isIn(a, s[len(s)/2+1])
                    
print isIn('c', 'abc')
