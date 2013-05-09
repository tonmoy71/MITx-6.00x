x = float(raw_input('Enter a number '))
p = int(raw_input('Enter an integer power '))

result = 1

for turn in range(p):
    print('iteration: ' +str(turn) + ' current result: ' + str(result))
    result = result * x
print('iteration: ' +str(turn+1) + ' current result: ' + str(result))


def iterativePower(x,p) :
    result = 1
    for turn in range(p):
        print('iteration: ' +str(turn) + ' current result: ' + str(result))
        result = result * x
    print('iteration: ' +str(turn+1) + ' current result: ' + str(result))
    return result
z = iterativePower(3, 5)
print(str(z))
