##x = 5
##p = 3
##result = 1
##
##for turn in range(p) :
##    print('iteration: ' + str(turn) + ' current result: ' + str(result))
##    result = result * x

x = 10
y = 15

def max(x,y):
    print('Inside function : x = ' + str(x))
    print('Inside function : y = ' + str(y))
    if x > y :
        return x
    else :
        return y
     
z = max(3,4)
print('Maximum is : z = ' + str(z))
print('Outside function : x = ' + str(x))
print('Outside function : y = ' + str(y))
