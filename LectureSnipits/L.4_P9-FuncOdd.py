def odd(x):
    '''
    x: int or float.

    returns: True if x is odd, False otherwise
    '''
    return 0.0 != x % 2

print odd(0.2) #False
print odd(5.321) #True
print odd(144) # False
print odd(167) # True