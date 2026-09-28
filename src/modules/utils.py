#!/bin/python3
from json import dumps, load
from subprocess import run

def clear():
    run("clear")

def int_input_handler(text: str, min: int = 0, max: int = 1, std: int = None):
    while True:
        choice = input(text)
        if std != None and choice == "":
            return std
        elif(choice.isdigit() == True):
            if(int(choice) >= min and int(choice) <= max):
                return int(choice)
        clear()
        print(f"Input a valid choice between(inclusive) {min} and {max}.\n")

def ensure_files(*args: str):
    for file in args:
        try:
            f = open(file, "x")
            f.close()
        except FileExistsError:
            pass

def dict_json(dict: dict, file: str):
    ensure_files(file)
    with open(file, "w") as f:
        f.write(dumps(dict, indent=4))

def json_dict(file: str) -> dict:
    ensure_files(file)
    with open(file, "r") as f:
        return load(f)
