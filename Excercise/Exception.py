import sys

try:
    f = open('grades.txt')
    p = open('score.txt')
    
except IOError,e:
    print('Can\'t open file: ' + str(e))
    
else:
    pass
    #p = open('score.txt')
    
##except ArithmeticError,e:
##    raise ValueError('Oops! Bug in grade calculation: ' + str(e))
##except NameError, e:
##    print('Can\'t find the name of the variable: ' + str(e))

finally:
    print('Executing finally block')

def divide(x,y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('Division by Zero!')
    except TypeError:
        print('Type not supported')
    else:
        print('Result is: ' + str(result))
    finally:
        print('Executing finally clause')
