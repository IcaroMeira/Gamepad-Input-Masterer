#!/bin/python3
from subprocess import run

def clear():
    run("clear")

def cmdIntInputHandler(Text, Min = 0, Max = 1):
    while True:
        choice = input(Text)
        if(choice.isdigit() == True):
            if(int(choice) >= Min and int(choice) <= Max):
                return int(choice)
        clear()
        print(f"Input a valid choice between(inclusive) {Min} and {Max}.\n")

def ensureFiles(*args):
    for file in args:
        try:
            f = open(file, "x")
            f.close()
        except FileExistsError:
            pass
