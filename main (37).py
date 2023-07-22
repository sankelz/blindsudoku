import random
from termcolor import colored, cprint

def blindsudoku():
    return printy(8)

def printy(number):
    numlist = []
    for x in range(number):
        num = random.randint(0, 9)
        numlist.append(num)
    return numlist

def ans1ver(ans1, oop):
    if 3 in oop:
        ans1 = 5
    if 5 in oop:
        ans1 = 9
    if 4 in oop or 2 in oop:
        ans1 = 8
    if 1 in oop or 7 in oop:
        ans1 = 2 or ans1 == 4
    if 6 in oop:
        ans1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    if 9 in oop:
        ans1 = "unsolvable"
    if ans1 == False or ans1 is None:
        return "WRONG!! try again ig HAHAHA"
    else:
        return "this is actually surprisingly correct"

oop = blindsudoku()
print('welcome to a simple game of blind sudoku')
print("if you lose you're toast ( ´ ∀ ` )ﾉ ")
cprint('yes', 'yellow', attrs=[])
query = str(input("?"))
if query == 'yes':
    print("great! here are the rules")
    print("one: you will be given eight out of nine numbers")
    cprint('ok and', 'green', attrs=[])
    query2 = str(input("?"))
else:
    print("wrong answer. try again (－_－) zzZ")
if query2 == 'ok and':
    print("two: you have 1 guess to find out how to make all numbers equal 9")
    cprint("what's the kicker", 'red', attrs=[])
    query3 = str(input("?"))
else:
    print("i don't like you. don't play")
if query3 == "what's the kicker":
    print("three: this is not like regular sudoku. you don't just have to add")
    print("the numbers. subtraction, multiplication, division; everything goes.")
    cprint(oop, 'cyan', attrs=[])
    print("the ninth number can be anything from 0 to 9.")
else:
    print("nnnnnnothing. have fun!")
    cprint(oop, 'black', attrs=[])
    print("the ninth number can be anything from 0 to 9.")

ans1 = int(input("your guess is?"))
print(ans1ver(ans1, oop))
print("this is the end of blind sudoku. play again sometime!")
