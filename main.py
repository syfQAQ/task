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
import facport
import tkinter.messagebox as messagebox
from tkinter import ttk
from multiprocessing import Process
import threading as thread

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.creteWidgets()
        self.file_path = 'C://nfsroot//test_fac//sd_check_report'


    def creteWidgets(self):
        self.msgLabVarStr = StringVar()
        self.msgLabVarStr.set('准备开始检测!')
        self.msgLabVarStr2 = StringVar()
        self.msgLabVarStr2.set('状态栏2')
        self.v = StringVar()    #前端ip 输入框
        self.v1 = StringVar()   #下拉框
        self.v3 = StringVar()   #本地ip 输入框

        fmMsg = Frame(self.master)
        fmMsg.pack(side=TOP, anchor=W, fill=X, expand=YES, pady=10)
        self.msgLable = Label(fmMsg, textvariable=self.msgLabVarStr, bg='white', font=('Arial', 16), width=60, height=6)
        self.msgLable.pack(side=TOP, fill=NONE, expand=YES)
        self.msgLable2 = Label(fmMsg, textvariable=self.msgLabVarStr2, bg='white', font=('Arial', 16), width=60, height=4)
        self.msgLable2.pack(side=TOP, fill=NONE, expand=YES)

        fmBtnFac = Frame(self.master)
        fmBtnFac.pack(side=TOP, anchor=W, fill=X, expand=YES, padx=12, ipadx=12, ipady=12)
        self.BtnTestNetWork = Button(fmBtnFac, text='检测GPS', activebackground="green", command=self.one)
        self.BtnTestNetWork.pack(side=LEFT, fill=X, expand=YES, ipadx=12, ipady=12, padx=12)

        self.BtnTestGps = Button(fmBtnFac, text='检测4G', activebackground="green",command=self.three)
        self.BtnTestGps.pack(side=LEFT, fill=X, expand=YES, ipadx=12, ipady=12, padx=12)
        self.BtnTestProbe = Button(fmBtnFac, text='检测探针', activebackground="green", command=self.four)
        self.BtnTestProbe.pack(side=LEFT, fill=X, expand=YES, ipadx=6, ipady=12, padx=12)
        self.BtnTestWifi = Button(fmBtnFac, text='检测WIFI', activebackground="green", command=self.five)
        self.BtnTestWifi.pack(side=LEFT, fill=X, expand=YES, ipadx=6, ipady=12, padx=12)
        self.BtnTestSd = Button(fmBtnFac, text='检测SD卡', activebackground="green", command=self.two)
        self.BtnTestSd.pack(side=LEFT, fill=X, expand=YES, ipadx=12, ipady=12, padx=12)
        self.BtnBurnMac = Button(fmBtnFac, text='获取mac', activebackground="green", command=self.six)
        self.BtnBurnMac.pack(side=LEFT, fill=X, expand=YES, ipadx=12, ipady=12, padx=12)

        fmBtnCus = Frame(self.master)
        fmBtnCus.pack(side=TOP, anchor=W, fill=X, expand=YES, pady=10, ipadx=8, ipady=8)
        self.boxlist = ttk.Combobox(fmBtnCus, width=10, textvariable=self.v1, state='readonly')
        self.boxlist.pack(side=LEFT, anchor=W, fill=X, expand=YES, ipadx=4, ipady=14, padx=2)

        self.boxlist['values'] = ('人脸普通', '人脸4G')
        self.boxlist.current(0)
        self.BtnClose = Button(fmBtnCus, text='选择', activebackground="green", command=self.obtain)
        self.BtnClose.pack(side=LEFT, fill=X, expand=NO, ipadx=6, ipady=8, padx=6)
        self.e = Entry(fmBtnCus, width=14, textvariable=self.v3)
        self.e.pack(side=LEFT, fill=X, expand=YES, ipadx=8, ipady=14, padx=12)
        self.v3.set(r'输入本地ip地址')
        self.BtnBurnApp = Button(fmBtnCus, text='选择', activebackground="green", command=self.LocalHost)
        self.BtnBurnApp.pack(side=LEFT, fill=X, expand=NO, ipadx=6, ipady=8, padx=5)
        self.e1 = Entry(fmBtnCus, width=14, textvariable=self.v)
        self.e1.pack(side=LEFT, fill=X, expand=YES, ipadx=8, ipady=14, padx=12)
        self.v.set(r'输入前端相机ip地址')  # 输入框默认值
        self.BtnBurnApp = Button(fmBtnCus, text='选择', activebackground="green", command=self.Host)
        self.BtnBurnApp.pack(side=LEFT, fill=X, expand=NO, ipadx=6, ipady=8, padx=5)
        self.BtnTest4G = Button(fmBtnCus, text='重置工具', activebackground="green",command=self.checkComplete)
        self.BtnTest4G.pack(side=LEFT, fill=X, expand=YES, ipadx=6, ipady=12, padx=12)

    def Host(self): #获取前端相机IP
        self.host = self.e1.get()
        if len(self.host) < 11:
            self.setMsgLab("地址无效", "red")
            return -1
        else:
            self.setMsgLab("已选择前端相机地址", "blue")
            self.devHost = self.host
            return self.devHost

    def LocalHost(self):#获取本地地址
        self.host = self.e.get()
        host = facport.testhost(self.host,self.setMsgLab)
        print(host)
        self.mountCmd = host
        return self.host

    def obtain(self):#获取设备类型（普通/4G）
        self.tain = self.boxlist.get()
        print(self.tain)
        self.option = facport.outPut(self.tain, self.setMsgLab)

    def one(self):      #代表GPS按钮
        a = self.testSd(1,self.option)
        return a
    def two(self):      #SD
        b = self.testSd(2, self.option)
        return b
    def three(self):    #4G
        c = self.testSd(3, self.option)
        return c
    def four(self):     #探针
        d = self.testSd(4, self.option)
        return d
    def five(self):     #WIFI
        e = self.testSd(5, self.option)
        return e
    def six(self):      #mac
        f = self.testSd(6, self.option)
        return f

    def testSd(self,a,b):
        self.setMsgLab("检测中", "yellow")
        if b == 1:
            retTelnet = telnetfac.checkSd(self.devHost, b'root', b'qwer1234', b' #', self.mountCmd, a, self.setMsgLab)
            retJudge = facport.judge(a, b, self.setMsgLab, self.file_path)
        elif b == 2:
            retTelnet = telnetfac4G.checkSd(self.devHost, b'root', b'qwer1234', b' #', self.mountCmd, a)
            retJudge = facport.judge(a, b, self.setMsgLab, self.file_path)

        if -1 == retTelnet:
            self.setMsgLab("电脑与设备网络连接失败", "red")
            return -1

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

    def setMsgLab2(self, msg, bgc):
        self.msgLabVarStr2.set(msg)
        self.msgLable.configure(bg=bgc)

if __name__ == '__main__':
    app = Application()
    app.master.iconbitmap(default=r'graceport.ico')  # 更改默认图标
    app.master.title("恩港摄相机测试工具")
    app.master.geometry("750x600")
    app.master.resizable(width=True, height=True)
    app.mainloop()