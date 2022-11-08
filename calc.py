import math

# Check if the input is a number.
def isNumber(number):
    try:
        float(number)
        return True
    except ValueError:
        return False

# In case an invalid operation is made.
def errorOperation(errorMessage):
    print("\n", errorMessage, "\n")
    exit()

# Check if operation exists.
def checkOperation(operation):
    
    operation = operation.lower()

    if(operation == "sum" or operation == "+"):
        return True
    elif(operation == "sub" or operation == "-"):
        return True
    elif(operation == "mult" or operation == "*"):
        return True
    elif(operation == "div" or operation == "/"):
        return True
    elif(operation == "sqrt" or operation == "v"):
        return True
    elif(operation == "exp" or operation == "e"):
        return True
    elif(operation == "perc" or operation == "%"):
        return True
    else:
        return False

# Shows the operations available
def showOperations():
    print("\n-------------------  OPERATIONS HELP  -------------------\n\n")
    print("\"SUM\" OR \"+\"  ---> n1 + n2\n")
    print("\"SUB\" OR \"-\"  ---> n1 - n2\n")
    print("\"MULT\" OR \"*\"  ---> n1 * n2\n")
    print("\"DIV\" OR \"/\"  ---> n1 / n2\n")
    print("\"SQRT\" OR \"V\"  ---> The square root of n1\n")
    print("\"EXP\" OR \"E\"  ---> n1^(n2)\n")
    print("\"PERC\" OR \"%\"  ---> n1 % n2\n")
    print("\nThe case of the letters does not matter (e.g. SUm or suM does the same thing)\n")
    print("\n---------------------------------------------------------\n\n")

# Do the operation between two numbers.
def doOperation(operation, n1, n2):

    operation = operation.lower()

    if(operation == "sum" or operation == "+"):
        return n1 + n2
    elif(operation == "sub" or operation == "-"):
        return (n1 - n2)
    elif(operation == "mult" or operation == "*"):
        return n1 * n2
    elif(operation == "div" or operation == "/"):
        if(n2 == 0):
            errorOperation("ERROR! n1 / 0 is undefined")
        return n1 / n2
    elif(operation == "exp" or operation == "e"):
        if(n1 == 0 and n2 == 0):
            errorOperation("ERROR! 0^0 is undefined")
        return n1 ** n2
    elif(operation == "perc" or operation == "%"):
        return n1 % n2


def main(number):

    if(number == "_"):

        # Getting the first number.
        question = "Choose the first number: "
        number_1 = input(question)

        # Checks if the user wants to exit the program.
        if(number_1.lower() == "exit"):
            exit()

        # Checking if is a number.
        while(not isNumber(number_1)): 
            question = "The value inputed is not a number, please choose a number again: "
            number_1 = input(question)

    else:

        # This is not the first operation and it is continuing from a previous one
        number_1 = number

    # Getting the operation to be done.
    question = "Choose operation (Write \"help\" for available operations): "
    operation = input(question)   


    # Checks if user wants help.
    while(operation.lower() == "help"):
        showOperations()
        question = "Choose operation (Write \"help\" for available operations): "
        operation = input(question)


    # Checks if the user wants to exit the program.
    if(operation.lower() == "exit"):
        exit()


    # Checks if operation exists
    while(not checkOperation(operation)):
        question = "That operation does not exist, use the \"help\" command: "
        operation = input(question)

        # Checks if the user wants to exit the program.
        if(operation.lower() == "exit"):
            exit()


    if(operation.lower() == "sqrt" or operation.lower() == "v"):

        if(number_1 < 0):
            errorOperation("ERROR! Can not do the square root of a negative number")            
        else:

            result = round(math.sqrt(number_1),5)
            print("The square root of ", number_1, " is ", result, "\n")
            main(result)

    else:

        # Getting the second number.
        question = "Choose the second number: "
        number_2 = input(question)


        # Checks if the user wants to exit the program.
        if(number_2.lower() == "exit"):
            exit()


        # Checking if is a number.
        while(not isNumber(number_2)): 
            question = "The value inputed is not a number, please choose a number again: "
            number_2 = input(question)


        result = round(doOperation(operation, float(number_1), float(number_2)),5)
        print("\n", number_1, " ", operation, " ", number_2, " = ", result, "\n")
        main(result)

if __name__ == "__main__":
    print("\nAT ANY TIME WRITE \"EXIT\" to exit the program.\n\n")
    main("_")
    

