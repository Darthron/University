import math

__author__ = 'Ratvel'

def getFeature() :
    #Input : -
    #Preconditions : -
    #Output : feature number
    #Postconditions : feature number = {1, 2, ..., 6}
    #Gets the feature number
    try :
        features =  "\t1. Add numbers into the list\n" \
                    "\t2. Modify elements from the list\n" \
                    "\t3. Write the numbers having different properties\n" \
                    "\t4. Obtain different characteristics of sublists\n" \
                    "\t5. Filter\n" \
                    "\t6. Undo the last operation\n" \
                    "\tYou can always exit the application by writing \"exit\""
        print ("Please choose from the following features :\n", features)
        menu = input()
        if (menu == "exit") :
            exit (0)
        while (menu < '1' or menu > '6') :
            print ("Please choose from the following features :\n", features)
            menu = input()
            if (menu == "exit") :
                exit(0)
        return menu
    except ValueError :
        print ("Select a natural number between 1 and 6!")
        getFeature()

def stringHasFormatWordNumberWordNumber (cmd, elements, firstNegative, secondNegative) :
    #Input : string, two words as list, boolean, boolean
    #Preconditions : string not NULL, list has at least two elements
    #Output : True if the string satisfies the format WordNumberWordNumber and the integers pass the negative test, if
    #         the corresponding boolean is False
    #         False otherwise
    #Postconditions : -
    #Checks if a string has the format "word integer word integer"
    firstSpaceIndex = cmd.index(' ')
    if (cmd[0 : firstSpaceIndex] == elements[0]) :
        secondSpaceIndex = cmd[firstSpaceIndex + 1 :].index(' ') + firstSpaceIndex + 1
        if (firstNegative == True) :
            if (cmd[firstSpaceIndex + 1 : secondSpaceIndex].isnumeric() or
                (cmd[firstSpaceIndex + 1] == '-' and cmd[firstSpaceIndex + 2 : secondSpaceIndex].isnumeric())) :
                thirdSpaceIndex = cmd[secondSpaceIndex + 1:].index(' ') + secondSpaceIndex + 1
                if (cmd[secondSpaceIndex + 1 : thirdSpaceIndex] == elements[1]) :
                    if (cmd[thirdSpaceIndex + 1 :].isnumeric()) :
                        return True
        else :
            if (cmd[firstSpaceIndex + 1 : secondSpaceIndex].isnumeric()) :
                thirdSpaceIndex = cmd[secondSpaceIndex + 1:].index(' ') + secondSpaceIndex + 1
                if (cmd[secondSpaceIndex + 1 : thirdSpaceIndex] == elements[1]) :
                    if (cmd[thirdSpaceIndex + 1 :].isnumeric()) :
                        return True
    return False

def stringHasFormatWordNumber (cmd, word, numberCanBeNegative) :
    #Input : string, word, boolean
    #Preconditions : string is not NULL, word is not NULL
    #Output : True if the string has the asked format and the integer passes the negative test if the boolean is False
    #Postconditions : -
    #Checks if a string has the format "word integer"
    firstSpaceIndex = cmd.index(' ')
    if (cmd[0 : firstSpaceIndex] == word) :
        if (numberCanBeNegative == True) :
            if (cmd[firstSpaceIndex + 1 :].isnumeric() or
                (cmd[firstSpaceIndex + 1] == '-') and cmd[firstSpaceIndex + 2 :].isnumeric()) :
                return True
            else :
                return False
        else :
            if (cmd[firstSpaceIndex + 1 :].isnumeric()) :
                return True
            else :
                return False
    return False

def checkAddCommand(cmd) :
    #Input : command written by the user
    #Preconditions : string
    #Output : True if the command is valid,
    #         False otherwise
    #Postconditions : Boolean
    #Check whether the command introduced by the user is valid or not
    try :
        #firstSpaceIndex = cmd.index(' ')
        if (stringHasFormatWordNumber(cmd, "add", True)) :
            return True
        else :
            elements = ["insert", "at"]
            if (stringHasFormatWordNumberWordNumber(cmd, elements, True, False)) :
                return True
        """if (cmd[0 : firstSpaceIndex] == "add") :
            if (cmd[firstSpaceIndex + 1 :].isnumeric() or
                (cmd[firstSpaceIndex + 1] == '-') and cmd[firstSpaceIndex + 2 :].isnumeric()) :
                return True
            else :
                return False
        elif (cmd[0 : firstSpaceIndex] == "insert") :
            secondSpaceIndex = cmd[firstSpaceIndex + 1 :].index(' ') + firstSpaceIndex + 1
            if (cmd[firstSpaceIndex + 1 : secondSpaceIndex].isnumeric() or
                    (cmd[firstSpaceIndex + 1] == '-' and cmd[firstSpaceIndex + 2 : secondSpaceIndex].isnumeric())) :
                thirdSpaceIndex = cmd[secondSpaceIndex + 1:].index(' ') + secondSpaceIndex + 1
                if (cmd[secondSpaceIndex + 1 : thirdSpaceIndex] == "at") :
                    if (cmd[thirdSpaceIndex + 1 :].isnumeric()) :
                        return True"""
        return False
    except ValueError :
        return False

