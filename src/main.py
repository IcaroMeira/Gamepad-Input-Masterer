#!/bin/python3
from modules import choose_device as cdev
from modules import gim
from modules import utils

SAVED_DEVICE_FILE = "../data/saved_device.txt"
STANDARD_CONFIG = "../data/conf/standard_config.json"

def __main():
    utils.ensure_files(SAVED_DEVICE_FILE)
    device = 1
    ask_to_save = True
    while device == 1:
        device = cdev.load_saved_device(debug=True)
        if device == 1:
                device = cdev.choose_device(cdev.available_devices(), debug=True)
        else:
            ask_to_save = False
    if ask_to_save and utils.int_input_handler(
            text=f"Want to save {device.name}? (No)\n0 - No\n1 - Yes\n-> ",
            std=0):
        cdev.save_device(device)

    gim0 = gim.GIM(device)
    gim0.load_config(STANDARD_CONFIG)
    gim0.start()

if __name__ == "__main__":
    __main()
