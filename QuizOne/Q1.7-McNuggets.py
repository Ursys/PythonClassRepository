def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    nugCombos = [6, 9, 15, 20, 26, 29, 35]
    if n < 6:
        return False
    for num in nugCombos:
        if n % num == 0:
            return True
    return False 
    

print McNuggets(236)
print McNuggets(70)
print McNuggets(10)
print McNuggets(16)
print McNuggets(2)
print McNuggets(10000)
print McNuggets(31)
print McNuggets(18)