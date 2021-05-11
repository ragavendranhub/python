def WelcomeScreen():
    print("\n")
    print("***************************************************")
    print("*****************Enter your choice*****************")
    print("***************************************************")
    print('\n')

    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("6. Modulus")
    print("7. Is Factor?")
    print("0. Exit")


def addition(value1, value2):
    print(value1, "added with", value2, "is ", value1+value2)
    return exitMsg()


def subtraction(value1, value2):
    print(value1, "subtracted with", value2, "is ", value1-value2)
    return exitMsg()


def multiplication(value1, value2):
    print("\n\n", "Product of ", value1, "and", value2, "is ", value1*value2)
    return exitMsg()


def division(value1, value2):
    print(value1, "divided by", value2, "is ", value1/value2)
    return exitMsg()


def floorDivision(value1, value2):
    print(value1, "floor divided by", value2, " yeilds ", value1/value2)
    return exitMsg()


def modulous(value1, value2):
    print(value2, "modulus of", value1, "is", (value2 % value1))
    return exitMsg()


def isFactor(value1, value2):
    print(value1, "is a factor of", value2, "is ", (value2 % value1 == 0))
    return exitMsg()


def exitMsg():
    a = '''\
\n
==============================
**** Thanks for your Time ****
==============================
    '''
    return a


while True:

    WelcomeScreen()
    choice = input("\nEnter your choice from above : ")

    value1 = int(input("\nEnter your First Number : "))
    value2 = int(input("\nEnter your Second Number : "))

    if choice in ('1', '2', '3', '4', '5', '6', '7', '0'):
        if choice == '1':
            print("\n*** ADDITION ***\n")
            print(addition(value1, value2))
        elif choice == '2':
            print("\n*** SUBSTRACTION ***\n")
            print(subtraction(value1, value2))
        elif choice == '3':
            print("\n*** MULTIPLICATION ***\n")
            print(multiplication(value1, value2))
        elif choice == '4':
            print("\n*** DIVISION ***\n")
            print(division(value1, value2))
        elif choice == '5':
            print("\n*** FLOOR DIVISION ***\n")
            print(floorDivision(value1, value2))
        elif choice == '6':
            print("\n*** MOD / MODULUS ***\n")
            print(modulous(value1, value2))
        elif choice == '7':
            print("\n*** FACTOR CHECK ***\n")
            print(isFactor(value1, value2))
        else:
            print("Invalid Input")
    break
