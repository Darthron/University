'''
Created on Oct 27, 2015

@author: ratvel
'''

from Domain.domain import *

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
                    "\t7 Redo the last undo operation" \
                    "\tYou can always exit the application by writing \"exit\""
        print ("Please choose from the following features :\n", features)
        menu = input()
        if (menu == "exit") :
            exit (0)
        while (menu < '1' or menu > '7') :
            print ("Please choose from the following features :\n", features)
            menu = input()
            if (menu == "exit") :
                exit(0)
        return menu
    except ValueError :
        print ("Select a natural number between 1 and 6!")
        getFeature()
        
def addToListOptions(l, u) :
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
    copyList(l, u)
    addCommand(cmd, l, u)
    print (l)
    #start(l, u)
    
def filterOptions(l, u) :
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
    copyList(l, u)
    filterCommand(cmd, l)
    print (l)
    #start(l, u)
    
def propertyOption(l, u) :
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
    copyList(l, u)
    propertyCommand(cmd, l)
    #start(l, u)
    
def characteristicOption(l, u) :
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
    copyList(l, u)
    characteristicCommand(cmd, l)
    #start(l, u)
    
def modifyOptions(l, u) :
    #Input : numerical list
    #Preconditions : numerical list contains only numbers
    ##Output : numerical list
    #Postconditions : numerical list contains only numbers
    #Modifies the list

    commands = "\tremove 1 - removes the element at position 1\n" \
               "\tremove from 1 to 3 - removes the elements at positions 1, 2 an 3\n" \
               "\treplace 1 3 5 with 5 3 - replaces all the occurrences of sublist 1 3 5 with the sublist 5 3\n"
    print ("Examples of the commands supported by our application :\n", commands)
    cmd = input("Please write a command\n")
    if (cmd == "exit") :
        exit(0)
    while (not checkModifyCommand(cmd)) :
        print ("Please write a command, as seen in the example :\n", commands)
        cmd = input()
        if (cmd == "exit") :
            exit(0)
    copyList(l, u)
    modifyCommand(cmd, l)
    print(l)
    #start(l, u)
    
def undoOption(l, u) :
    #Input : current list, last list
    #Preconditions : numerical lists
    #Output : l, u
    #Postconditions : numerical lists
    #Undoes the last operation
    
    command = "\tundo\n"
    print ("Examples of the commands supported by our application :\n", command)
    cmd = input("Please write a command\n")
    if (cmd == "exit") :
        exit(0)
    while (not checkUndoCommand(cmd)) :
        print ("Please write a command, as seen in the example :\n", command)
        cmd = input()
        if (cmd == "exit") :
            exit(0)
    undoCommand(l, u)
    print(l)
    #start(l, u)

def redoOption(l, u) :
    #Input : current list, last list
    #Preconditions : numerical lists
    #Output : l, u
    #Postconditions : numerical lists
    #Cancels the last undo

    command = "\tredo\n"
    print ("Examples of the commands supported by our application :\n", command)
    cmd = input("Please write a command\n")
    if (cmd == "exit") :
        exit(0)
    while (not checkRedoCommand(cmd)) :
        print ("Please write a command, as seen in the example :\n", command)
        cmd = input()
        if (cmd == "exit") :
            exit(0)
    redoCommand(l, u)
    print(l)
    #start(l, u)

def start(l, u) :
    menuOptions = {'1' : addToListOptions, '2' : modifyOptions, '3' : propertyOption, '4' : characteristicOption,
                   '5' : filterOptions, '6' : undoOption, '7' : redoOption}
    canUndo = False
    while True :
        menu = getFeature()
        if (canUndo == False and menu == '7') :
            print("Nothing to undo!")
        else :
            menuOptions[menu](l, u)
        if menu == '6' :
            canUndo = True
        else :
            canUndo = False

