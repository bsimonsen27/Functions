# get information from the user about conversion
# TODO user input validation 
userInput = input('What is the number? ')
print('Your number is :', userInput) # TODO remove 
userNumber = float(userInput)

# perform the conversion 
# convert in to mm 
# convert from in to mm (userNumber * 25.4)
userAnswer = userNumber * 25.4

# convert from mm to in (userNumber / 25.4)
userAnswer = userNumber / 25.4

# print that information
print('The answer is', userAnswer)