def addCommand(cmd, l) :
    #Input : add to list command of the user, the numerical list
    #Preconditions : valid add to list command, numerical list
    #Output : numerical list
    #Postconditions : list containing only numbers
    #Performs the command given by the user
    firstSpaceIndex = cmd.index(' ')
    if (cmd[: firstSpaceIndex] == "add") :
        l.append(int (cmd[firstSpaceIndex + 1 :]))
    elif (cmd[: ]) :
        secondSpaceIndex = cmd[firstSpaceIndex + 1 :].index(' ') + firstSpaceIndex + 1
        thirdSpaceIndex = cmd[secondSpaceIndex + 1:].index(' ') + secondSpaceIndex + 1
        number = int (cmd[firstSpaceIndex + 1 : secondSpaceIndex])
        position = int (cmd[thirdSpaceIndex + 1 :]) - 1
        if (position > len(l) + 1) :
            print("Please insert the number at a valid position. The last position currently occupied by an "
                  "element is", len(l))
            addToListOptions(l)
        l.insert(position, number)


def addToListOptions(l) :
    #Input : numerical list
    #Preconditions : numerical list contains only numbers
    #Output : numerical list
    #Postconditions : numerical list contains only numbers
    #Presents the user with the addition commands and calls the addCommand function
    commands = "\tadd 123 - adds 123 at the end of the list\n" \
              "\tinsert 123 at 1 - insert number 123 at position 1 in the list; positions are numbered from 0\n"
    print ("Examples of the commands supported by our application :\n", commands)
    cmd = input("Please write a command\n")
    if ("exit" == cmd) :
        exit(0)
    while (not checkAddCommand(cmd)) :
        print ("Please write a command, as seen in the example :\n", commands)
        cmd = input()
        if ("exit" == cmd) :
            exit(0)
    addCommand(cmd, l)
    print (l)
    start(l)

def isPrime(no) :
    #Input : number
    #Preconditions : natural number
    #Output : True if the number is prime
    #         False otherwise
    #Postconditions :
    #Checks whether a number is prime or not
    if (no < 2) :
        return False
    if (no < 4) :
        return True
    d = 2
    while (d <= math.sqrt(no)) :
        if (no % d == 0) :
            return False
        d += 1
    return True

def checkFilterCommand(cmd) :
    #Input : the command written by the user
    #Preconditions :
    #Outpute : True if the command is a valid filter command
    #          False if the command is not a valid filter command
    #Postconditions : -
    #Checks whether the command given by the user is a valid filter command or not
    try :
        spaceIndex = cmd.index(' ')
        if (cmd[: spaceIndex] != "filter") :
            return False
        if (cmd[spaceIndex + 1 :] == "negative") :
            return True
        if (cmd[spaceIndex + 1 :] == "prime") :
            return True
        return False
    except ValueError :
        return False

def filterCommand(cmd, l) :
    #Input : command given by user, numerical list
    #Preconditions : valid command, list containing only numbers
    #Output : numerical list
    #Postconditions : list containing only numbers
    #Performs the command given by the user
    spaceIndex = cmd.index(' ')
    if (cmd[spaceIndex + 1 :] == "prime") :
        i = 0
        while (i < len(l)) :
            if (not isPrime(l[i])) :
                l.remove(l[i])
                i -= 1
            i += 1
    else :
        i = 0
        while (i < len(l)) :
            if (l[i] >= 0) :
                l.remove(l[i])
                i -= 1
            i += 1

def filterOptions(l) :
    #Input : numerical list
    #Preconditions : numerical list contains only numbers
    #Output : numerical list
    #Postconditions : numerical list contains only numbers
    #Presents the user with the filter commands and calls the filterCommand function
    commands = "\tfilter prime - retains only the prime numbers\n" \
               "\tfilter negative - retains only the negative numbers\n"
    print ("Examples of the commands supported by our application :\n", commands)
    cmd = input("Please write a command\n")
    if (cmd == "exit") :
        exit(0)
    while (not checkFilterCommand(cmd)) :
        print ("Please write a command, as seen in the example :\n", commands)
        cmd = input()
        if (cmd == "exit") :
            exit(0)
    filterCommand(cmd, l)
    print (l)
    start(l)

