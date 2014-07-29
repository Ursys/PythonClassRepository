def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    if len(str2) != len(str1):
            return False
    elif len(str1) == 0:
        return True
    elif str1[0] == str2[-1]:
        return semordnilap(str1[1:], str2[0:-1])
    else:
        return False


def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)
    
    
    
    
print semordnilapWrapper("jeb", "be")