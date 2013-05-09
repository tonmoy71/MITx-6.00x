def findRoot1(x, power, epsilon):

    """
    We can not calculate when the number is negative and  the power is even 
    """

    if x < 0 and power%2 == 0 :
        print('Can\'t calculate')
        return None
        
    low = min(-1, x)
    high = max(1, x)
    print('Initial low value : ' + str(low))
    print('Initial high value : ' +str(high))
    ans = (high + low)/2.0
    
    while (abs(ans**power - x ) > epsilon) :
        print('ans : ' + str(ans))
        if ans ** power < x :
            low = ans
            print('low : ' + str(low))
        else :
            high = ans
            print('high : ' + str(high))
        ans = (high + low) / 2.0
    return ans


