s = 'azcbobobegghakl'
testString = s[0]
subString = ''
whileCount = len(s)
start = 0

while whileCount < len(s):
    if s[whileCount] >= s[whileCount - 1]:
        testString += s[start + 1]
    elif s[whileCount] < s[whileCount - 1]:
        if len(testString) > len(subString):
            subString = testString
            testString == s[whileCount]
        else:
            testString == s[whileCount]
    print subString
    whileCount += 1
