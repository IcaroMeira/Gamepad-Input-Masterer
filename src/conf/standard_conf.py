inps = {
    "[RB]": {
        "a": {
            "dep": ["LA_UP"],
            "exc": ["LB"],
            "func": ["{a}"]
        },
        "b": {
            "dep": ["LA_RIGHT"],
            "exc": ["LB"],
            "func": ["{b}"]
        },
        "h": {
            "dep": ["LA_DOWN"],
            "exc": ["LB"],
            "func": ["{h}"]
        },
        "f": {
            "dep": ["LA_LEFT"],
            "exc": ["LB"],
            "func": ["{f}"]
        },
        "0": {
            "dep": ["LA_UP", "LB"],
            "exc": ["NULL"],
            "func": ["{0}"]
        },
        "5": {
            "dep": ["LA_DOWN", "LB"],
            "exc": ["NULL"],
            "func": ["{5}"]
        },
        "t": {
            "dep": ["LA_RIGHT", "LB"],
            "exc": ["NULL"],
            "func": ["{t}"]
        },
        "w": {
            "dep": ["LA_LEFT", "LB"],
            "exc": ["NULL"],
            "func": ["{w}"]
        }
    },

    "[Y]": {
        "e": {
            "dep": ["LA_UP"],
            "exc": ["LB"],
            "func": ["{e}"]
        },
        "c": {
            "dep": ["LA_RIGHT"],
            "exc": ["LB"],
            "func": ["{c}"]
        },
        "g": {
            "dep": ["LA_DOWN"],
            "exc": ["LB"],
            "func": ["{g}"]
        },
        "j": {
            "dep": ["LA_LEFT"],
            "exc": ["LB"],
            "func": ["{j}"]
        },
        "1": {
            "dep": ["LA_UP", "LB"],
            "exc": ["NULL"],
            "func": ["{1}"] },
        "6": {
            "dep": ["LA_DOWN", "LB"],
            "exc": ["NULL"],
            "func": ["{6}"]
        },
        "v": {
            "dep": ["LA_RIGHT", "LB"],
            "exc": ["NULL"],
            "func": ["{v}"]
        }
    },

    "[B]": {
        "i": {
            "dep": ["LA_UP"],
            "exc": ["LB"],
            "func": ["{i}"]
        },
        "d": {
            "dep": ["LA_RIGHT"],
            "exc": ["LB"],
            "func": ["{d}"]
        },
        "l": {
            "dep": ["LA_DOWN"],
            "exc": ["LB"],
            "func": ["{l}"]
        },
        "k": {
            "dep": ["LA_LEFT"],
            "exc": ["LB"],
            "func": ["{k}"]
        },
        "2": {
            "dep": ["LA_UP", "LB"],
            "exc": ["NULL"],
            "func": ["{2}"]
        },
        "7": {
            "dep": ["LA_DOWN", "LB"],
            "exc": ["NULL"],
            "func": ["{7}"]
        },
        "x": {
            "dep": ["LA_RIGHT", "LB"],
            "exc": ["NULL"],
            "func": ["{x}"]
        }
    },

    "[A]": {
        "o": {
            "dep": ["LA_UP"],
            "exc": ["LB"],
            "func": ["{o}"]
        },
        "p": {
            "dep": ["LA_RIGHT"],
            "exc": ["LB"],
            "func": ["{p}"]
        },
        "m": {
            "dep": ["LA_DOWN"],
            "exc": ["LB"],
            "func": ["{m}"]
        },
        "r": {
            "dep": ["LA_LEFT"],
            "exc": ["LB"],
            "func": ["{r}"]
        },
        "3": {
            "dep": ["LA_UP", "LB"],
            "exc": ["NULL"],
            "func": ["{3}"]
        },
        "8": {
            "dep": ["LA_DOWN", "LB"],
            "exc": ["NULL"],
            "func": ["{8}"]
        },
        "y": {
            "dep": ["LA_RIGHT", "LB"],
            "exc": ["NULL"],
            "func": ["{y}"]
        }
    },

    "[X]": {
        "u": {
            "dep": ["LA_UP"],
            "exc": ["LB"],
            "func": ["{u}"]
        },
        "q": {
            "dep": ["LA_RIGHT"],
            "exc": ["LB"],
            "func": ["{q}"]
        },
        "n": {
            "dep": ["LA_DOWN"],
            "exc": ["LB"],
            "func": ["{n}"]
        },
        "s": {
            "dep": ["LA_LEFT"],
            "exc": ["LB"],
            "func": ["{s}"]
        },
        "4": {
            "dep": ["LA_UP", "LB"],
            "exc": ["NULL"],
            "func": ["{4}"]
        },
        "9": {
            "dep": ["LA_DOWN", "LB"],
            "exc": ["NULL"],
            "func": ["{9}"]
        },
        "z": {
            "dep": ["LA_RIGHT", "LB"],
            "exc": ["NULL"],
            "func": ["{z}"]
        }
    },
    "[START]": {
            "main": {
                "dep": ["NULL"],
                "exc": ["ALL"],
                "func": ["QUIT"]
                }
            }
}

