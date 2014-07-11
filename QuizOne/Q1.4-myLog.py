# This code passed the test on the course website

def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    ans = 0
    while True:
        if b**ans > x:
            return ans - 1
        elif b**ans == x:
            return ans
        else:
            ans += 1

print myLog(27,3)
print myLog(26,3)
print myLog(28,3)
print myLog(4,16)
