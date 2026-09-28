#!/bin/python3
from evdev      import InputDevice, list_devices
from subprocess import run
from modules import utils

SAVED_DEVICE_FILE = "../data/saved_device.txt"

# Return a indexed list of devices as string
def list_devices_str() -> str:
    devices = [InputDevice(path) for path in list_devices()]
    devlist = ""
    for index, device in enumerate(devices):
        devlist += f"{index} - {device.path}\t{device.name}\t{device.phys}\n"
    return devlist

# Saves or replaces a device in the data folder
def save_device(device, debug: bool = False) -> int:
    try:
        with open(SAVED_DEVICE_FILE, "w") as f:
            f.write(f"{device.info.vendor}:{device.info.product}")
        if debug:
            print(f"Saved device: {device.name} successfully.")
        return 0
    except:
        return 1

# Try to load device saved in data folder
# Returns 1 if failed
# Returns saved device if succeed
def load_saved_device(debug: bool = False):
    id = ""
    try:
        with open(SAVED_DEVICE_FILE, "r") as f:
            id = f.read().split(":")
    except:
        return 1
    for path in list_devices():
        device = InputDevice(path)
        if(str(device.info.vendor) == id[0] and str(device.info.product) == id[1]):
            if debug:
                print(f"Loaded device: {device.name}")
            return device
    return 1

# Looks for devices available or ask to proceed if no devices are found.
# Returns 2 if quit is chosen
# Returns a list of inputed devices if succeed
def available_devices():
    while True:
        devices = [InputDevice(path) for path in list_devices()]
        if(len(devices) == 0):
            if utils.int_input_handler(
                    text="No devices found.\n\n0 - Retry\n1 - Close\nChoose how to continue (Retry)\n-> ",
                    std=0) == 1:
                return 2
        else:
            return devices

# Ask user which device use in a list of inputed devices
# Returns 1 if retry is chosen
# Quits if quit is chosen
# Returns a device if a device is chosen
def choose_device(devices, debug: bool = False):
    len_devices = len(devices)
    choice = utils.int_input_handler(
            text=f"{list_devices_str()}{len_devices} - Retry\n{len_devices+1} - Close\n\nChoose an option (Retry)\n-> ",
            min=0,
            max=len_devices+1,
            std=len_devices)
    if(choice == len_devices):
        return 1
    elif(choice == len_devices+1):
        quit()
    if debug:
        print(f"Choose: {devices[choice].name}\n")
    return devices[choice]

def __main():
    utils.ensure_files(SAVED_DEVICE_FILE)
    device = 1
    ask_to_save = True
    while device == 1:
        device = load_saved_device(debug=True)
        if device == 1:
                device = choose_device(available_devices(), debug=True)
        else:
            ask_to_save = False
    if ask_to_save and utils.int_input_handler(
            text=f"Want to save {device.name}? (No)\n0 - No\n1 - Yes\n-> ",
            std=0):
        save_device(device)

if __name__ == "__main__":
    __main()
