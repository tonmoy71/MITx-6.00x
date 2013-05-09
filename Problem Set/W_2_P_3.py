balance = 9999999999
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate/12.0

low = balance / 12
up = (balance * (1 + monthlyInterestRate)**12) / 12

monthlyPayment = (low + up) / 2
initBalance = 1.0

while abs(initBalance) >= 0.01 :
    initBalance = balance
    for month in range(1,13) :
        initBalance = (initBalance - monthlyPayment) * (1 + monthlyInterestRate)

    if initBalance >= 0.01 :
        low = monthlyPayment
    else :
        up = monthlyPayment
    monthlyPayment = (low+up) / 2
print('Lowest Payment: ' + str(round(monthlyPayment, 2)))

