import time
import telnetlib
import requests
import json
import os
def checkSd(devhost, user, pwd, finish, mountCmd,i,setMsgLab):
    MsgLab = setMsgLab
    try:
        tn = telnetlib.Telnet(devhost, port=23, timeout=3)
    except Exception as e:
        print("Connect device timeout, 设备网络连接超时:", e)
        return -1

    tn.read_until(b'login: ')
    tn.write(user+b'\n')
    tn.read_until(b'Password: ')
    tn.write(pwd+b'\n')
    tn.read_until(finish)

    tn.write(mountCmd)
    tn.read_until(finish)

    if i == 2:
        print("sd检测中")
        MsgLab("检测中", "yellow")
        tn.write(b"chmod + x /tmp/fac/test_fac/fac_common/test_fac_sd.sh;/tmp/fac/test_fac/fac_common/test_fac_sd.sh;cp /tmp/sd_check_report /tmp/fac/test_fac/sd_check_report -f;sync;\n")
        tn.read_until(finish)
        time.sleep(2)
        tn.close()
        return 0

    if i == 5:
        print("wifi检测中")
        MsgLab("检测中", "yellow")
        tn.write(b"chmod + x /tmp/fac/test_fac/fac_common/test_fac_wifi.sh;/tmp/fac/test_fac/fac_common/test_fac_wifi.sh;cp /tmp/sd_check_report /tmp/fac/test_fac/sd_check_report -f;sync;\n")
        tn.read_until(finish)
        time.sleep(2)
        tn.close()
        return 0

    elif i == 4:
        print("probe检测中")
        tn.write(b"chmod + x /tmp/fac/test_fac/fac_common/test_fac_probe.sh;/tmp/fac/test_fac/fac_common/test_fac_probe.sh;cp /tmp/sd_check_report /tmp/fac/test_fac/sd_check_report -f;sync;\n")
        tn.read_until(finish)
        time.sleep(2)
        tn.close()
        return 0

    elif i == 1:
        print("GPS检测中")
        tn.write(b"chmod + x /tmp/fac/test_fac/fac_common/test_fac_gps.sh;/tmp/fac/test_fac/fac_common/test_fac_gps.sh;cp /tmp/sd_check_report /tmp/fac/test_fac/sd_check_report -f;sync;\n")
        tn.read_until(finish)
        time.sleep(3)
        tn.close()
        return 0

    elif i == 6:
        print("mac 获取中")
        tn.write(b"chmod + x /tmp/fac/test_fac/fac_common/test_fac_mac.sh;/tmp/fac/test_fac/fac_common/test_fac_mac.sh;cp /tmp/sd_check_report /tmp/fac/test_fac/sd_check_report -f;sync;\n")
        tn.read_until(finish)
        time.sleep(2)
        tn.close()
        return 0
    return 0

def readfile(file_path):
    i = -1
    try:
        with open(file_path, 'r') as file:
            i = int(file.read())
    except Exception as e:
        print("read file_path fail:", e)
        a = str(e)
        print(len(a))
        a1 = a.split()
        return a1

    if -1 == i:
        print('no checkfile\n')
        return i
    print('sd_check_report %d' % i)
    return i
