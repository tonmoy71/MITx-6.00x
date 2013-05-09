## Week 2 Problem 1

## Need to initialize these variables first : 

## balance 
## annualInterestRate 
## monthlyPaymentRate 

totalPaid = 0

for month in range(1,13):
    
    monthlyInterestRate = annualInterestRate/12
    monthlyPayment = balance * monthlyPaymentRate
    interest = (balance - monthlyPayment) * monthlyInterestRate
    balance = balance - monthlyPayment + interest
    totalPaid += monthlyPayment
    
    print('Month: ' + str(month))
    print('Minimum monthly payment: ' + str(round(monthlyPayment, 2)))
    print('Remaining balance: ' + str(round(balance, 2)))

print('Total paid: ' + str(round(totalPaid, 2)))
print('Remaining balance: ' + str(round(balance, 2)))


  
    
    
