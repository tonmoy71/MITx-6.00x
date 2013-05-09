## Week 2 Problem 2

balance = 9999999999
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate/12.0

monthlyPayment = 10
initBalance = 1.0

while initBalance > 0 :
    initBalance = balance
    for month in range(1,13) :
        monthlyInterestRate = annualInterestRate/12
        initBalance = (initBalance - monthlyPayment) * (1 + monthlyInterestRate)

    if initBalance < 0 :
        break
    else :
        monthlyPayment += 10
print('Lowest Payment: ' + str(monthlyPayment))
        

        
