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
        setMsgLab("已选择人脸普通", "green")
        return 1
    elif tain == "人脸4G":
        setMsgLab("已选择人脸4G", "green")
        return 2

def judge(num1,num2,setMsgLab,file_path):   #num1代表设备类型   num2代表界面按钮
    orderNum = num1
    optionNum = num2
    if optionNum == 1:      #人脸普通
        if orderNum == 2:
            retSd = telnetfac.readfile(file_path)
            if retSd == 0:
                setMsgLab("检测SD卡正常", "green")
                return 0
            elif retSd == 1:
                setMsgLab("检测SD卡不正常", "red")
                return -1
            else:
                setMsgLab("获取SD卡信息失败，请点击重置工具！\n 重新检测", "red")
                return -1
        elif orderNum == 5:
             retWifi = telnetfac.readfile(file_path)
             if retWifi == 0:
                 setMsgLab("检测wifi正常", "green")
                 return 0
             elif retWifi == 1:
                 setMsgLab("检测WIFI不正常", "red")
                 return -1
             else:
                 setMsgLab("获取WIFI信息失败，请点击重置工具！\n 重新检测", "red")
                 return -1
        elif orderNum == 4:
             retProbe = telnetfac.readfile(file_path)

             if retProbe == 0:
                 setMsgLab("检测探针正常", "green")
                 return 0
             elif retProbe == 1:
                 setMsgLab("检测探针不正常", "red")
                 return -1
             else:
                 setMsgLab("获取探针信息失败，请点击重置工具！\n 重新检测", "red")
                 return -1
        elif orderNum == 1:
            retGps = telnetfac.readfile(file_path)
            if retGps == 0:
                setMsgLab("检测gps正常", "green")
                return 0
            elif retGps == 1:
                setMsgLab("检测GPS不正常", "red")
            else:
                setMsgLab("获取GPS信息失败，请点击重置工具！\n 重新检测", "red")
                return -1
        elif orderNum == 3:
            setMsgLab("无4G功能", "red")
            return -1
        elif orderNum == 6:  # 获取mac地址
            retMac = telnetfac4G.readfile(file_path)
        if len(retMac) > 10:
            for i in retMac:
                a = retMac[11]
                setMsgLab(a, "green")
        else:
            setMsgLab("获取mac失败,点击重置工具，重新获取", "red")
            return 0
    elif optionNum == 2:    #人脸4G
        if orderNum == 2:
            retSd = telnetfac4G.readfile(file_path)
            if retSd == 0:
                setMsgLab("检测SD卡正常", "green")
                return 0
            elif retSd == 1:
                setMsgLab("检测SD卡不正常", "red")
                return -1
            else:
                setMsgLab("获取SD卡信息失败，请点击重置工具！\n 重新检测", "red")
                return -1
        elif orderNum == 5:
                setMsgLab("无wifi功能", "red")
                return -1
        elif orderNum == 4:
            retProbe = telnetfac4G.readfile(file_path)
            if retProbe == 1:
                setMsgLab("检测探针正常", "green")
                return 0
            elif retProbe == 1:
                setMsgLab("检测探针不正常", "red")
            else:
                setMsgLab("获取探针信息失败，请点击重置工具！\n 重新检测", "red")
                return -1
        elif orderNum == 1:
            retGps = telnetfac4G.readfile(file_path)
            if retGps == 1:
                setMsgLab("检测GPS正常", "green")
                return 0
            elif retGps == 1:
                setMsgLab("检测GPS不正常", "red")
            else:
                setMsgLab("获取GPS信息失败，请点击重置工具！\n 重新检测", "red")
                return -1
        elif orderNum == 3:
            ret4G = telnetfac4G.readfile(file_path)
            if ret4G == 1:
                setMsgLab("检测4G正常","green")
            elif ret4G == 1:
                setMsgLab("检测4G不正常", "red")
            else:
                setMsgLab("获取4G信息失败，请点击重置工具！\n 重新检测", "red")
            return -1
        elif orderNum == 6:  # 获取mac地址
            retMac = telnetfac4G.readfile(file_path)
        if len(retMac) > 10:
            print("获取MAC地址")
            print(retMac)
            for i in retMac:
                a = retMac[11]
                setMsgLab(a, "green")
        else:
                setMsgLab("获取mac失败，点击重置工具，重新获取", "red")
                return 0
def testhost(host,setMsgLab):
    mountcmd1 = host
    mountcmd = 'mkdir /tmp/fac/;''mount -t nfs -o nolock '
    mountcmd2 =':/c/nfsroot /tmp/fac;\n'
    mountcmd3 = bytes(mountcmd+mountcmd1+mountcmd2,'utf-8') #字符串转字节
    print("已选择地址：",mountcmd3)
    print(len(mountcmd3))
    if len(mountcmd3) <= 61:
        setMsgLab("无地址", "red")
        return -0
    elif len(mountcmd3) <=74 and len(mountcmd3) >= 72:
        setMsgLab("已选择 本地地址 ", "blue")
        return mountcmd3
    else:
        setMsgLab("本地地址 无效", "red")
        return -1
