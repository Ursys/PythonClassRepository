def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    index = 0
    vowels = 'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'
    while index < len(vowels):
        if char == vowels[index]:
            return True
        index += 1
    return False
    
print isVowel('a')
print isVowel('O')
print isVowel('A')
print isVowel('J')
print isVowel('e')
print isVowel('b')