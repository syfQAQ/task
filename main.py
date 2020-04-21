#!/usr/bin/env python
# -*- coding: utf-8 -*-
#摄像机出货测试工具
import time
import os
import numpy as np
from tkinter import *
import time
import os
from tkinter import *
import telnetfac
import telnetfac4G
import telnetcar
import telnetcardh
import facport
import tkinter.messagebox as messagebox
from tkinter import ttk
from multiprocessing import Process

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.creteWidgets()

        #self.devHost = '192.168.1.115'
        self.mountCmd = b'mkdir /tmp/fac/;mount -t nfs -o nolock 192.168.1.56:/c/nfsroot/test_fac /tmp/fac;\n'
        self.file_path = 'C://nfsroot//test_fac//sd_check_report'
        #self.file_path = 'C://nfsroot//test_fac//mac_gain_report'


    def creteWidgets(self):
        self.msgLabVarStr = StringVar()
        self.msgLabVarStr.set('准备开始检测！')
        self.msgLabVarStr2 = StringVar()
        self.msgLabVarStr2.set('状态栏2')
        self.v = StringVar()
        self.v1 = StringVar()

        fmMsg = Frame(self.master)
        fmMsg.pack(side=TOP, anchor=W, fill=X, expand=YES, pady=10)
        self.msgLable = Label(fmMsg, textvariable=self.msgLabVarStr, bg='white', font=('Arial', 16), width=60, height=6)
        self.msgLable.pack(side=TOP, fill=NONE, expand=YES)
        self.msgLable2 = Label(fmMsg, textvariable=self.msgLabVarStr2, bg='white', font=('Arial', 16), width=60, height=4)
        self.msgLable2.pack(side=TOP, fill=NONE, expand=YES)

        fmBtnFac = Frame(self.master)
        fmBtnFac.pack(side=TOP, anchor=W, fill=X, expand=YES, padx=12, ipadx=12, ipady=12)
        self.BtnTestNetWork = Button(fmBtnFac, text='检查GPS', command=self.one)
        self.BtnTestNetWork.pack(side=LEFT, fill=X, expand=YES, ipadx=12, ipady=12, padx=12)
        self.BtnTestSd = Button(fmBtnFac, text='检查SD卡', command=self.two)
        self.BtnTestSd.pack(side=LEFT, fill=X, expand=YES, ipadx=12, ipady=12, padx=12)
        self.BtnTestGps = Button(fmBtnFac, text='检查4G', command=self.three)
        self.BtnTestGps.pack(side=LEFT, fill=X, expand=YES, ipadx=12, ipady=12, padx=12)
        self.boxlist = ttk.Combobox(fmBtnFac, textvariable=self.v1, state='readonly')
        self.boxlist.pack(side=LEFT, anchor=W, fill=X, expand=NO, ipady=13)

        self.boxlist['values'] = ('人脸普通', '人脸4G', 'GP_BAT_1', 'GP_BAT_2')
        self.boxlist.current(0)
        self.BtnClose = Button(fmBtnFac, text='选择', command=self.obtain)
        self.BtnClose.pack(side=LEFT, fill=X, expand=NO, ipadx=6, ipady=8, padx=6)

        fmBtnCus = Frame(self.master)
        fmBtnCus.pack(side=TOP, anchor=W, fill=X, expand=YES, pady=10, ipadx=8, ipady=8)
        self.BtnTestProbe = Button(fmBtnCus, text='检查探针', command=self.four)
        self.BtnTestProbe.pack(side=LEFT, fill=X, expand=YES, ipadx=12, ipady=12, padx=12)
        self.BtnTestWifi = Button(fmBtnCus, text='检查WIFI', command=self.five)
        self.BtnTestWifi.pack(side=LEFT, fill=X, expand=YES, ipadx=12, ipady=12, padx=12)
        self.e1 = Entry(fmBtnCus, textvariable=self.v)
        self.e1.pack(side=LEFT, fill=X, expand=NO, ipadx=8, ipady=12, padx=12)
        self.BtnBurnApp = Button(fmBtnCus, text='选择', command=self.Host)
        self.BtnBurnApp.pack(side=LEFT, fill=X, expand=NO, ipadx=6, ipady=8, padx=5)
        self.BtnTest4G = Button(fmBtnCus, text='重置工具', command=self.checkComplete)
        self.BtnTest4G.pack(side=LEFT, fill=X, expand=YES, ipadx=12, ipady=12, padx=12)
        self.e1 = Entry(fmBtnCus, textvariable=self.v)
        self.BtnBurnMac = Button(fmBtnCus, text='获取mac', command=self.six)
        self.BtnBurnMac.pack(side=LEFT, fill=X, expand=NO, ipadx=6, ipady=8, padx=6)

    #self.host = self.e1.get()
       # len1 = len(self.host)
        #if (len1 > 13):
        #    self.setMsgLab("输入地址错误", "red")
       # else:
          #  self.setMsgLab("已更改地址", "green")

    #def Host(self):
        #top = Toplevel()
        #v1 = StringVar()
        #e1 = Entry(top, textvariable=v1, width=10)
        #e1.grid(row=10, column=5, padx=0, pady=0)
        #Button(top, text='确认地址').grid(row=1, column=1, padx=1, pady=1)
        #Button(top, text='确认地址')

    def Host(self):
        self.host = self.e1.get()
        if len(self.host) < 11:
            self.setMsgLab("地址无效", "red")
            return -1
        else:
            self.setMsgLab("已选择地址", "blue")
            self.devHost = self.host
            return self.devHost

    def obtain(self):
        self.tain = self.boxlist.get()
        print(self.tain)
        self.option = facport.outPut(self.tain, self.setMsgLab)
        print(self.option)

    def one(self):
        a = self.testSd(1,self.option)
        return a

    def two(self):
        b = self.testSd(2, self.option)
        return b

    def three(self):
        c = self.testSd(3, self.option)
        return c
    def four(self):
        d = self.testSd(4, self.option)
        return d
    def five(self):
        e = self.testSd(5, self.option)
        return e
    def six(self):
        f = self.testSd(6, self.option)
        return f

    def testSd(self,a,b):
        self.setMsgLab("检查中", "yellow")

        retTelnet = telnetfac.checkSd(self.devHost, b'root', b'qwer1234', b' #', self.mountCmd,a)
        retJudge = facport.judge(a, b, self.setMsgLab, self.file_path)
        #retTelnet = telnetfac4G.checkSd(self.devHost, b'root', b'qwer1234', b' #', self.mountCmd, a)
        if -1 == retTelnet:
            self.setMsgLab("电脑与设备网络连接失败", "red")
            return -1

        #retJudge = facport.judge(a,b,self.setMsgLab,self.file_path)

    def checkComplete(self):
        try:
            if os.path.exists(self.file_path):
                print('remove file %s' % self.file_path)
                os.remove(self.file_path)
        except Exception as e:
            print("remove file fail:", e)
            messagebox.showinfo('message', '手动删除文件 %s' % self.file_path)

        self.msgLable.configure(bg='white')
        self.msgLabVarStr.set("准备开始检测")
        self.msgLable2.configure(bg='white')
        self.msgLabVarStr2.set("状态栏2")

    def setMsgLab(self, msg, bgc):
        self.msgLabVarStr.set(msg)
        self.msgLable.configure(bg=bgc)



if __name__ == '__main__':
    app = Application()
    app.master.iconbitmap(default=r'graceport.ico')  # 更改默认图标
    app.master.title("恩港摄相机测试工具")
    app.master.geometry("750x600")
    app.master.resizable(width=True, height=True)
    app.mainloop()