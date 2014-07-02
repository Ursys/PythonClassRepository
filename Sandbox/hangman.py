def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    numGuess = 8
    lettersGuessed = ''
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.'
    while numGuess > 0:
        print '_' * 13
        print 'You have ' + str(numGuess) + ' guesses left.'
        print 'Available letters: ' + str(getAvailableLetters(lettersGuessed))
        userGuess = raw_input('Please guess a letter: ')
        if lettersGuessed.find(userGuess) > -1:
            print 'Oops! You\'ve already guessed that letter: ' + str(getGuessedWord(secretWord, lettersGuessed))
        elif secretWord.find(userGuess) == -1:
            lettersGuessed += userGuess
            print 'Oops! That letter is not in my word: ' + str(getGuessedWord(secretWord, lettersGuessed))
            numGuess -= 1
        else:
            lettersGuessed += userGuess
            print 'Good guess: ' + str(getGuessedWord(secretWord, lettersGuessed))
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print 'Congratulations, you won!'
    print 'Sorry, you ran out of guesses. The word was else.'