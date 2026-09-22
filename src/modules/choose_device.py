#!/bin/python3
from evdev import InputDevice, list_devices
from subprocess import run
from .utils import *
from .global_vars import *

def listDevicesStr():
    devicesList = [InputDevice(path) for path in list_devices()]
    devlist = ""
    for index, device in enumerate(devicesList):
        devlist += f"{index} - {device.path}\t{device.name}\t{device.phys}\n"
    return devlist


def saveDevice(device) -> None:
    with open(saved_device_file, "w") as f:
        f.write(f"{device.info.vendor}:{device.info.product}")
        print(f"{device.info.vendor}:{device.info.product}")

def loadSavedDevice():
    id = ""
    with open(saved_device_file, "r") as f:
        id = f.read().split(":")
    for path in list_devices():
        dev = InputDevice(path)
        if(str(dev.info.vendor) == id[0] and str(dev.info.product) == id[1]):
            print(f"Loaded saved device {dev.name}")
            return dev
    return 0

def chooseDevice():
    while True:
        devices = [InputDevice(path) for path in list_devices()]
        if(len(devices) == 0):
            if(cmdIntInputHandler("No devices found.\n\nChoose how to continue:\n0 - Retry\n1 - Close\n-> ") == 1):
                return 2
        else:
            break
    choice = cmdIntInputHandler(f"{listDevicesStr()}{len(devices)} - Retry\n{len(devices)+1} - Close\nChoose a device by number\n-> ", 0, len(devices)+1)
    if(choice == len(devices)):
        return 1
    if(choice == len(devices)+1):
        return 2
    print(f"Choice: {devices[choice].name}\n")
    if cmdIntInputHandler(f"Want to save {devices[choice].name}?\n0 - No\n1 - Yes\n-> "):
        saveDevice(devices[choice])
    return devices[choice]

def __main():
    ensureFiles(saved_device_file)
    device = chooseDevice()

if __name__ == "__main__":
    __main()