def checkPropertyCommand(cmd) :
    #Input : the command written by the user
    #Preconditions :
    #Outpute : True if the command is a valid property command
    #          False if the command is not a valid property command
    #Postconditions : -
    #Checks whether the command given by the user is a valid property command or not
    ok = 0
    firstSpaceIndex = cmd.index(' ')
    secondSpaceIndex = cmd[firstSpaceIndex + 1 :].index(' ') + firstSpaceIndex + 1
    thirdSpaceIndex = cmd[secondSpaceIndex + 1 :].index(' ') + secondSpaceIndex + 1
    fourthSpaceIndex = cmd[thirdSpaceIndex + 1 :].index(' ') + thirdSpaceIndex + 1

    start = int (cmd[secondSpaceIndex + 1 : thirdSpaceIndex]) - 1
    end = int (cmd[fourthSpaceIndex + 1 :]) - 1
    if (end < start) :
        return False
    acceptedFirstWords = ["prime", "odd"]
    for word in acceptedFirstWords :
        if (cmd[: firstSpaceIndex] == word) :
            ok = 1
            break
    if (not ok) :
        return False
    elements = ["from", "to"]
    return stringHasFormatWordNumberWordNumber(cmd[firstSpaceIndex + 1 :], elements, False, False)

def propertyCommand(cmd, l) :
    #Input : command given by user, numerical list
    #Preconditions : valid command, list containing only numbers
    #Output : numerical list
    #Postconditions : list containing only numbers
    #Performs the command given by the user
    firstSpaceIndex = cmd.index(' ')
    secondSpaceIndex = cmd[firstSpaceIndex + 1 :].index(' ') + firstSpaceIndex + 1
    thirdSpaceIndex = cmd[secondSpaceIndex + 1 :].index(' ') + secondSpaceIndex + 1
    fourthSpaceIndex = cmd[thirdSpaceIndex + 1 :].index(' ') + thirdSpaceIndex + 1

    start = int (cmd[secondSpaceIndex + 1 : thirdSpaceIndex])
    end = int (cmd[fourthSpaceIndex + 1 :]) + 1
    if (cmd[: firstSpaceIndex] == "prime") :
        for c in l[start : end] :
            if (isPrime(c)) :
                print(c, end = " ")
    elif (cmd[: firstSpaceIndex] == "odd") :
        for c in l[start : end] :
            if (c % 2 == 1) :
                print (c, end = " ")
    print()

def propertyOption(l) :
    #Input : numerical list
    #Preconditions : numerical list contains only numbers
    ##Output : numerical list
    #Postconditions : numerical list contains only numbers
    #Writes the numbers with the property the user asked, in the interval given

    commands = "\tprime from 1 to 5 - writes the prime numbers between position 1 and 5 in the list\n" \
               "\todd from 1 to 5 - writes the odd numbers between position 1 and 5 in the list\n"
    print ("Examples of the commands supported by our application :\n", commands)
    cmd = input("Please write a command\n")
    if (cmd == "exit") :
        exit(0)
    while (not checkPropertyCommand(cmd)) :
        print ("Please write a command, as seen in the example :\n", commands)
        cmd = input()
        if (cmd == "exit") :
            exit(0)
    propertyCommand(cmd, l)
    start(l)

def checkCharacteristicCommand(cmd) :
    #Input : the command written by the user
    #Preconditions :
    #Outpute : True if the command is a valid characteristic command
    #          False if the command is not a valid characteristic command
    #Postconditions : -
    #Checks whether the command given by the user is a valid characteristic command or not
    try :
        ok = 0
        firstSpaceIndex = cmd.index(' ')
        secondSpaceIndex = cmd[firstSpaceIndex + 1 :].index(' ') + firstSpaceIndex + 1
        thirdSpaceIndex = cmd[secondSpaceIndex + 1 :].index(' ') + secondSpaceIndex + 1
        fourthSpaceIndex = cmd[thirdSpaceIndex + 1 :].index(' ') + thirdSpaceIndex + 1

        start = int (cmd[secondSpaceIndex + 1 : thirdSpaceIndex])
        end = int (cmd[fourthSpaceIndex + 1 :])
        if (end < start) :
            return False
        acceptedFirstWords = ["gcd", "max", "sum"]
        for word in acceptedFirstWords :
            if (cmd[: firstSpaceIndex] == word) :
                ok = 1
                break
        if (not ok) :
            return False
        elements = ["from", "to"]
        return stringHasFormatWordNumberWordNumber(cmd[firstSpaceIndex + 1 :], elements, False, False)
    except ValueError :
        return False

