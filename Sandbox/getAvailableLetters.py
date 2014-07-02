def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    lettersAvailable = 'abcdefghijklmnopqrstuvwxyz'
    for letter in lettersGuessed:
        lettersAvailable = lettersAvailable.replace(letter,'')
    return lettersAvailable


print getAvailableLetters('rstlne')