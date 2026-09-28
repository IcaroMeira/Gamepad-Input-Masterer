#!/bin/python3
from evdev import ecodes, UInput

from modules import lookup_tables as lut
from modules import utils

ck = lut.CodeKeys
cva = lut.CodeValueAbs
ki = lut.KeyInput

class Keys():
    def __init__(self):
        self.LB = 0
        self.LT = 0
        self.RB = 0
        self.RT = 0
        self.Y = 0
        self.B = 0
        self.A = 0
        self.X = 0
        self.SELECT = 0
        self.START = 0
        self.LAB = 0
        self.RAB = 0
        self.UP = 0
        self.RIGHT = 0
        self.DOWN = 0
        self.LEFT = 0
        self.LA_UP = 0
        self.LA_RIGHT = 0
        self.LA_DOWN = 0
        self.LA_LEFT = 0
        self.RA_UP = 0
        self.RA_RIGHT = 0
        self.RA_DOWN = 0
        self.RA_LEFT = 0
        self.NULL = 1

class GIM():
    def __init__(self, device):
        self.device = device
        self.config = None
        self.keys = Keys()
        self.down_keys = dict((k, []) for k in Keys().__dict__)
        self.ui = UInput()

    def load_config(self, conf: str):
        self.config = utils.json_dict(conf)

    def sim_key_press(self, key_func, key):
        self.ui.write(ecodes.EV_KEY, key_func, 1)
        self.ui.syn()
        self.down_keys[key].append(key_func)

    def clear_key_press(self, key):
        for k in self.down_keys[key]:
            self.ui.write(ecodes.EV_KEY, k, 0)
            self.ui.syn()
        self.down_keys[key] = []

    def exec_func(self, func, key):
        if func.startswith("{") and func.endswith("}"):
            self.sim_key_press(ki[func], key)
        elif func == "QUIT":
            quit()

    def check_deps(self, deps, keys):
        if "NULL" in deps or all(keys[dep] for dep in deps):
            return 0
        return 1

    def check_excs(self, deps, excs, indeps, keys):
        if "ALL" in excs:
            if all(keys[exc] == 0
                    for exc in keys
                    if exc not in deps and exc not in indeps
                    ):
                return 0
        elif "NULL" in excs or all(keys[exc] == 0 for exc in excs):
            return 0
        return 1

    def handle_func(self, key, value):
        if not value:
            for k in key:
                self.clear_key_press(k)
            return

        key = key[0]
        section = self.config.get(f"[{key}]")

        if not section:
            return

        for _, func_conf in section.items():
            deps = [*func_conf["dep"], key]
            excs = func_conf["exc"]
            indeps = func_conf["indep"]

            keys = self.keys.__dict__

            if self.check_deps(deps, keys):
                continue

            if self.check_excs(deps, excs, indeps, keys):
                continue

            for func in func_conf["func"]:
                self.exec_func(func, key)

    def start(self):
        for event in self.device.read_loop():
            if event.type == ecodes.EV_KEY:
                match event.code:
                    case 310:
                        self.keys.LB = event.value
                        self.handle_func(ck[event.code], event.value)
                    case 312:
                        self.keys.LT = event.value
                        self.handle_func(ck[event.code], event.value)
                    case 311:
                        self.keys.RB = event.value
                        self.handle_func(ck[event.code], event.value)
                    case 313:
                        self.keys.RT = event.value
                        self.handle_func(ck[event.code], event.value)
                    case 308:
                        self.keys.Y = event.value
                        self.handle_func(ck[event.code], event.value)
                    case 305:
                        self.keys.B = event.value
                        self.handle_func(ck[event.code], event.value)
                    case 304:
                        self.keys.A = event.value
                        self.handle_func(ck[event.code], event.value)
                    case 307:
                        self.keys.X = event.value
                        self.handle_func(ck[event.code], event.value)
                    case 314:
                        self.keys.SELECT = event.value
                        self.handle_func(ck[event.code], event.value)
                    case 315:
                        self.keys.START = event.value
                        self.handle_func(ck[event.code], event.value)
                    case 317:
                        self.keys.LAB = event.value
                        self.handle_func(ck[event.code], event.value)
                    case 318:
                        self.keys.RAB = event.value
                        self.handle_func(ck[event.code], event.value)
            if event.type == ecodes.EV_ABS:
                match event.code:
                    case 17:
                        if event.value == -1:
                            self.keys.UP = 1
                            self.keys.DOWN = 0
                        elif event.value == 1:
                            self.keys.UP = 0
                            self.keys.DOWN = 1
                        else:
                            self.keys.UP = 0
                            self.keys.DOWN = 0

                        self.handle_func(
                                cva[event.code][event.value],
                                0 if not event.value else 1)

                    case 16:
                        if event.value == 1:
                            self.keys.RIGHT = 1
                            self.keys.LEFT = 0
                        elif event.value == -1:
                            self.keys.RIGHT = 0
                            self.keys.LEFT = 1
                        else:
                            self.keys.RIGHT = 0
                            self.keys.LEFT = 0

                        self.handle_func(
                                cva[event.code][event.value],
                                0 if not event.value else 1)

                    case 1:
                        if event.value <= 64:
                            self.keys.LA_UP = 1
                            self.keys.LA_DOWN = 0
                        elif event.value >= 192:
                            self.keys.LA_UP = 0
                            self.keys.LA_DOWN = 1
                        else:
                            self.keys.LA_UP = 0
                            self.keys.LA_DOWN = 0

                        self.handle_func(
                                cva[event.code][
                                    -1 if event.value <= 64 
                                    else 1 if event.value >= 192 
                                    else 0], 
                                0 if event.value >= 64 and event.value <= 192 else 1)

                    case 0:
                        if event.value >= 192:
                            self.keys.LA_RIGHT = 1
                            self.keys.LA_LEFT = 0
                        elif event.value <= 64:
                            self.keys.LA_RIGHT = 0
                            self.keys.LA_LEFT = 1
                        else:
                            self.keys.LA_RIGHT = 0
                            self.keys.LA_LEFT = 0

                        self.handle_func(
                                cva[event.code][
                                    -1 if event.value <= 64 
                                    else 1 if event.value >= 192 
                                    else 0], 
                                0 if event.value >= 64 and event.value <= 192 else 1)

                    case 5:
                        if event.value <= 64:
                            self.keys.RA_UP = 1
                            self.keys.RA_DOWN = 0
                        elif event.value >= 192:
                            self.keys.RA_UP = 0
                            self.keys.RA_DOWN = 1
                        else:
                            self.keys.RA_UP = 0
                            self.keys.RA_DOWN = 0

                        self.handle_func(
                                cva[event.code][
                                    -1 if event.value <= 64 
                                    else 1 if event.value >= 192 
                                    else 0],
                                0 if event.value >= 64 and event.value <= 192 else 1)

                    case 2:
                        if event.value >= 192:
                            self.keys.RA_RIGHT = 1
                            self.keys.RA_LEFT = 0
                        elif event.value <= 64:
                            self.keys.RA_RIGHT = 0
                            self.keys.RA_LEFT = 1
                        else:
                            self.keys.RA_RIGHT = 0
                            self.keys.RA_LEFT = 0

                        self.handle_func(
                                cva[event.code][
                                    -1 if event.value <= 64 
                                    else 1 if event.value >= 192 
                                    else 0],
                                0 if event.value >= 64 and event.value <= 192 else 1)
