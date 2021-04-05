# get information from the user about conversion
# TODO user input validation for menu
#TODO user input validation fro menu
#user input on the type of conversion
userConversion = input('What type of conversion?\n\t1-inches to mm.\n\t2- mm to inches.\n')

userInput = input('What is the number? ')
print('Your number is :', userInput) # TODO remove 
userNumber = float(userInput)

# perform the conversion 
#conditional statement 
if userConversion == '1':
    # convert from in to mm (userNumber * 25.4)
    print('in to mm')
    userAnswer = userNumber * 25.4
    print('The answer is', userAnswer, 'mm')
if userConversion == '2':
    # convert from mm to in (userNumber / 25.4)
    print('mm to in')
    userAnswer = userNumber / 25.4
    print('The answer is', userAnswer, 'inches.')

# print that information
print('The answer is', userAnswer)