s = 'azcbobobegghakl'
testString = s[0]
subString = ''
whileCount = len(s)
start = 0

for letters in s:
    if s[letter] >= s[letter - 1]:
        testString += s[start + 1]
    elif s[letter] < s[letter - 1]:
        if len(testString) > len(subString):
            subString = testString
            testString == s[letter]
        else:
            testString == s[letter]