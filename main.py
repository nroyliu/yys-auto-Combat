#coding=utf-8
import os
import time

import aircv as ac

def getSrcreenCap():
    result = os.system("cd platform-tools && adb shell /system/bin/screencap -p /sdcard/screenshot.png"
                       " && adb pull /sdcard/screenshot.png ../screencap/screencap.png")
    return result
def findImg(obj,find,all="false"):
    imgobj = ac.imread(obj)
    imgfind = ac.imread(find)
    if(all == "true"):
        result = ac.find_all_template(imgobj, imgfind, 0.9)
    else:
        result = ac.find_template(imgobj, imgfind, 0.9)
    return result
if __name__ == '__main__':
    # os.system("cd platform-tools && adb shell input tap 500 500")
    while(1):
        getSrcreenCap()
        isRoom = findImg("screencap/screencap.png","images/leaveteam.png")
        isInvite = findImg("screencap/screencap.png", "images/isinvite.png")
        isCombat = findImg("screencap/screencap.png", "images/face.png")
        isWin = findImg("screencap/screencap.png", "images/win.png")
        isDefeated = findImg("screencap/screencap.png", "images/upyuhun.png")
        isDamo = findImg("screencap/screencap.png", "images/damo.png")
        isOpenDamo = findImg("screencap/screencap.png", "images/opendamo.png")
        if(isRoom):
            isRoomCount = findImg("screencap/screencap.png","images/invite.png","true")
            print("房间内"+str(3-len(isRoomCount))+"人")
            if((3-len(isRoomCount))>1):
                print("倒计时3秒开始")
                print("======>"+str(3))
                time.sleep(0.5)
                print("======>"+str(2))
                time.sleep(0.5)
                print("======>"+str(1))
                start = findImg("screencap/screencap.png","images/start.png")
                if(start):
                    x = start['result'][0]
                    y = start['result'][1]
                    os.system("cd platform-tools && adb shell input tap "+str(x)+" "+str(y))
                else:
                    print("不在房间")

        elif(isCombat):
            print("战斗中")
            isStart = findImg("screencap/screencap.png", "images/ready.png")
            if(isStart):
                print("自动准备")
                x = isStart['result'][0]
                y = isStart['result'][1]
                os.system("cd platform-tools && adb shell input tap "+str(x)+" "+str(y))
            time.sleep(2)
        elif(isWin):
            print("战斗胜利")
            os.system("cd platform-tools && adb shell input tap 200 350")

        elif (isDefeated):
            print("战斗失败")
            os.system("cd platform-tools && adb shell input tap 200 350")

        elif(isInvite):
            print("邀请队友")
            accept = findImg("screencap/screencap.png", "images/accept.png")
            if(accept):
                x = accept['result'][0]
                y = accept['result'][1]
                os.system("cd platform-tools && adb shell input tap " + str(x) + " " + str(y))
            time.sleep(1)

        elif(isDamo):
            print("奖励未打开")
            os.system("cd platform-tools && adb shell input tap 200 350")


        elif(isOpenDamo):
            print("奖励已打开")
            os.system("cd platform-tools && adb shell input tap 200 350")


