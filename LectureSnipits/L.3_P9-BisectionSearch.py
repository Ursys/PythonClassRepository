guess = 50
low = 0
high = 100

print("Please think of a number between 0 and 100! ")

while True:
    print('Is your secret number ' + str(guess) + ' ?')
    userInput = raw_input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly. ')
    if userInput == 'c':
        print('Game over. Your secret number was: ' + str(guess))
        break
    elif userInput == 'l':
        low = guess
        guess = (guess + high) / 2
    elif userInput == 'h':
        high = guess
        guess = (low + guess) / 2
    else:
        print('I\'m sorry I don\'t understand that selection please choose \'l\', \'h\' or \'c\': ')