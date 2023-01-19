from array import *
import ctypes
import time

AwesomeKey = 0x21 #Your Dayz Interact Key Here (https://web.archive.org/web/20190801085838/http://www.gamespp.com/directx/directInputKeyboardScanCodes.html)
TimeBeforeStart = 4

SendInput = ctypes.windll.user32.SendInput

PUL = ctypes.POINTER(ctypes.c_ulong)

class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0,
                        ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def IncrementLock():
    time.sleep(0.4)
    PressKey(AwesomeKey)
    time.sleep(1.4)
    ReleaseKey(AwesomeKey)
    time.sleep(0.2)

def NextRow():
    time.sleep(0.4)
    PressKey(AwesomeKey)
    time.sleep(0.2)
    ReleaseKey(AwesomeKey)
    time.sleep(0.2)

def SwitchRow(pwd):
    i = 0
    if pwd[1] == 9 and pwd[2] == 9 and pwd[3] == 9:
        time.sleep(0.4)
        for i in range(3):
            NextRow()
            IncrementLock()
        NextRow()
        pwd[0] += 1
        pwd[1] = 0
        pwd[2] = 0
    elif pwd[2] == 9 and pwd[3] == 9:
        time.sleep(0.4)
        for i in range(2):
            NextRow()
        IncrementLock()
        NextRow()
        IncrementLock()
        NextRow()
        pwd[1] += 1
        pwd[2] += 1
        if pwd[2] == 10:
            pwd[2] = 0
    elif pwd[3] == 9:
        time.sleep(0.4)
        for i in range(3):
            NextRow()
        IncrementLock()
        NextRow()
        pwd[2] += 1
        if pwd[2] == 10:
            pwd[2] = 0
    pwd[3] = 0
    return (pwd)

if __name__ == '__main__':
    pwd = array('i', [0, 0, 0, 0])
    time.sleep(TimeBeforeStart)
    while True:
        PressKey(AwesomeKey)
        time.sleep(6.25)
        ReleaseKey(AwesomeKey)
        time.sleep(0.2)
        pwd[3] = 9
        pwd = SwitchRow(pwd)
