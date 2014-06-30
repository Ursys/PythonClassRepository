def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    vowels = 'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'
    if char == 'a' or 'A' # or 'e' or 'E' or 'i' or 'I' or 'o' or 'O' or 'u' or 'U'
        return True
    return False
    
print isVowel('a')
print isVowel('O')
print isVowel('A')
print isVowel('J')
print isVowel('e')
print isVowel('b')