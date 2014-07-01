balance = 1661.32
annualInterestRate = 0.2199

epsilon = 0.0001
LowBound = balance/12.0
HighBound = (balance * (1 + annualInterestRate/12.0)**12)/12.0
minPayment = (HighBound + LowBound)/2.0
testPayment = 0
while abs(minPayment-testPayment) > epsilon:
    testBalance = balance
    month = 0
    while (month < 12):
        month += 1
        testBalance = round((testBalance-minPayment)*(1+annualInterestRate/12),2)
        
    if testBalance < 0:
        HighBound = minPayment
    else:
        LowBound = minPayment
    testPayment = minPayment
    minPayment = round((HighBound + LowBound)/2.0,2)
print('Lowest Payment: ' + str(minPayment))