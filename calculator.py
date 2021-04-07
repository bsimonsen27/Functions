# get information from the user about conversion
# TODO user input validation for menu
#TODO user input validation fro menu
#user input on the type of conversion
def in2mm(userNumber):
        return userNumber * 25.4

def mm2in(userNumber):
    return userNumber / 25.4

def in2ft(userNumber):
    return userNumber / 12


def printResults(type, input):
    #calcVal = calculate(userNumber, userConversion)
    if type == '1':
        cfrom = 'in'
        to = 'mm'
        calcVal = in2mm(input)
    if type == '2':
        cfrom = 'mm'
        to = 'in'
        calcVal = mm2in(input)
    if type == '3':
        cfrom = 'in'
        to = 'ft'
        calcVal = in2ft(input)
    print('The answer is', input, cfrom,'=', calcVal, to)

while True:
    userConversion = input('What type of conversion?\n\t1-inches to mm.\n\t2- mm to inches.\n\t3-inches to feet.\n\tq to quit.\n')
    if userConversion == 'q':
        break
    userInput = input('What is the number? ')
    print('Your number is :', userInput) # TODO remove 
    userNumber = float(userInput)

    #function that calculates
    


    printResults(userConversion, userNumber)

