import serial
import serial.tools.list_ports
import time
import telnetlib
import telnetfac
import telnetfac4G
import requests
import json

def outPut(tain, setMsgLab):
    if tain == "人脸普通":
        setMsgLab("已选择人脸普通", "blue")
        return 1
    elif tain == "人脸4G":
        setMsgLab("已选择人脸4G", "blue")
        return 2
    elif tain == "GP_BAT_1":
        setMsgLab("已选择车牌东舜", "blue")
        return 3
    elif tain == "GP_BAT_2":
        setMsgLab("已选择车牌", "blue")
        return 4


def judge(num1,num2,setMsgLab,file_path):
    orderNum = num1
    optionNum = num2
    if optionNum == 1:
        if orderNum == 2:
            retSd = telnetfac.readfile(file_path)
            if retSd == 0:
                setMsgLab("sd卡正常", "green")
                return 0
            else:
                setMsgLab("sd卡不正常", "red")
                return -1
        elif orderNum == 5:
             retWifi = telnetfac.readfile(file_path)
             if retWifi == 0:
                 setMsgLab("wifi正常", "green")
                 return 0
             else:
                 setMsgLab("wifi不正常", "red")
                 return -1
        elif orderNum == 4:
             retProbe = telnetfac.readfile(file_path)
             if retProbe == 1:
                 setMsgLab("探针正常", "green")
                 return 0
             else:
                 setMsgLab("探针不正常", "red")
                 return -1
        elif orderNum == 1:
            retGps = telnetfac.readfile(file_path)
            if retGps == 1:
                setMsgLab("gps正常", "green")
                return 0
            else:
                setMsgLab("gps不正常", "red")
                return -1
        elif orderNum == 3:
            setMsgLab("无4G功能", "red")
            return -1
        elif orderNum == 6:  # 获取mac地址
            retMac = telnetfac4G.readfile(file_path)
        if len(retMac) > 1:
            print("66666666666666666")
            print(retMac)
            for i in retMac:
                a = retMac[11]
                setMsgLab(a, "green")
        else:
            setMsgLab("获取失败", "red")
        return 0

    elif optionNum == 2:
        if orderNum == 2:
            retSd = telnetfac4G.readfile(file_path)
            if retSd == 0:
                setMsgLab("sd卡正常", "green")
                return 0
            else:
                setMsgLab("sd卡不正常", "red")
                return -1
        elif orderNum == 5:
            retWifi = telnetfac4G.readfile(file_path)
            if retWifi == 0:
                setMsgLab("无wifi功能", "red")
                return 0
        elif orderNum == 4:
            retProbe = telnetfac4G.readfile(file_path)
            if retProbe == 1:
                setMsgLab("探针正常", "green")
                return 0
            else:
                setMsgLab("探针不正常", "red")
                return -1
        elif orderNum == 1:
            retGps = telnetfac4G.readfile(file_path)
            if retGps == 1:
                setMsgLab("gp正常", "green")
                return 0
            else:
                setMsgLab("gps不正常", "red")
                return -1
        elif orderNum == 3:
            setMsgLab("无4G功能", "red")
            return -1
        '''elif orderNum == 1:  #获取mac地址
            retGps = telnetfac4G.readfile(file_path)
            if len(retGps) > 1:
                print("66666666666666666")
                print(retGps)
                for i in retGps:
                    a = retGps[11]
                print(a)
                setMsgLab(a, "green")
                return 0'''