def getMaxFromList(l) :
    #Input : numerical list
    #Preconditions : list has only numbers
    #Output : maximum element
    #Postconditions : maximum element belongs to the list
    maxim = l[0]
    for elem in l[1 :] :
        maxim = max(maxim, elem)
    return maxim

def getSumOfElements(l) :
    #Input : numerical list
    #Preconditions : list has only numebers
    #Output : sum of the elements
    #Postconditions : -
    s = 0
    for elem in l :
        s += elem
    return s

def gcd(a, b) :
    #Input : two numbers
    #Preconditions : numbers are natural
    #Output : greatest common divisor
    #Postcondition : natural number, greater or equal to 1
    if b == 0 :
        return a
    a = a % b
    aux = b
    b = a
    a = aux
    return gcd (a, b)

def getGcdOfElements(l) :
    #Input : numerical list
    #Preconditions : list has only numbers
    #Output : greatest common divisor
    #Postconditions : natural number, greater or equal to 1
    if (len(l) == 1) :
        return l[0]
    res = abs(l[0])
    for e in l[1 :] :
        res = gcd(res, abs(e))
    return res

def characteristicCommand(cmd, l) :
    #Input : command given by user, numerical list
    #Preconditions : valid command, list containing only numbers
    #Output : numerical list
    #Postconditions : list containing only numbers
    #Performs the command given by the user
    firstSpaceIndex = cmd.index(' ')
    secondSpaceIndex = cmd[firstSpaceIndex + 1 :].index(' ') + firstSpaceIndex + 1
    thirdSpaceIndex = cmd[secondSpaceIndex + 1 :].index(' ') + secondSpaceIndex + 1
    fourthSpaceIndex = cmd[thirdSpaceIndex + 1 :].index(' ') + thirdSpaceIndex + 1

    start = int (cmd[secondSpaceIndex + 1 : thirdSpaceIndex])
    end = int (cmd[fourthSpaceIndex + 1 :]) + 1
    if (cmd[: firstSpaceIndex] == "max") :
        print (getMaxFromList(l[start : end]))
    elif (cmd[: firstSpaceIndex] == "gcd") :
        print (getGcdOfElements(l[start : end]))
    elif (cmd[: firstSpaceIndex] == "sum") :
        print (getSumOfElements(l[start : end]))

def characteristicOption(l) :
    #Input : numerical list
    #Preconditions : numerical list contains only numbers
    ##Output : numerical list
    #Postconditions : numerical list contains only numbers
    #Writes the numbers with the property the user asked, in the interval given
    commands = "\tsum from 1 to 5 - writes the sum numbers between position 1 and 5 in the list\n" \
               "\tgcd from 1 to 5 - writes the greatest common divisor of elements " \
               "between position 1 and 5 in the list\n" \
               "\tmax from 1 to 5 - writes the greater element of the sublist from position 1 to 5\n"
    print ("Examples of the commands supported by our application :\n", commands)
    cmd = input("Please write a command\n")
    if (cmd == "exit") :
        exit(0)
    while (not checkCharacteristicCommand(cmd)) :
        print ("Please write a command, as seen in the example :\n", commands)
        cmd = input()
        if (cmd == "exit") :
            exit(0)
    characteristicCommand(cmd, l)
    start(l)

def testCheckCharacteristicCommand() :
    assert checkCharacteristicCommand("sum from 1 to 4") == True
    assert checkCharacteristicCommand("max from 1 to 4") == True
    assert checkCharacteristicCommand("gcd from 1 to 4") == True
    assert checkCharacteristicCommand("sum from -1 to 5") == False
    assert checkCharacteristicCommand("sum from 2 to 1") == False
    assert checkCharacteristicCommand("sum from  2 to 3") == False

def testGetGcdOfElements() :
    assert getGcdOfElements([1, 2, 4, 16]) == 1
    assert getGcdOfElements([4, 5]) == 1
    assert getGcdOfElements([-4, 6]) == 2

def testGetMaxFromList() :
    assert getMaxFromList([-1]) == -1
    assert getMaxFromList([0, 0, -2]) == 0
    assert getMaxFromList([1, 2, 4]) == 4

def testGetSumOfElements() :
    assert getSumOfElements([]) == 0
    assert getSumOfElements([1, 3]) == 4
    assert getSumOfElements([1]) == 1
    assert getSumOfElements([-1, 1]) == 0


def testGcd() :
    assert gcd(1, 5) == 1
    assert gcd(-6, 14) == 2
    assert gcd(4, 4) == 4

