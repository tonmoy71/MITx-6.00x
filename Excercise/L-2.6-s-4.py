x = int(raw_input('Enter a number '))

if x%2 == 0:
    if(x%3 == 0):
        print('Divisible by 2 and 3')
    else:
        print('Divisible by 2 but not by 3')
elif x%3 == 0:
    print('Divisible by 3')
else:
    print('Not divisible by 2 or 3')
    



