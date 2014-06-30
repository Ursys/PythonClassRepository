def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    return max(lo,min(x,hi))

print clip(1,2,3) #2
print clip(4,3,7) #4
print clip(3,8,7) #7