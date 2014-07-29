def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    midCharIndex = len(aStr) / 2
    if midCharIndex == 0:
        return False
    elif aStr[midCharIndex] == char:
        return True
    elif aStr[midCharIndex] < char:
        return isIn(char, aStr[midCharIndex:])
    else:
        return isIn(char, aStr[:midCharIndex])