# get information from the user about conversion
# TODO user input validation for menu
#TODO user input validation fro menu
#user input on the type of conversion
userConversion = input('What type of conversion?\n\t1-inches to mm.\n\t2- mm to inches.\n')

userInput = input('What is the number? ')
print('Your number is :', userInput) # TODO remove 
userNumber = float(userInput)

#function that calculates
def in2mm(userNumber):
    userAnswer = userNumber * 25.4
    return userAnswer

def mm2in(userNumber):
    userAnswer = userNumber / 25.4
    return userAnswer

def calculate(userNumber, converstionType):
    if converstionType == '1':
        userAnswer = userNumber * 25.4
    if converstionType == '2':
        userAnswer = userNumber / 25.4
    return userAnswer

calcVal = calculate(userNumber, userConversion)

def printResults(type, input, calc):
    if type == '1':
        print('The answer is', input, 'in =', calc, 'mm')
    if type == '2':
        print('The answer is', input, 'mm =', calc, 'in')

printResults(userConversion, userInput, calcVal)

