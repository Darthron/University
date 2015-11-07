'''
Created on Oct 27, 2015

@author: ratvel
'''

from Domain.domain import *
from Utility.utility import *

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

def testStringHasFormatWordIntegerWordInteger() :
    assert stringHasFormatWordIntegerWordInteger("insert 1 at -1", ["insert", "at"], True, False) == False
    assert stringHasFormatWordIntegerWordInteger("insert -1 at 1", ["insert", "at"], False, False) == False
    assert stringHasFormatWordIntegerWordInteger("inser -1 at 1", ["insert", "at"], True, False) == False
    assert stringHasFormatWordIntegerWordInteger("insert  -1 at 1", ["insert", "at"], True, False) == False
    assert stringHasFormatWordIntegerWordInteger("insert -1 at 1", ["insert", "at"], True, False) == True
    assert stringHasFormatWordIntegerWordInteger("insert 1 at 1", ["inser", "at"], True, False) == False

def testStringHasFormatWordInteger() :
    assert stringHasFormatWordInteger("add 1", "add", True) == True
    assert stringHasFormatWordInteger(" add 1", "add", True) == False
    assert stringHasFormatWordInteger("add -1", "ad", True) == False
    assert stringHasFormatWordInteger("add -1", "add", False) == False

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
    addCommand("insert -1 at 1", l)
    assert l == [-1, 1, 2, 3, 4]
    l = [1, 2, 3, 4]
    addCommand("insert 1 at 7", l)
    assert l == [1, 2, 3, 4]
    
def testFindSublist() :
    l1 = []
    l2 = [1]
    assert findSublist(l1, l2) == -1
    l1 = [1, 2]
    l2 = [3]
    assert findSublist(l1, l2) == -1
    l1 = [1, 2]
    l2 = [2, 3]
    assert findSublist(l1, l2) == -1
    l1 = [1, 2]
    l2 = [1]
    assert findSublist(l1, l2) == 0
    
def testGetList() :
    assert getList("1 2 3") == [1, 2, 3]
    assert getList("-1 1") == [-1, 1]
    
def testIndexOfFirstLetter() :
    assert indexOfFirstLetter("213a") == 3
    assert indexOfFirstLetter("~11") == -1
    assert indexOfFirstLetter("") == -1
    
def testStringIsNumbericUntilSpaceOrEnd() :
    assert stringIsNumericUntilSpaceOrEnd("1a ") == False
    assert stringIsNumericUntilSpaceOrEnd("11111") == True
    assert stringIsNumericUntilSpaceOrEnd("34 saa") == True

def testStringIsListOfIntegers() :
    assert stringIsListOfIntegers(" 1 2 3") == False
    assert stringIsListOfIntegers("1a 2 3") == False
    assert stringIsListOfIntegers("a 11 2") == False
    assert stringIsListOfIntegers("1  2") == False
    assert stringIsListOfIntegers("1 2 3") == True
    assert stringIsListOfIntegers("-5") == True

def testModifyCommand() :
    l = [1, 2, 3]
    assert modifyCommand("remove 1", l) == [2, 3]
    assert modifyCommand("replace 2 3 with 1 2 3 4 5", l) == [1, 2, 3, 4, 5]
    assert modifyCommand("remove from 3 to 5", l) == [1, 2]
    
def testCheckModifyCommand() :
    assert checkModifyCommand("replace 1 with") == False
    assert checkModifyCommand("replace 1 with 1") == True
    assert checkModifyCommand("remove 0") == False
    assert checkModifyCommand("replace 1 - 5 with 6") == False

def testCopyList() :
    l = [1, 2, 3]
    u = []
    copyList(l, u)
    assert u == l
    l = []
    u = [1, 2]
    copyList(l, u)
    assert u == l
    l = [1, 2, 3]
    u = [4, 5]
    copyList(l, u)
    assert u == l
    l = []
    u = []
    copyList(l, u)
    assert u == l

def testSwapLists() :
    l = []
    u = []
    swapLists(l, u)
    assert l == [] and u == []
    l = []
    u = [1]
    swapLists(l, u)
    assert l == [1]
    assert u == []
    l = [1, 2]
    u = []
    swapLists(l, u)
    assert l == []
    assert u == [1, 2]
    l = [1, 2]
    u = [2, 3]
    swapLists(l, u)
    assert l == [2, 3]
    assert u == [1, 2]

def testCheckUndoCommand() :
    assert checkUndoCommand("undo") == True
    assert checkUndoCommand("und") == False

def testUndoCommand() :
    l = [1, 2, 3]
    u = [1]
    undoCommand(l, u)
    assert l == [1]
    l = []
    u = [1, 2]
    undoCommand(l, u)
    assert l == [1, 2]

def testCheckRedoCommand() :
    assert checkRedoCommand("redo") == True
    assert checkRedoCommand("red") == False
