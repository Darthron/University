'''
Created on Oct 27, 2015

@author: ratvel
'''

from math import sqrt

def stringHasFormatWordIntegerWordInteger (cmd, elements, firstNegative, secondNegative) :
    #Input : string, two words as list, boolean, boolean
    #Preconditions : string not NULL, list has at least two elements
    #Output : True if the string satisfies the format WordNumberWordNumber and the integers pass the negative test, if
    #         the corresponding boolean is False
    #         False otherwise
    #Postconditions : -
    #Checks if a string has the format "word integer word integer"
    try :
        firstSpaceIndex = cmd.index(' ')
        secondSpaceIndex = cmd[firstSpaceIndex + 1 :].index(' ') + firstSpaceIndex + 1
        if (stringHasFormatWordInteger(cmd[: secondSpaceIndex], elements[0], firstNegative)) :
            if (stringHasFormatWordInteger(cmd[secondSpaceIndex + 1 :], elements[1], secondNegative)) :
                return True
        return False
        """if (cmd[0 : firstSpaceIndex] == elements[0]) :
        secondSpaceIndex = cmd[firstSpaceIndex + 1 :].index(' ') + firstSpaceIndex + 1
        if (firstNegative == True) :
            if (cmd[firstSpaceIndex + 1 : secondSpaceIndex].isnumeric() or
                (cmd[firstSpaceIndex + 1] == '-' and cmd[firstSpaceIndex + 2 : secondSpaceIndex].isnumeric())) :
                thirdSpaceIndex = cmd[secondSpaceIndex + 1:].index(' ') + secondSpaceIndex + 1
                if (stringHasFormatWordInteger(cmd[secondSpaceIndex + 1 :], elements[1]], secondNegative))
                if (cmd[secondSpaceIndex + 1 : thirdSpaceIndex] == elements[1]) :
                    if (cmd[thirdSpaceIndex + 1 :].isnumeric()) :
                        return True
        else :
            if (cmd[firstSpaceIndex + 1 : secondSpaceIndex].isnumeric() and cmd[firstSpaceIndex + 1] > '0') :
                thirdSpaceIndex = cmd[secondSpaceIndex + 1:].index(' ') + secondSpaceIndex + 1
                if (cmd[secondSpaceIndex + 1 : thirdSpaceIndex] == elements[1]) :
                    if (cmd[thirdSpaceIndex + 1 :].isnumeric()) :
                        return True
        return False"""
    except ValueError :
        return False

def stringHasFormatWordInteger (cmd, word, numberCanBeNegative) :
    #Input : string, word, boolean
    #Preconditions : string is not NULL, word is not NULL
    #Output : True if the string has the asked format and the integer passes the negative test if the boolean is False
    #Postconditions : -
    #Checks if a string has the format "word integer"
    try :
        firstSpaceIndex = cmd.index(' ')
        if (cmd[0 : firstSpaceIndex] == word) :
            if (numberCanBeNegative == True) :
                if ((cmd[firstSpaceIndex + 1 :].isnumeric()) or
                    (cmd[firstSpaceIndex + 1] == '-') and cmd[firstSpaceIndex + 2 :].isnumeric()) :
                    return True
                else :
                    return False
            else :
                if (cmd[firstSpaceIndex + 1 :].isnumeric() and cmd[firstSpaceIndex + 1] != '0') :
                    return True
                else :
                    return False
        return False
    except ValueError :
        return False
    except IndexError :
        return False

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
    while (d <= sqrt(no)) :
        if (no % d == 0) :
            return False
        d += 1
    return True

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

def indexOfFirstLetter(str) :
    #Input : string
    #Preconditions : str is a string
    #Output : -1 if there is no letter
    #         the index in str of the first letter
    #Postconditions : integer
    length = len(str)
    for i in range(length) :
        if (str[i] >= 'a' and str[i] <= 'z') or (str[i] >= 'A' and str[i] <= 'Z') :
            return i
    return -1

def stringIsNumericUntilSpaceOrEnd(str) :
    #Input : string
    #Preconditions : -
    #Output : True if str has only digits until its first space character or string ends
    #         False otherwise
    #Postconditions :
    
    if (not str[0].isnumeric()) :
        return False
    for c in str :
        if (c < '0' or c > '9') :
            if (c == ' ') :
                return True
            return False
    return True

def stringIsListOfIntegers(str) :
    #Input : String
    #Preconditions : str is a string
    #Output : True if str has format "a b c", where a, b, c are IntegerSizeTests
    #         False otherwise
    #Postconditions :-
    
    length = len(str)
    if (length == 1 and not str[0].isnumeric()) :
        return False
    if (length == 1 and str[0].isnumeric()) :
        return True
    i = 0
    while i < length :
        if (str[i] == '-') :
            if (not stringIsNumericUntilSpaceOrEnd(str[i + 1 :])) :
                return False
            while (i < length and str[i].isnumeric()) :
                i += 1
            i += 1
        else :
            if (not stringIsNumericUntilSpaceOrEnd(str[i :])) :
                return False
            while (i < length and str[i].isnumeric()) :
                i += 1
            i += 1
    return True

def getList(str) :
    #Input : String
    #Preconditions : str is a string
    #Output : numerical list
    #Postconditions : -
    #Builds a list based on the input
    
    l = []
    length = len(str)
    i= 0
    while i < length :
        j = i + 1
        while (j < length and str[j] != ' ') :
            j += 1
        l.append(int (str[i : j]))
        i = j + 1
    return l

def findSublist(l, listToFind) :
    #Input : two lists
    #Preconditions : numerical lists
    #Output : -1 if the second list is not in the first one
    #          the index where the second list begins in the first one
    #Postconditions : -
    
    length1 = len(l)
    length2 = len(listToFind)
    i = 0
    j = 0
    if length2 == 0 :
        return -1
    while (i < length1 and l[i] != listToFind[j]) :
        i += 1
    while (i < length1 and j < length2 and l[i] == listToFind[j]) :
        i += 1
        j += 1
    if (j == length2) :
        return i - length2
    return -1

def swapLists(l, u) :
    #Input : two lists
    #Preconditions : -
    #Output : l, u
    #Postconditions : -
    #Swaps two given lists
    
    length1 = len(l)
    length2 = len(u)

    temp = list(l)
    del l[ : ]
    for i in range(length2) :
        l.append(u[i])
    del u[ : ]
    for i in range(length1) :
        u.append(temp[i])

    
def copyList(source, dest) :
    #Input : two list
    #Preconditions :
    #Output : dest
    #Postconditions : -
    #Copies from source to dest
    
    length1 = len(source)

    del dest[ : ]
    for i in range(length1) :
        dest.append(source[i])