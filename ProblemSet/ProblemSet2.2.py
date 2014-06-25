balance = 
annualInterestRate = 

def MonthlyPaymentCalc(balance, annualInterestRate)
    monthlyPayment = 10
    while balance > 0:
        monthlyInterestRate = annualInterestRate / 12.0
        month = 0
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
            



    print('Lowest Payment: ' + str(LowPay))    