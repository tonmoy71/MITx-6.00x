# A simple while loop

x = int(raw_input('Enter number : '))
ans = 0
itersLeft = x

while(itersLeft != 0):
    ans = ans + x
    itersLeft = itersLeft - 1
print(str(x) + ' * ' + str(x) + ' = ' + str(ans))
