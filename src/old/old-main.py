#!/bin/python3
import modules.global_vars as gv
from modules.function_handler import execFunc, clearKey
from modules.choose_device import loadSavedDevice, chooseDevice
from evdev import ecodes
from conf.standard_conf import inps as conf
from modules.utils import clear, ensureFiles

k = gv.Keys
ck = gv.CodeKeys
cva = gv.CodeValueAbs
cvdp = gv.CodeValueDPad

def mainLoop():
    for ev in gv.device.read_loop():
        if ev.type == ecodes.EV_KEY:
            if ev.code in ck:
                if f"[{ck[ev.code]}]" in conf:
                    execFunc(conf[f"[{ck[ev.code]}]"], ev.value, ck[ev.code])
                match ev.code:
                    case 310:
                        k["LB"] = ev.value
                    case 312:
                        k["LT"] = ev.value
                    case 311:
                        k["RB"] = ev.value
                    case 313:
                        k["RT"] = ev.value
                    case 308:
                        k["Y"] = ev.value
                    case 305:
                        k["B"] = ev.value
                    case 304:
                        k["A"] = ev.value
                    case 307:
                        k["X"] = ev.value
                    case 314:
                        k["SELECT"] = ev.value
                    case 315:
                        k["START"] = ev.value
                    case 317:
                        k["LAB"] = ev.value
                    case 318:
                        k["RAB"] = ev.value
        elif ev.type == ecodes.EV_ABS:
            if ev.code in cva:
                if ev.code in cvdp:
                    for ckey in cvdp[ev.code][ev.value]:
                        if f"[{ckey}]" in conf:
                            execFunc(conf[f"[{ckey}]"], 1 if ev.value != 0 else 0, ev.code)
                match ev.code:
                    case 17:
                        if ev.value == -1:
                            k["UP"] = 1
                        elif ev.value == 1:
                            k["DOWN"] = 1
                        else:
                            k["UP"] = 0
                            k["DOWN"] = 0
                    case 16:
                        if ev.value == 1:
                            k["RIGHT"] = 1
                        elif ev.value == -1:
                            k["LEFT"] = 1
                        else:
                            k["RIGHT"] = 0
                            k["LEFT"] = 0
                    case 1:
                        if ev.value <= 64:
                            k["LA_UP"] = 1
                        elif ev.value >= 192:
                            k["LA_DOWN"] = 1
                        else:
                            k["LA_UP"] = 0
                            k["LA_DOWN"] = 0
                    case 0:
                        if ev.value >= 192:
                            k["LA_RIGHT"] = 1
                        elif ev.value <= 64:
                            k["LA_LEFT"] = 1
                        else:
                            k["LA_RIGHT"] = 0
                            k["LA_LEFT"] = 0
                    case 5:
                        if ev.value <= 64:
                            k["RA_UP"] = 1
                        elif ev.value >= 192:
                            k["RA_DOWN"] = 1
                        else:
                            k["RA_UP"] = 0
                            k["RA_DOWN"] = 0
                    case 2:
                        if ev.value >= 192:
                            k["RA_RIGHT"] = 1
                        elif ev.value <= 64:
                            k["RA_LEFT"] = 1
                        else:
                            k["RA_RIGHT"] = 0
                            k["RA_LEFT"] = 0

def __main():
    ensureFiles(gv.saved_device_file)
    while True:
        dev = loadSavedDevice()
        if not(dev):
            dev = chooseDevice()
            if dev == 2:
                quit()
            elif not dev == 1:
                gv.device = dev
                break
        else:
            gv.device = dev
            break
    mainLoop()

if __name__ == "__main__":
    __main()