def testStringHasFormatWordNumberWordNumber() :
    assert stringHasFormatWordNumberWordNumber("insert 1 at -1", ["insert", "at"], True, False) == False
    assert stringHasFormatWordNumberWordNumber("insert -1 at 1", ["insert", "at"], False, False) == False
    assert stringHasFormatWordNumberWordNumber("inser -1 at 1", ["insert", "at"], True, False) == False
    assert stringHasFormatWordNumberWordNumber("insert  -1 at 1", ["insert", "at"], True, False) == False
    assert stringHasFormatWordNumberWordNumber("insert -1 at 1", ["insert", "at"], True, False) == True
    assert stringHasFormatWordNumberWordNumber("insert 1 at 1", ["inser", "at"], True, False) == False

def testStringHasFormatWordNumber() :
    assert stringHasFormatWordNumber("add 1", "add", True) == True
    assert stringHasFormatWordNumber(" add 1", "add", True) == False
    assert stringHasFormatWordNumber("add -1", "ad", True) == False
    assert stringHasFormatWordNumber("add -1", "add", False) == False

def testCheckPropertyCommand () :
    assert checkPropertyCommand("prim from 1 to 5") == False
    assert checkPropertyCommand("prime fro 1 to 5") == False
    assert checkPropertyCommand("prime from -1 to 5") == False
    assert checkPropertyCommand("prime from 1 to -4") == False
    assert checkPropertyCommand("prime from 3 to 2") == False
    assert checkPropertyCommand("prime from 3 t 1") == False
    assert checkPropertyCommand("prime from 3 to 4 ") == False
    assert checkPropertyCommand("prime from 3 to 5") == True
    assert checkPropertyCommand("odd from 3 to 5") == True

def testCheckAddCommand() :
    assert checkAddCommand("add") == False
    assert checkAddCommand("add 1a") == False
    assert checkAddCommand("add 1 ") == False
    assert checkAddCommand("add 1") == True
    assert checkAddCommand(" add 1") == False
    assert checkAddCommand("add 1 1") == False
    assert checkAddCommand("insert 1 at 1") == True
    assert checkAddCommand("insert -1 at 1") == True
    assert checkAddCommand("insert 1 at -1") == False
    assert checkAddCommand("insert") == False
    assert checkAddCommand("insert 1") == False
    assert checkAddCommand("insert 1 at ") == False

def testCheckFilterCommand() :
    assert checkFilterCommand("filter") == False
    assert checkFilterCommand("filter prim") == False
    assert checkFilterCommand("filter negative") == True
    assert checkFilterCommand("filter prime") == True
    assert checkFilterCommand("filter prime ") == False

def testFilterCommand() :
    l = [0]
    filterCommand("filter prime", l)
    assert  l == []
    l = [0, 1, 2, 3, 4, 5, -4]
    filterCommand("filter prime", l)
    assert l == [2, 3, 5]
    l = [-1, 0, 4, 5, -3]
    filterCommand("filter negative", l)
    assert l == [-1, -3]

def testIsPrime() :
    assert isPrime(-5) == False
    assert isPrime(0) == False
    assert isPrime(1) == False
    assert isPrime(2) == True
    assert isPrime(3) == True
    assert isPrime(4) == False
    assert isPrime(9) == False
    assert isPrime(17) == True

def testAddCommand() :
    l = []
    addCommand("add -1", l)
    assert l == [-1]
    l = [0]
    addCommand("add 1", l)
    assert  l == [0, 1]
    l = [1, 2, 3, 4]
    addCommand("insert -1 at 0", l)
    assert l == [-1, 1, 2, 3, 4]
    l = [1, 2, 3, 4]
    addCommand("insert 1 at 6", l)
    assert l == [1, 2, 3, 4]

def start(l) :
    menuOptions = {'1' : addToListOptions, '5' : filterOptions, '3' : propertyOption, '4' : characteristicOption}
    menu = getFeature()
    menuOptions[menu](l)

def main() :
    l = [3, 1, -2, 3, -4, -5, 6, -5, 5, -17, 2, 10]
    #characteristicCommand("odd from 1 to 1", l)
    """
    testCheckCharacteristicCommand()
    testGcd()
    testGetMaxFromList()
    testGetGcdOfElements()
    testGetSumOfElements()
    testCheckPropertyCommand()
    testStringHasFormatWordNumberWordNumber()
    testStringHasFormatWordNumber()
    testFilterCommand()
    testIsPrime()
    testAddCommand()
    testCheckAddCommand()
    testCheckFilterCommand()
    """
    start(l)

main()
