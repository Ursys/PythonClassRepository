# This code passed the test on the course website

s = 'abcdefghijklmnopqrstuvwxyz'
lrgString = ''
subString = ''
mailBox = ''

for letter in s:
    #print ('letter: ' + letter)
    #print ('mailBox: ' + mailBox)
    #print ('subString: ' + subString)
    #print ('lrgString: ' + lrgString)
    
    
    if letter >= mailBox:
        subString += letter
        #print ('subString changed to ' + subString)
    else:
        if len(lrgString) < len(subString):
            lrgString = subString
            #print ('lrgString changed to ' + lrgString)
        subString = letter
        #print ('subString changed to ' + letter)
    mailBox = letter
    #print ('mailBox changed to ' + letter)
if len(subString) > len(lrgString):
    lrgString = subString
print ('Longest substring in alphabetical order is: ' + lrgString)
