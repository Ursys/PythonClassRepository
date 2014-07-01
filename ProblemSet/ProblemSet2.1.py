# This code passed the test on the course website

balance = 4768.20  # needs to be only two decimal places
annualInterestRate = 0.1725 
monthlyPaymentRate = 0.04

def annualCreditCardPayment (balance, annualIntrestRate, monthlyPaymentRate):
    monthlyInterestRate = annualInterestRate / 12.0
    month = 0
    totalPaid = 0
    while month < 12:
        prevBalance = balance
        minPayment = monthlyPaymentRate * prevBalance
        month += 1
        prevBalance -= minPayment
        balance = prevBalance + (monthlyInterestRate * prevBalance)
        totalPaid += minPayment
        print ('Month: ' + str(month))
        print ('Minimum monthly payment: ' + str(round(minPayment,2)))
        print ('Remaining balance: ' + str(round(balance,2)))

    print('Total paid: ' + str(round(totalPaid,2)))
    print('Remaining balance: ' + str(round(balance,2)))
annualCreditCardPayment(balance, annualInterestRate, monthlyPaymentRate)
        
    