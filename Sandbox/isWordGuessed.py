def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    isInGuess = 0
    for letter in secretWord:
        isInGuess = lettersGuessed.count(letter) 
        if isInGuess == 0:
            return False
    return True

sW = 'purified'
lG = 'p, r, f, e, u, i, d'
print isWordGuessed(sW,lG)