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

# perform the conversion 
#conditional statement 
calcVal = calculate(userNumber, userConversion)
print('The answer is ', calcVal)
