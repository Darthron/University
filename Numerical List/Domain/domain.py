

from Utility.utility import *
from UI.ui import *
#from UI.ui import modifyOptions

def checkCharacteristicCommand(cmd) :
    #Input : the command written by the user
    #Preconditions :
    #Output : True if the command is a valid characteristic command
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
        return stringHasFormatWordIntegerWordInteger(cmd[firstSpaceIndex + 1 :], elements, False, False)
    except ValueError :
        return False
    
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

    start = int (cmd[secondSpaceIndex + 1 : thirdSpaceIndex]) - 1
    end = int (cmd[fourthSpaceIndex + 1 :])
    if (cmd[: firstSpaceIndex] == "max") :
        print (getMaxFromList(l[start : end]))
    elif (cmd[: firstSpaceIndex] == "gcd") :
        print (getGcdOfElements(l[start : end]))
    elif (cmd[: firstSpaceIndex] == "sum") :
        print (getSumOfElements(l[start : end]))
        
def checkPropertyCommand(cmd) :
    #Input : the command written by the user
    #Preconditions :
    #Output : True if the command is a valid property command
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
    return stringHasFormatWordIntegerWordInteger(cmd[firstSpaceIndex + 1 :], elements, False, False)

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

    start = int (cmd[secondSpaceIndex + 1 : thirdSpaceIndex]) - 1
    end = int (cmd[fourthSpaceIndex + 1 :])
    if (cmd[: firstSpaceIndex] == "prime") :
        for c in l[start : end] :
            if (isPrime(c)) :
                print(c, end = " ")
    elif (cmd[: firstSpaceIndex] == "odd") :
        for c in l[start : end] :
            if (c % 2 == 1) :
                print (c, end = " ")
    print()
    
def checkFilterCommand(cmd) :
    #Input : the command written by the user
    #Preconditions :
    #Output : True if the command is a valid filter command
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
    
def checkAddCommand(cmd) :
    #Input : command written by the user
    #Preconditions : string
    #Output : True if the command is valid,
    #         False otherwise
    #Postconditions : Boolean
    #Check whether the command introduced by the user is valid or not
    try :
        #firstSpaceIndex = cmd.index(' ')
        if (stringHasFormatWordInteger(cmd, "add", True)) :
            return True
        else :
            elements = ["insert", "at"]
            if (stringHasFormatWordIntegerWordInteger(cmd, elements, True, False)) :
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

def addCommand(cmd, l, u) :
    #Input : add to list command of the user, the numerical list
    #Preconditions : valid add to list command, numerical list
    #Output : numerical list
    #Postconditions : list containing only numbers
    #Performs the command given by the user
    firstSpaceIndex = cmd.index(' ')
    if (cmd[: firstSpaceIndex] == "add") :
        l.append(int (cmd[firstSpaceIndex + 1 :]))
    elif (cmd[: firstSpaceIndex] == "insert") :
        secondSpaceIndex = cmd[firstSpaceIndex + 1 :].index(' ') + firstSpaceIndex + 1
        thirdSpaceIndex = cmd[secondSpaceIndex + 1:].index(' ') + secondSpaceIndex + 1
        number = int (cmd[firstSpaceIndex + 1 : secondSpaceIndex])
        position = int (cmd[thirdSpaceIndex + 1 :]) - 1
        """if (position > len(l) + 1) :
            print("Please insert the number at a valid position. The last position currently occupied by an "
                  "element is", len(l))
            addToListOptions(l, u)"""
        l.insert(position, number)

def checkModifyCommand(cmd) :
    #Input : command written by the user
    #Preconditions : string
    #Output : True if the command is valid,
    #         False otherwise
    #Postconditions : Boolean
    #Check whether the command introduced by the user is valid or not
    try :
        firstSpaceIndex = cmd.index(' ')
        if (stringHasFormatWordInteger(cmd, "remove", False)) :
            return True
        elif (cmd[: firstSpaceIndex] == "remove") :
            if (stringHasFormatWordIntegerWordInteger(cmd[firstSpaceIndex + 1 :], ["from", "to"], False, False)) :
                return True 
        elif (cmd[: firstSpaceIndex] == "replace") :
            letterIndex = indexOfFirstLetter(cmd[firstSpaceIndex + 1 :]) + firstSpaceIndex + 1
            spaceIndex = cmd[letterIndex + 1 :].index(' ') + letterIndex + 1
            if (stringIsListOfIntegers(cmd[firstSpaceIndex + 1 : letterIndex - 1])) :
                if (cmd[letterIndex : spaceIndex] == "with") :
                    if (stringIsListOfIntegers(cmd[spaceIndex + 1 :])) :
                        return True
        return False
    except ValueError :
        return False

def modifyCommand(cmd, l) :
    #Input : command, list
    #Preconditions : valid command, list of integers
    #Output : list
    #Postconditions : numerical list
    #Executes the command given by the user
    
    firstSpaceIndex = cmd.index(' ')
    if (stringHasFormatWordInteger(cmd, "remove", False)) :
        position = int (cmd[firstSpaceIndex + 1 :]) - 1
        del l[position]
    elif (cmd[: firstSpaceIndex] == "remove") :
        if (stringHasFormatWordIntegerWordInteger(cmd[firstSpaceIndex + 1 :], ["from", "to"], False, False)) :
            secondSpaceIndex = cmd[firstSpaceIndex + 1 :].index(' ') + firstSpaceIndex + 1
            thirdSpaceIndex = cmd[secondSpaceIndex + 1 :].index(' ') + secondSpaceIndex + 1
            fourthSpaceIndex = cmd[thirdSpaceIndex + 1 :].index(' ') + thirdSpaceIndex + 1
            begin = int (cmd[secondSpaceIndex + 1 : thirdSpaceIndex]) - 1
            end = int (cmd[fourthSpaceIndex :])
            """if (end > len(l)) :
                print("There are only", len(l), "numbers in the list!")
                modifyOptions(l, u)"""
            del l[begin : end]
    elif (cmd[: firstSpaceIndex] == "replace") :
        endOfFirstList = indexOfFirstLetter(cmd[firstSpaceIndex + 1 :]) + firstSpaceIndex
        sublistToReplace = getList(cmd[firstSpaceIndex + 1: endOfFirstList])
        beginningOfSecondSublist = cmd[endOfFirstList + 1 :].index(' ') + endOfFirstList + 2
        newSublist = getList(cmd[beginningOfSecondSublist :])
        position = findSublist(l, sublistToReplace)
        length = len(sublistToReplace)
        while (position != -1) :
            l[position : position + length] = newSublist
            position = findSublist(l[position + length + 1 :], sublistToReplace)
      
def checkUndoCommand(cmd) :
    #Input : string
    #Preconditions : -
    #Output : True if it is a valid undo command
    #         False otherwise
    #Postconditions : -
    
    if (cmd == "undo") :
        return True
    return False
   
def undoCommand(l, u) :
    #Input : current list, last list
    #Preconditions : numerical lists
    #Output : l, u
    #Postconditions : -   
          
    swapLists(l, u)

def checkRedoCommand(cmd) :
    #Input : string
    #Preconditions : -
    #Output : True if it is a valid redo command
    #         False otherwise
    #Postconditions : -

    if (cmd == "redo") :
        return True
    return False

def redoCommand(l, u) :
    #Input : current list, last list
    #Preconditions : numerical lists
    #Output : l, u
    #Postconditions : -

    swapLists(l, u)
            
            
