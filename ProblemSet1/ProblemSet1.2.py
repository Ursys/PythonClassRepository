s = 'azcbobobegghakl'
bobCount = 0
whileCount = len(s)
start = 0

while whileCount > 0:
    if s[start:start+3] == 'bob':
        bobCount += 1
    whileCount -=1
    start +=1

print 'Number of times bob occurs is: ' + str(bobCount)