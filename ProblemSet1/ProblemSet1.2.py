s = 'azcbobobegghakl'
bobCount = 0

for letter in s:
    if letter == 'b':
        if letter + 1 == 'o':
            if letter + 2 == 'b':
                bobCount +=1

print 'Number of times bob occurs is: ' + str(bobCount)