#!/bin/python3
from .global_vars import Keys as k, uinput as ui, KeyInput as ki
from evdev import UInput, ecodes

ui = UInput()

def simKeyPress(key):
    ui.write(ecodes.EV_KEY, key, 1)
    ui.write(ecodes.EV_KEY, key, 0)
    ui.syn()

def execFunc(KeyMaps):
    for mapKF in KeyMaps:
        mapKF = KeyMaps[mapKF]
        canExec = True
        if not ("NULL" in mapKF["dep"] or all(k[dep] for dep in mapKF["dep"])):
            canExec = False
        if "ALL" in mapKF["exc"]:
            if not all(k[exc] == 0 for exc in k if exc not in mapKF["dep"]):
                canExec = False
        elif not ("NULL" in mapKF["exc"] or all(k[exc] == 0 for exc in mapKF["exc"])):
            canExec = False
        if canExec:
            for func in mapKF["func"]:
                if func[0] == "{" and func[len(func)-1] == "}":
                    simKeyPress(ki[func])
                if func == "QUIT":
                    exit()
