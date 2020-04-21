import time
import telnetlib

def checkSd(devhost, user, pwd, finish, mountCmd,i):
   # self.devHost, b'root', b'qwer1234', b' #', self.mountCmd, a, b
    devhost = '192.168.1.115'
    user = b'root'
    pwd = b'qwer1234'
    finish = b'#'
    mountCmd = b'mkdir /tmp/fac/;mount -t nfs -o nolock 192.168.1.56:/c/nfsroot/test_fac /tmp/fac;\n'
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

    if i == 1:
        print("wifiiiiiiiiiiiiidgshdgffffshsgdhghsdfhsdiiiiiiiiiiiiii")
        tn.write(b"chmod + x /tmp/fac/test_fac/fac_4G/test_fac_mac.sh;/tmp/fac/test_fac/fac_4G/test_fac_mac.sh;cp /tmp/mac_gain_report /tmp/fac/test_fac/mac_gain_report -f;sync;\n")
        tn.read_until(finish)
        time.sleep(2)
        tn.close()
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
        #else:
         #   return -1

    if -1 == i:
        print('no checkfile\n')
        return i
    print('sd_check_report %d' % i)
    return i
