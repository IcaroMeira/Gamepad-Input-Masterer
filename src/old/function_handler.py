#!/bin/python3
from .global_vars import Keys as k, uinput as ui, KeyInput as ki, DownKeysList as dkl, CodeKeys as ck
from evdev import UInput, ecodes

ui = UInput()

def simKeyPress(key, keycode):
    ui.write(ecodes.EV_KEY, key, 1)
    ui.syn()
    dkl[ck[keycode]].append(key)

def clearKey(keycode):
    for k in dkl[ck[keycode]]:
        ui.write(ecodes.EV_KEY, k, 0)
        ui.syn()
    dkl[ck[keycode]] = []

def handleFunc(func, state, keycode):
    if func[0] == "{" and func[len(func)-1] == "}":
        simKeyPress(ki[func], keycode)
    if func == "QUIT":
        exit()

def execFunc(keyfuncs, value, keycode):
    if not value:
        clearKey(keycode)
    else:
        for mapKF in keyfuncs:
            mapKF = keyfuncs[mapKF]
            if not ("NULL" in mapKF["dep"] or all(k[dep] for dep in mapKF["dep"])):
                continue
            if "ALL" in mapKF["exc"]:
                if not all(k[exc] == 0 for exc in k if exc not in mapKF["dep"]):
                    continue
            elif not ("NULL" in mapKF["exc"] or all(k[exc] == 0 for exc in mapKF["exc"])):
                continue
            for func in mapKF["func"]:
                handleFunc(func, value, keycode)
