def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    newTup = ()
    index = 0
    while index < len(aTup):
        if index % 2 == 0:
            newTup += (aTup[index],)
        index += 1
    return newTup
    
oddTuples((2, 12, 10, 1, 2, 1, 18, 9, 4))