userInput = raw_input('Type an integer \n')
int(userInput)
if userInput % 2 == 0:
  print(str(userInput) + "is an EVEN number.")
else:
  print(str(userInput) + "is an ODD number.")