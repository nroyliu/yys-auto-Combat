#coding=utf-8
import os

def getSrcreenCap():
    result = os.system("cd platform-tools && adb shell /system/bin/screencap -p /sdcard/screenshot.png"
                       " && adb pull /sdcard/screenshot.png ../screencap/screencap.png")
    return result
if __name__ == '__main__':
    result = getSrcreenCap()
    print(result)