def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        i = exp - 1
        result = base
        while i > 0:
            result = result*base
            i -= 1
        return result 
    
print iterPower(2,0)
print iterPower(3,2)
print iterPower(1.5,2)