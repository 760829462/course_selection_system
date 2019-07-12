# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author Lu.zehao

import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import pickle
import pymysql
import time
import re

def zhu_jie_mian(no= '', name= '', old_wnd=''):
    '''主界面'''
    global shou_ye
    shou_ye = tk.Tk()#建立窗口
    shou_ye.title('选课系统——主界面')#标题
    # shou_ye.geometry('600x400')#设立界面大小

    # 设置窗口大小
    width = 600
    height = 400
    # 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
    screenwidth = shou_ye.winfo_screenwidth()
    screenheight = shou_ye.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    shou_ye.geometry(alignstr)

    shou_ye.resizable(width=False, height=False)  # 窗口尺寸不可变化

    #标签——选课系统
    tk.Label(shou_ye, text='选课系统', fg='red', font=('Arial', 25), width=30, height=2).pack()
    # 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高

    #按钮1——学生登入端
    tk.Button(shou_ye, text='学生端', font=('Arial', 20), width=8, height=1, command = lambda:jie_mian_geng_ti(xue_sheng_deng_ru, shou_ye)).place(x=120, y=170)

    #按钮2——教师登入端
    tk.Button(shou_ye, text='教师端', font=('Arial', 20), width=8, height=1, command = lambda:jie_mian_geng_ti(jiao_shi_deng_ru, shou_ye)).place(x=330, y=170)

    #按钮3——管理员登入端
    tk.Button(shou_ye, text='管理员', font=('Arial', 20), width=8, height=1, command = lambda:jie_mian_geng_ti(guan_li_yuan_deng_ru, shou_ye)).place(x=230, y=280)

    shou_ye.mainloop()#主窗口循环显示

def xue_sheng_deng_ru(no= '', name= '', old_wnd=''):
    '''学生登入端'''
    global xue_sheng
    xue_sheng = tk.Tk()#建立窗口
    xue_sheng.title('选课系统——学生登入端')#标题
    # xue_sheng.geometry('600x400')#设立界面大小

    # 设置窗口大小
    width = 600
    height = 400
    # 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
    screenwidth = xue_sheng.winfo_screenwidth()
    screenheight = xue_sheng.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    xue_sheng.geometry(alignstr)

    xue_sheng.resizable(width=False, height=False)  # 窗口尺寸不可变化

    #标签——登入窗口
    tk.Label(xue_sheng, text='学号:', font=('Arial', 14)).place(x=150, y=100)
    tk.Label(xue_sheng, text='密码:', font=('Arial', 14)).place(x=150, y=150)

    #输入学号
    global zhang_hao
    zhang_hao = StringVar()
    Entry(xue_sheng, textvariable=zhang_hao, font=('Arial', 14)).place(x=210, y=100)
    # 输入密码
    global mi_ma
    mi_ma = StringVar()
    entry_mi_ma = tk.Entry(xue_sheng, textvariable=mi_ma,font=('Arial', 14), show='*')
    entry_mi_ma.place(x=210, y=150)

    #标签——学生登入
    tk.Label(xue_sheng, text='学生登入', fg='red', font=('Arial', 25), width=30, height=2).pack()#标签放置
    # 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高

    #按钮1——登入
    tk.Button(xue_sheng, text='登入', font=('Arial', 10), width=8, height=1, command = lambda:deng_ru(zhang_hao.get(), mi_ma.get(), 1)).place(x=190, y=200)

    #按钮2——注册
    tk.Button(xue_sheng, text='注册', font=('Arial', 10), width=8, height=1, command = lambda:jie_mian_geng_ti(zhu_ce_duan, xue_sheng, old_wnd_hanshu = 1)).place(x=330, y=200)

    #按钮3——返回
    tk.Button(xue_sheng, text='返回首页', font=('Arial', 15), width=8, height=1, command = lambda:jie_mian_geng_ti(zhu_jie_mian, xue_sheng)).place(x=250, y=280)

    xue_sheng.mainloop()#主窗口循环显示

def jiao_shi_deng_ru(no= '', name= '', old_wnd=''):
    '''教师登入端'''
    global jiao_shi
    jiao_shi = tk.Tk()#建立窗口
    jiao_shi.title('选课系统——教师登入端')#标题
    # jiao_shi.geometry('600x400')#设立界面大小

    # 设置窗口大小
    width = 600
    height = 400
    # 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
    screenwidth = jiao_shi.winfo_screenwidth()
    screenheight = jiao_shi.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    jiao_shi.geometry(alignstr)

    jiao_shi.resizable(width=False, height=False)  # 窗口尺寸不可变化

    #标签——登入窗口
    tk.Label(jiao_shi, text='教工号:', font=('Arial', 14)).place(x=150, y=100)
    tk.Label(jiao_shi, text='密    码:', font=('Arial', 14)).place(x=150, y=150)

    #输入教工号
    zhang_hao = tk.StringVar()
    entry_zhang_hao = tk.Entry(jiao_shi, textvariable=zhang_hao, font=('Arial', 14))
    entry_zhang_hao.place(x=220, y=100)
    # 输入密码
    mi_ma = tk.StringVar()
    entry_mi_ma = tk.Entry(jiao_shi, textvariable=mi_ma, font=('Arial', 14), show='*')
    entry_mi_ma.place(x=220, y=150)


    #标签——教师登入
    jiao_shi_biaoqian_1 = tk.Label(jiao_shi, text='教师登入', fg='red', font=('Arial', 25), width=30, height=2).pack()
    # 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高

    #按钮1——登入
    tk.Button(jiao_shi, text='登入', font=('Arial', 10), width=8, height=1, command = lambda:deng_ru(zhang_hao.get(), mi_ma.get(), 2)).place(x=190, y=200)

    #按钮2——注册
    tk.Button(jiao_shi, text='注册', font=('Arial', 10), width=8, height=1, command = lambda:jie_mian_geng_ti(zhu_ce_duan, jiao_shi, old_wnd_hanshu = 2, name=name, no=no)).place(x=330, y=200)

    #按钮3——返回
    tk.Button(jiao_shi, text='返回首页', font=('Arial', 15), width=8, height=1, command = lambda:jie_mian_geng_ti(zhu_jie_mian, jiao_shi)).place(x=250, y=280)

    jiao_shi.mainloop()#主窗口循环显示

def guan_li_yuan_deng_ru(no= '', name= '', old_wnd=''):
    '''管理员登入端'''
    global guan_li_yuan
    guan_li_yuan = tk.Tk()#建立窗口
    guan_li_yuan.title('选课系统——管理员登入端')#标题
    # guan_li_yuan.geometry('600x400')#设立界面大小

    # 设置窗口大小
    width = 600
    height = 400
    # 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
    screenwidth = guan_li_yuan.winfo_screenwidth()
    screenheight = guan_li_yuan.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    guan_li_yuan.geometry(alignstr)

    guan_li_yuan.resizable(width=False, height=False)  # 窗口尺寸不可变化

    #标签——登入窗口
    tk.Label(guan_li_yuan, text='账号:', font=('Arial', 14)).place(x=150, y=100)
    tk.Label(guan_li_yuan, text='密码:', font=('Arial', 14)).place(x=150, y=150)

    #输入帐号
    zhang_hao = tk.StringVar()
    entry_zhang_hao = tk.Entry(guan_li_yuan, textvariable=zhang_hao, font=('Arial', 14))
    entry_zhang_hao.place(x=220, y=100)
    # 输入密码
    mi_ma = tk.StringVar()
    entry_mi_ma = tk.Entry(guan_li_yuan, textvariable=mi_ma, font=('Arial', 14), show='*')
    entry_mi_ma.place(x=220, y=150)


    #标签——管理员登入
    guan_li_yuan_biaoqian_1 = tk.Label(guan_li_yuan, text='管理员登入', fg='red', font=('Arial', 25), width=30, height=2)
    # 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高

    guan_li_yuan_biaoqian_1.pack()#标签放置

    #按钮1——登入
    an_niu_1 = tk.Button(guan_li_yuan, text='登入', font=('Arial', 10), width=8, height=1, command = lambda :deng_ru(entry_zhang_hao.get(), entry_mi_ma.get(), 3))

    an_niu_1.place(x=250, y=200)#按钮1放置


    #按钮3——返回
    tk.Button(guan_li_yuan, text='返回首页', font=('Arial', 15), width=8, height=1, command = lambda:jie_mian_geng_ti(zhu_jie_mian, guan_li_yuan)).place(x=240, y=280)

    guan_li_yuan.mainloop()#主窗口循环显示

def guan_li_yuan_duan(no= '', name= '', old_wnd=''):
    ''''''
    global guan_li_yuan
    guan_li_yuan = tk.Tk()  # 建立窗口
    guan_li_yuan.title('选课系统——管理员中心')  # 标题
    guan_li_yuan.geometry('600x400')  # 设立界面大小

    # 设置窗口大小
    width = 600
    height = 400
    # 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
    screenwidth = guan_li_yuan.winfo_screenwidth()
    screenheight = guan_li_yuan.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    guan_li_yuan.geometry(alignstr)

    guan_li_yuan.resizable(width=False, height=False)  # 窗口尺寸不可变化

    xue_sheng_lie_biao = tk.Listbox(guan_li_yuan, width=80, height=2)
    jiao_shi_lie_biao = tk.Listbox(guan_li_yuan, width=80, height=2)

    # 为表添加内容
    db = pymysql.connect('localhost', 'root', '123456', 'course selection system')  # mysql    本机   账户  密码   表名
    cur = db.cursor()

    sql_1 = "select * from student_information"
    sql_2 = "select * from teacher_information"

    try:
        cur.execute(sql_1)
        db.commit()
        xue_sheng_xin_xi = cur.fetchall()

        cur.execute(sql_2)
        db.commit()
        jiao_shi_xin_xi = cur.fetchall()

        def align(str1, distance, alignment='left'):
            length = len(str1.encode('gbk'))
            space_to_fill = distance - length if distance > length else 0
            if alignment == 'left':
                str1 = str1 + ' ' * space_to_fill
            elif alignment == 'right':
                str1 = ' ' * space_to_fill + str1
            elif alignment == 'center':
                str1 = ' ' * (distance // 2) + str1 + ' ' * (distance - distance // 2)
            return str1

        for a_a in range(len(xue_sheng_xin_xi)):
            b_b = (align(xue_sheng_xin_xi[a_a][0], 20) + align(xue_sheng_xin_xi[a_a][1], 10) + align(xue_sheng_xin_xi[a_a][2], 20) + align(xue_sheng_xin_xi[a_a][3], 10) + align(xue_sheng_xin_xi[a_a][4], 10)+ align(xue_sheng_xin_xi[a_a][5], 30))
            xue_sheng_lie_biao.insert(END, b_b)

        for a_a in range(len(jiao_shi_xin_xi)):
            c_c = (align(jiao_shi_xin_xi[a_a][0], 20) + align(jiao_shi_xin_xi[a_a][1], 10) + align(jiao_shi_xin_xi[a_a][3], 20) + align(jiao_shi_xin_xi[a_a][2], 10) + align(jiao_shi_xin_xi[a_a][4], 10)+ align(jiao_shi_xin_xi[a_a][5], 30))

            jiao_shi_lie_biao.insert(END, c_c)

    except Exception as e:
        db.rollback()
        print(str(e))

    xue_sheng_lie_biao.place(x=20, y=50, width=560, height=80)
    jiao_shi_lie_biao.place(x=20, y=200, width=560, height=80)



    # 创建一个方法用于按钮的点获取点击事件
    def print_selection(duan_kou):
        value = duan_kou.get(duan_kou.curselection())  # 获取当前选中的文本

        value = re.match(r"^\d+", value).group()
        db = pymysql.connect('localhost', 'root', '123456', 'course selection system')  # mysql    本机   账户  密码   表名
        cur = db.cursor()

        sql_4 = "delete from `course selection system`.student_information where Sno='%s'" % (value)
        sql_1 = "delete from `course selection system`.stc_information where Sno='%s'" % (value)

        sql_5 = "delete from `course selection system`.teacher_information where Tno='%s'" % (value)
        sql_3 = "delete from `course selection system`.course_information where Tno='%s'" % (value)
        sql_2 = "delete from `course selection system`.stc_information where Tno='%s'" % (value)

        if duan_kou == xue_sheng_lie_biao:
            try:
                cur.execute(sql_1)
                db.commit()
                cur.execute(sql_4)
                db.commit()

                tkinter.messagebox.showinfo(message='删除成功！')
                duan_kou.delete(ACTIVE)

            except Exception as e:
                db.rollback()
                print(str(e))
        elif duan_kou == jiao_shi_lie_biao:
            try:
                try:
                    cur.execute(sql_2)
                    db.commit()
                except Exception as e:
                    db.rollback()
                    print(str(e))
                cur.execute(sql_3)
                db.commit()
                cur.execute(sql_5)
                db.commit()

                tkinter.messagebox.showinfo(message='删除成功！')
                duan_kou.delete(ACTIVE)

            except Exception as e:
                db.rollback()
                print(str(e))

    # 创建一个按钮，点击按钮调用print_selection函数
    tk.Button(guan_li_yuan, text='删除该条数据', font=('Arial', 10), width=10, height=1, command=lambda :print_selection(xue_sheng_lie_biao)).place(x=240, y=150)
    tk.Button(guan_li_yuan, text='删除该条数据', font=('Arial', 10), width=10, height=1, command=lambda :print_selection(jiao_shi_lie_biao)).place(x=240, y=300)

    # 按钮3——返回
    tk.Button(guan_li_yuan, text='返回', font=('Arial', 12), width=8, height=1, command=lambda: jie_mian_geng_ti(guan_li_yuan_deng_ru, guan_li_yuan)).place(x=450, y=330)

    tk.Label(guan_li_yuan, text='学生信息：', font=('Arial', 12), width=10, height=1).place(x=20, y=20)
    tk.Label(guan_li_yuan, text='教师信息：', font=('Arial', 12), width=10, height=1).place(x=20, y=170)
    guan_li_yuan.mainloop()  # 主窗口循环显示

def xue_sheng_duan(no= '', name= '', old_wnd=''):
    '''学生选课端'''
    global xue_sheng_xuan_ke
    xue_sheng_xuan_ke = tk.Tk()  # 建立窗口
    xue_sheng_xuan_ke.title('选课系统——学生选课中心')  # 标题
    xue_sheng_xuan_ke.geometry('600x400')  # 设立界面大小

    # 设置窗口大小
    width = 600
    height = 400
    # 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
    screenwidth = xue_sheng_xuan_ke.winfo_screenwidth()
    screenheight = xue_sheng_xuan_ke.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    xue_sheng_xuan_ke.geometry(alignstr)

    xue_sheng_xuan_ke.resizable(width=False, height=False)  # 窗口尺寸不可变化

    # 标签——选课系统
    tk.Label(xue_sheng_xuan_ke, text='学生选课中心', fg='red', font=('Arial', 25), width=30, height=2).place(x=20, y=-10)

    tk.Label(xue_sheng_xuan_ke, text="欢迎!%s"%(name), font=('Arial', 14), width=10, height=1).place(x=15, y=10)

    #标签——可选课程
    tk.Label(xue_sheng_xuan_ke, text='可选课程：', font=('Arial', 14), width=8, height=1).place(x=20, y=50)

    # 标签——课程信息
    tk.Label(xue_sheng_xuan_ke, text='课程代码                     课程名                           学分              授课老师', font=('Arial', 10), width=60, height=1).place(x=5, y=85)

    # 创建变量，用ke_cheng_xin_xi用来接收鼠标点击具体选项的内容
    ke_cheng_xin_xi = tk.StringVar()

    # 课程列表
    mu_biao = tk.Listbox(xue_sheng_xuan_ke, width=80, height=2)

    # 为表添加内容
    db = pymysql.connect('localhost', 'root', '123456', 'course selection system')  # mysql    本机   账户  密码   表名
    cur = db.cursor()

    sql_1 = "select * from course_information "

    try:
        cur.execute(sql_1)
        db.commit()
        yuan_su = cur.fetchall()

        def align(str1, distance, alignment='left'):
            length = len(str1.encode('gbk'))
            space_to_fill = distance - length if distance > length else 0
            if alignment == 'left':
                str1 = str1 + ' ' * space_to_fill
            elif alignment == 'right':
                str1 = ' ' * space_to_fill + str1
            elif alignment == 'center':
                str1 = ' ' * (distance // 2) + str1 + ' ' * (distance - distance // 2)
            return str1

        for a_a in range(len(yuan_su)):
            b_b = (align(yuan_su[a_a][0], 25)+align(yuan_su[a_a][1], 30)+align(yuan_su[a_a][2], 25)+align(yuan_su[a_a][3], 25))
            mu_biao.insert(END, b_b)

    except Exception as e:
        db.rollback()
        print(str(e))

    mu_biao.place(x=20, y=110, width=560, height=130)

    # 创建一个方法用于按钮的点获取点击事件
    def print_selection():
        value = mu_biao.get(mu_biao.curselection())  # 获取当前选中的文本

        value = re.match(r"^\d+", value).group()

        db = pymysql.connect('localhost', 'root', '123456', 'course selection system')  # mysql    本机   账户  密码   表名
        cur = db.cursor()

        sql_1 = "select * from `course selection system`.course_information where Cno='%s'" % (value)

        try:
            cur.execute(sql_1)
            db.commit()
            que_ren_xuan_ke_yuan_su = cur.fetchall()

        except Exception as e:
            db.rollback()
            print(str(e))

        xuan_ke(que_ren_xuan_ke_yuan_su[0][0], que_ren_xuan_ke_yuan_su[0][1], que_ren_xuan_ke_yuan_su[0][4], que_ren_xuan_ke_yuan_su[0][3], no, name)


    # 创建一个按钮，点击按钮调用print_selection函数
    tk.Button(xue_sheng_xuan_ke, text='选择该课', font=('Arial', 12), width=15, height=2, command=print_selection).place(x=100, y=260)

    #按钮——查看已选课程
    tk.Button(xue_sheng_xuan_ke, text='查看已选课程', font=('Arial', 12), width=15, height=2, command= lambda :jie_mian_geng_ti(xue_sheng_yi_xuan_duan, xue_sheng_xuan_ke, xue_sheng_duan, name=name, no=no)).place(x=350, y=260)

    # 按钮3——返回
    tk.Button(xue_sheng_xuan_ke, text='返回', font=('Arial', 15), width=8, height=1, command=lambda: jie_mian_geng_ti(xue_sheng_deng_ru, xue_sheng_xuan_ke)).place(x=250, y=330)

    xue_sheng_xuan_ke.mainloop()  # 主窗口循环显示

def xuan_ke(cno, cname, tno, tname, sno, sname):
    '''学生选课后，将课程/教师/学生信息添加进表'''
    # 为表添加内容
    db = pymysql.connect('localhost', 'root', '123456', 'course selection system')  # mysql    本机   账户  密码   表名
    cur = db.cursor()

    sql_1 = "INSERT INTO `course selection system`.`stc_information` (`Cno`, `Cname`, `Tno`, `Tname`, `Sno`, `Sname`) VALUES ('%s', '%s', %s, '%s', '%s', '%s')" % (cno, cname, tno, tname, sno, sname)

    try:
        cur.execute(sql_1)
        db.commit()

        tkinter.messagebox.showinfo(message='选课成功！')

    except Exception as e:
        db.rollback()
        print(str(e))

def xue_sheng_yi_xuan_duan(no= '', name= '', old_wnd=''):
    '''已选课程端'''
    global yi_xuan_ke_cheng
    yi_xuan_ke_cheng = tk.Tk()  # 建立窗口
    yi_xuan_ke_cheng.title('选课系统——已选课程')  # 标题
    yi_xuan_ke_cheng.geometry('600x400')  # 设立界面大小

    # 设置窗口大小
    width = 600
    height = 400
    # 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
    screenwidth = yi_xuan_ke_cheng.winfo_screenwidth()
    screenheight = yi_xuan_ke_cheng.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    yi_xuan_ke_cheng.geometry(alignstr)

    yi_xuan_ke_cheng.resizable(width=False, height=False)  # 窗口尺寸不可变化

    # 标签——选课系统
    tk.Label(yi_xuan_ke_cheng, text='已选课程', fg='red', font=('Arial', 25), width=30, height=2).pack()

    # 标签——可选课程
    tk.Label(yi_xuan_ke_cheng, text='已选课程：', font=('Arial', 14), width=8, height=1).place(x=20, y=60)

    tk.Label(yi_xuan_ke_cheng, text='课程代码                     课程名                         教师号                    授课老师', font=('Arial', 10), width=60, height=1).place(x=5, y=110)
    # 课程列表
    mu_biao = tk.Listbox(yi_xuan_ke_cheng, width=80, height=2)

    # 为表添加内容
    db = pymysql.connect('localhost', 'root', '123456', 'course selection system')  # mysql    本机   账户  密码   表名
    cur = db.cursor()

    sql_1 = "select * from stc_information where Sno=%s"%(no)

    try:
        cur.execute(sql_1)
        db.commit()
        yuan_su = cur.fetchall()

        def align(str1, distance, alignment='left'):
            length = len(str1.encode('gbk'))
            space_to_fill = distance - length if distance > length else 0
            if alignment == 'left':
                str1 = str1 + ' ' * space_to_fill
            elif alignment == 'right':
                str1 = ' ' * space_to_fill + str1
            elif alignment == 'center':
                str1 = ' ' * (distance // 2) + str1 + ' ' * (distance - distance // 2)
            return str1

        for a_a in range(len(yuan_su)):
            b_b = (align(yuan_su[a_a][0], 25) + align(yuan_su[a_a][1], 30) + align(yuan_su[a_a][2], 25) + align(
                yuan_su[a_a][3], 25))
            mu_biao.insert(END, b_b)

    except Exception as e:
        db.rollback()
        print(str(e))

    mu_biao.place(x=20, y=135, width=560, height=150)

    def tui_xuan():
        '''退选'''
        value = mu_biao.get(mu_biao.curselection())  # 获取当前选中的文本

        value = re.match(r"^\d+", value).group()

        db = pymysql.connect('localhost', 'root', '123456', 'course selection system')  # mysql    本机   账户  密码   表名
        cur = db.cursor()

        sql_1 = "select * from `course selection system`.stc_information where Cno='%s'" % (value)

        try:
            cur.execute(sql_1)
            db.commit()
            que_ren_xuan_ke_yuan_su = cur.fetchall()

        except Exception as e:
            db.rollback()
            print(str(e))

        cno = que_ren_xuan_ke_yuan_su[0][0]

        db = pymysql.connect('localhost', 'root', '123456', 'course selection system')  # mysql    本机   账户  密码   表名
        cur = db.cursor()

        sql_1 = "delete from `course selection system`.stc_information where Cno='%s' and Sno='%s'" % (cno, no)

        try:
            cur.execute(sql_1)
            db.commit()
            tkinter.messagebox.showinfo(message='退选成功！')
            mu_biao.delete(ACTIVE)

        except Exception as e:
            db.rollback()
            print(str(e))

    # 创建一个按钮，点击按钮调用print_selection函数
    tk.Button(yi_xuan_ke_cheng, text='退选该课', font=('Arial', 12), width=15, height=2, command= tui_xuan ).place(x=90, y=320)

    # 返回
    tk.Button(yi_xuan_ke_cheng, text='返回', font=('Arial', 12), width=15, height=2, command=lambda:jie_mian_geng_ti(xue_sheng_duan, yi_xuan_ke_cheng, name=name, no=no)).place(x=320, y=320)

    yi_xuan_ke_cheng.mainloop()  # 主窗口循环显示

def jiao_shi_duan(no= '', name= '', old_wnd=''):
    '''教师编辑课程端'''
    global jiao_shi_pai_ke
    jiao_shi_pai_ke = tk.Tk()  # 建立窗口
    jiao_shi_pai_ke.title('选课系统——教师中心')  # 标题
    jiao_shi_pai_ke.geometry('600x400')  # 设立界面大小

    # 设置窗口大小
    width = 600
    height = 400
    # 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
    screenwidth = jiao_shi_pai_ke.winfo_screenwidth()
    screenheight = jiao_shi_pai_ke.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    jiao_shi_pai_ke.geometry(alignstr)

    jiao_shi_pai_ke.resizable(width=False, height=False)  # 窗口尺寸不可变化

    # 标签——选课系统
    tk.Label(jiao_shi_pai_ke, text='教师中心', fg='red', font=('Arial', 25), width=30, height=2).place(x=20, y=-10)

    tk.Label(jiao_shi_pai_ke, text="欢迎!%s" % (name), font=('Arial', 14), width=10, height=1).place(x=15, y=10)

    #标签——可选课程
    tk.Label(jiao_shi_pai_ke, text='已开设课程：', font=('Arial', 14), width=10, height=1).place(x=20, y=50)

    #标签——课程信息
    tk.Label(jiao_shi_pai_ke, text='课程代码                               课程名                                                学分', font=('Arial', 10), width=60, height=1).place(x=5, y=80)

    # 创建一个方法用于按钮的点获取点击事件
    def print_selection():
        value = mu_biao.get(mu_biao.curselection())  # 获取当前选中的文本

        value= re.match(r"^\d+", value).group()

        db = pymysql.connect('localhost', 'root', '123456', 'course selection system')  # mysql    本机   账户  密码   表名
        cur = db.cursor()

        sql_1 = "delete from `course selection system`.course_information where Cno='%s'" % (value)
        sql_2 = "delete from `course selection system`.stc_information where Cno='%s'" % (value)

        try:
            cur.execute(sql_1)
            db.commit()
            cur.execute(sql_2)
            db.commit()
            tkinter.messagebox.showinfo(message='删除成功！')
            mu_biao.delete(ACTIVE)

        except Exception as e:
            db.rollback()
            print(str(e))

    # 创建变量，用ke_cheng_xin_xi用来接收鼠标点击具体选项的内容
    ke_cheng_xin_xi = tk.StringVar()

    # 课程列表
    mu_biao = tk.Listbox(jiao_shi_pai_ke, width=80, height=2)

    #为表添加内容
    db = pymysql.connect('localhost', 'root', '123456', 'course selection system')  # mysql    本机   账户  密码   表名
    cur = db.cursor()

    sql_1 = "select * from course_information where Tno='%s'" % (no)

    def align(str1, distance, alignment='left'):
        length = len(str1.encode('gbk'))
        space_to_fill = distance - length if distance > length else 0
        if alignment == 'left':
            str1 = str1 + ' ' * space_to_fill
        elif alignment == 'right':
            str1 = ' ' * space_to_fill + str1
        elif alignment == 'center':
            str1 = ' ' * (distance // 2) + str1 + ' ' * (distance - distance // 2)
        return str1

    try:
        cur.execute(sql_1)
        db.commit()
        yuan_su = cur.fetchall()
        for a_a in range(len(yuan_su)):
            b_b = (align(yuan_su[a_a][0], 30)+align(yuan_su[a_a][1], 50)+align(yuan_su[a_a][2], 30))
            mu_biao.insert(END, b_b)

    except Exception as e:
        db.rollback()
        print(str(e))

    mu_biao.place(x=20, y=110, width=560, height=130)


    # 创建一个按钮，点击按钮调用print_selection函数
    tk.Button(jiao_shi_pai_ke, text='删除该课程', font=('Arial', 12), width=15, height=2, command=print_selection).place(x=100, y=250)

    #按钮——查看已选课程
    def jiao_shi_pai_ke_destroy(name, no):
        jiao_shi_pai_ke.destroy()
        tian_ke_duan(name, no)

    tk.Button(jiao_shi_pai_ke, text='添加新课程', font=('Arial', 12), width=15, height=2, command = lambda : jiao_shi_pai_ke_destroy(name, no)).place(x=350, y=250)

    #按钮——查看选课信息
    tk.Button(jiao_shi_pai_ke, text='查看选课信息', font=('Arial', 12), width=15, height=2, command = lambda :jie_mian_geng_ti(jiao_shi_cha_kan, jiao_shi_pai_ke, jiao_shi_duan, name=name, no=no)).place(x=100, y=330)

    tk.Button(jiao_shi_pai_ke, text='返回', font=('Arial', 12), width=15, height=2, command=lambda: jie_mian_geng_ti(jiao_shi_deng_ru, jiao_shi_pai_ke)).place(x=350, y=330)

    jiao_shi_pai_ke.mainloop()  # 主窗口循环显示

def jiao_shi_cha_kan(no= '', name= '', old_wnd=''):
    '''教师查看选课信息'''
    global cha_kan
    cha_kan = tk.Tk()  # 建立窗口
    cha_kan.title('选课系统——课程信息')  # 标题
    cha_kan.geometry('300x400')  # 设立界面大小

    # 设置窗口大小
    width = 300
    height = 400
    # 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
    screenwidth = cha_kan.winfo_screenwidth()
    screenheight = cha_kan.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    cha_kan.geometry(alignstr)

    cha_kan.resizable(width=False, height=False)  # 窗口尺寸不可变化

    db = pymysql.connect('localhost', 'root', '123456', 'course selection system')  # mysql    本机   账户  密码   表名
    cur = db.cursor()

    sql_1 = "select Cname from course_information where Tno='%s'" % (no)


    try:
        cur.execute(sql_1)
        db.commit()
        yuan_su = cur.fetchall()

    except Exception as e:
        db.rollback()
        print(str(e))


    tk.Label(cha_kan, text='请选择课程名:', font=('Arial', 12)).place(x=30, y=25)
    value = StringVar()
    numberChosen = ttk.Combobox(width=30, textvariable=value)

    lie_biao_zhi =[]

    for wei_zhi in range(len(yuan_su)):
        lie_biao_zhi.append(yuan_su[wei_zhi][0])

    numberChosen['values'] = lie_biao_zhi  # 设置下拉列表的值
    numberChosen.place(x=30,y=50)
    numberChosen.current(0)

    def cha_xun(cname):
        db = pymysql.connect('localhost', 'root', '123456', 'course selection system')  # mysql    本机   账户  密码   表名
        cur = db.cursor()

        sql_1 = "select Sname,Sno from `course selection system`.stc_information where Cname='%s'" % (cname)

        try:
            cur.execute(sql_1)
            db.commit()
            yuan_su = cur.fetchall()

        except Exception as e:
            db.rollback()
            print(str(e))

        mu_biao = tk.Listbox(cha_kan, width=80, height=2)

        for a_a in range(len(yuan_su)):
            mu_biao.insert(END, yuan_su[a_a][0]+('   ')+yuan_su[a_a][1])

        tk.Label(cha_kan, text='选择该课的学生:', font=('Arial', 12)).place(x=30, y=150)
        mu_biao.place(x=65, y=180, width=150, height=80)

    tk.Button(cha_kan, text='查询', font=('Arial', 12), width=8, height=1, command = lambda :cha_xun(numberChosen.get())).place(x=100, y=85)

    def wnd_destroy(tname, tno):
        cha_kan.destroy()
        jiao_shi_duan(no= tno, name= tname)

    tk.Button(cha_kan, text='返回', font=('Arial', 12), width=8, height=1, command=lambda :wnd_destroy(name, no)).place(x=100, y=330)

    cha_kan.mainloop()  # 主窗口循环显示

def tian_ke_duan(tname, tno, old_wnd=''):
    '''添加新课程'''
    global tain_ke
    tain_ke = tk.Tk()  # 建立窗口
    tain_ke.title('选课系统——添加课程端')  # 标题
    tain_ke.geometry('600x400')  # 设立界面大小

    # 设置窗口大小
    width = 600
    height = 400
    # 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
    screenwidth =  tain_ke.winfo_screenwidth()
    screenheight =  tain_ke.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    tain_ke.geometry(alignstr)

    tain_ke.resizable(width=False, height=False)  # 窗口尺寸不可变化

    global new_cname
    new_cname = tk.StringVar()
    tk.Label(tain_ke, text='课程名: ', font=('Arial', 20), width=8, height=1).place(x=110, y=100)  # 将`User name:`放置在坐标（10,10）。
    tk.Entry(tain_ke, textvariable=new_cname, font=('Arial', 17)).place(x=250, y=105)

    global new_cdit
    new_cdit = tk.StringVar()
    tk.Label(tain_ke, text='学分:', font=('Arial', 20)).place(x=140, y=150)
    tk.Entry(tain_ke, textvariable=new_cdit, font=('Arial', 17), width=5).place(x=250, y=155)

    tk.Button(tain_ke, text='创建', font=('Arial', 15), width=8, height=1, command=lambda:ke_cehng_xin_xi_jian_cha(new_cname.get(), new_cdit.get(), tname, tno)).place(x=180, y=300)

    # 按钮3——返回
    def wnd_destroy(tname, tno):
        tain_ke.destroy()
        jiao_shi_duan(no= tno, name= tname)
    tk.Button(tain_ke, text='关闭', font=('Arial', 15), width=8, height=1, command=lambda :wnd_destroy(tname, tno)).place(x=320, y=300)


    tain_ke.mainloop()

def ke_cehng_xin_xi_jian_cha(cfm_name, cfm_dit, cfm_tname, cfm_tno):
    '''检查新建课程信息，并添加进数据库'''
    if len(cfm_name) == 0 or len(cfm_dit) == 0 :
        tkinter.messagebox.showerror(message='课程信息不完整！请检查！')

    db = pymysql.connect('localhost', 'root', '123456', 'course selection system')  # mysql    本机   账户  密码   表名
    cur = db.cursor()

    sql_1 = "select Cname from course_information where Cname='%s'" % (cfm_name)
    sql_2 = "select count('%s') from `course selection system`.course_information where Tname = '%s'"%(cfm_tname,cfm_tname)

    try:
        cur.execute(sql_1)
        db.commit()
        if len(cur.fetchall()) == 0:
            try:
                cur.execute(sql_2)
                db.commit()
                cfm_cno = (cfm_tno)+(str(cur.fetchall()[0][0]+1))
                try:
                    sql_3 = "INSERT INTO `course selection system`.`course_information` (`Cno`, `Cname`, `Cdit`, `Tname`, `Tno`) VALUES ('%s', '%s', %s, '%s', '%s')" % (cfm_cno, cfm_name, cfm_dit, cfm_tname, cfm_tno)
                    cur.execute(sql_3)
                    db.commit()

                    tkinter.messagebox.showinfo(message='添加成功！')

                except Exception as e:
                    db.rollback()
                    print(str(e))

            except Exception as e:
                db.rollback()
                print(str(e))

        else:
            tkinter.messagebox.showerror(message='该课程已存在！')

    except Exception as e:
        # 有错打印错误信息
        db.rollback()
        print(str(e))

def deng_ru(usr_name, usr_psd, duan_kou):
    '''登入功能'''
    # global zhang_hao
    # global mi_ma
    # usr_name = zhang_hao.get()
    # usr_psd = mi_ma.get()

    if len(usr_name) == 0:
        tkinter.messagebox.showerror(message='账号不能为空！')

    elif len(usr_psd) == 0:
        tkinter.messagebox.showerror(message='密码不能为空！')

    elif duan_kou == 1 or duan_kou == 2:
        db = pymysql.connect('localhost', 'root', '123456', 'course selection system')#mysql    本机   账户  密码   表名
        cur = db.cursor()

        xue_sheng_1 = "select Sno from Student_information where Sno=%s"%(usr_name)   #查找用户名
        xue_sheng_2 = "select Spassword from Student_information where Sno=%s"%(usr_name)    #查找用户名对应密码
        xue_sheng_3 = "select Sname from Student_information where Sno=%s"%(usr_name)

        jiao_shi_1 = "select Tno from Teacher_information where Tno=%s"%(usr_name)
        jiao_shi_2 = "select Tpassword from Teacher_information where Tno=%s"%(usr_name)
        jiao_shi_3 = "select Tname from Teacher_information where Tno=%s" % (usr_name)

        if duan_kou == 1:
            sql_1 = xue_sheng_1
            sql_2 = xue_sheng_2
            sql_3 = xue_sheng_3
            kai_qi = xue_sheng_duan
            guan_bi = xue_sheng

        elif duan_kou == 2:
            sql_1 = jiao_shi_1
            sql_2 = jiao_shi_2
            sql_3 = jiao_shi_3
            kai_qi = jiao_shi_duan
            guan_bi = jiao_shi

        try:
            cur.execute(sql_1)
            db.commit()
            if len(cur.fetchall()) != 0:
                try:
                    cur.execute(sql_2)
                    db.commit()

                    if cur.fetchall()[0][0] == usr_psd:
                        cur.execute(sql_3)
                        db.commit()
                        jie_mian_geng_ti(kai_qi, guan_bi, name=cur.fetchall()[0][0], no=usr_name)

                    elif len(cur.fetchall()) == 0 or cur.fetchall()[0][0] != usr_psd:
                        tkinter.messagebox.showerror(message='密码错误！请重新输入！')

                except Exception as e:
                    db.rollback()
                    print(str(e))

            elif len(cur.fetchall()) == 0:
                tkinter.messagebox.showerror(message='账号不存在！请重新输入！')


        except Exception as e:
            #有错打印错误信息
            db.rollback()
            print(str(e))

    elif duan_kou == 3:
        if usr_name == '1' and usr_psd == '1':
            jie_mian_geng_ti(guan_li_yuan_duan, guan_li_yuan)
        elif usr_name != '1':
            tkinter.messagebox.showerror(message='非管理员账户！请重新输入！')
        elif usr_psd != '1' and usr_name == '1':
            tkinter.messagebox.showerror(message='密码错误！请重新输入！')

def zhu_ce_duan(no= '', name= '', old_wnd = ''):
    '''注册端'''
    duan_kou =old_wnd

    global zhu_ce_duan
    zhu_ce_duan = tk.Tk()  # 建立窗口
    zhu_ce_duan.title('选课系统——注册端')  # 标题
    zhu_ce_duan.geometry('600x400')  # 设立界面大小

    # 设置窗口大小
    width = 600
    height = 400
    # 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
    screenwidth = zhu_ce_duan.winfo_screenwidth()
    screenheight = zhu_ce_duan.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    zhu_ce_duan.geometry(alignstr)

    zhu_ce_duan.resizable(width=False, height=False)  # 窗口尺寸不可变化

    global new_no
    new_no = tk.StringVar()  # 新建账号——帐号
    tk.Label(zhu_ce_duan, text='帐号（学号/教工号）: ').place(x=110, y=10)  # 将`User name:`放置在坐标（10,10）。
    tk.Entry(zhu_ce_duan, textvariable=new_no).place(x=250, y=10)

    global new_psd
    new_psd = tk.StringVar()  # 新建账号——密码
    tk.Label(zhu_ce_duan, text='密码： ').place(x=150, y=50)
    tk.Entry(zhu_ce_duan, textvariable=new_psd, show='*').place(x=250, y=50)

    global new_psd_confirm
    new_psd_confirm = tk.StringVar()  # 新建账号——确认密码
    tk.Label(zhu_ce_duan, text='请再次输入密码: ').place(x=150, y=90)
    tk.Entry(zhu_ce_duan, textvariable=new_psd_confirm, show='*').place(x=250, y=90)

    global new_name
    new_name = tk.StringVar()
    tk.Label(zhu_ce_duan, text = '姓名：').place(x=150, y=130)
    tk.Entry(zhu_ce_duan, textvariable = new_name).place(x=250, y=130)

    global new_sex
    new_sex = tk.StringVar()
    tk.Label(zhu_ce_duan, text = '性别：').place(x=150, y=170)
    tk.Radiobutton(zhu_ce_duan, text = '男', variable = new_sex, value = '男').place(x=250, y=170)
    tk.Radiobutton(zhu_ce_duan, text='女', variable=new_sex, value='女').place(x=300, y=170)

    global new_age
    new_age = tk.StringVar()
    tk.Label(zhu_ce_duan, text = '年龄：').place(x=150, y=210)
    tk.Entry(zhu_ce_duan, textvariable = new_age).place(x=250, y=210)

    global new_dept
    new_dept = tk.StringVar()
    tk.Label(zhu_ce_duan, text ='院系：').place(x=150, y=250)
    tk.Entry(zhu_ce_duan, textvariable = new_dept).place(x=250,y=250)

    tk.Button(zhu_ce_duan, text='注册', font=('Arial', 15), width=8, height=1, command = lambda:zhu_ce_xin_xi_jian_cha(duan_kou, new_no.get(), new_psd.get(), new_psd_confirm.get(), new_name.get(), new_age.get(), new_sex.get(), new_dept.get())).place(x=180, y=300)

    # 按钮3——返回
    if duan_kou == 1:
        tk.Button(zhu_ce_duan, text='返回', font=('Arial', 15), width=8, height=1, command=lambda:jie_mian_geng_ti(xue_sheng_deng_ru, zhu_ce_duan)).place(x=320, y=300)

    elif duan_kou == 2:
        tk.Button(zhu_ce_duan, text='返回', font=('Arial', 15), width=8, height=1, command=lambda: jie_mian_geng_ti(jiao_shi_deng_ru, zhu_ce_duan)).place(x=320, y=300)

    zhu_ce_duan.mainloop()

def jie_mian_geng_ti(new_wnd_hanshu, old_wnd_chuangkou, old_wnd_hanshu='', name ='', no =''):
    '''关闭之前窗口,打开新窗口'''
    old_wnd_chuangkou.destroy()
    new_wnd_hanshu(name= name, no= no, old_wnd = old_wnd_hanshu)

def zhu_ce_xin_xi_jian_cha(duan_kou, cfm_new_no, cfm_new_psd, cfm_new_psd_confirm, cfm_new_name, cfm_new_age, cfm_new_sex, cfm_new_dept):
    '''检查注册信息，并添加进数据库'''
    # global new_no, new_psd, new_psd_confirm, new_name, new_age,new_sex, new_dept
    # cfm_new_no = new_no.get()
    # cfm_new_psd = new_psd.get()
    # cfm_new_psd_confirm = new_psd_confirm.get()
    # cfm_new_name = new_name.get()
    # cfm_new_age = new_age.get()
    # cfm_new_sex = new_sex.get()
    # cfm_new_dept = new_dept.get()

    if len(cfm_new_no) == 0 or len(cfm_new_psd) == 0 or len(cfm_new_psd_confirm) == 0 or len(cfm_new_name) == 0 or len(cfm_new_age) == 0 or len(cfm_new_sex) == 0 or len(cfm_new_dept) == 0:
        tkinter.messagebox.showerror(message='用户信息不完整！请检查！')

    elif cfm_new_psd != cfm_new_psd_confirm:
        tkinter.messagebox.showerror(message='两次输入的密码不相同！请检查！')

    else:
        db = pymysql.connect('localhost', 'root', '123456', 'course selection system')  # mysql    本机   账户  密码   表名
        cur = db.cursor()

        xue_sheng_1 = "select Sno from Student_information where Sno=%s"%(cfm_new_no)
        xue_sheng_2 = "INSERT INTO `course selection system`.`student_information` (`Sno`, `Sname`, `Ssex`, `Sage`, `Sdept`, `Spassword`) " \
                      "VALUES ('%s', '%s', '%s', %s, '%s', %s)"% (cfm_new_no, cfm_new_name, cfm_new_sex, cfm_new_age, cfm_new_dept, cfm_new_psd)

        jiao_shi_1 = "select Tno from Teacher_information where Tno=%s" % (cfm_new_no)
        jiao_shi_2 = "INSERT INTO `course selection system`.`Teacher_information` (`Tno`, `Tname`, `Tsex`, `Tage`, `Tdept`, `Tpassword`) " \
                     "VALUES ('%s', '%s', '%s', %s, '%s', %s)" % (cfm_new_no, cfm_new_name, cfm_new_sex, cfm_new_age, cfm_new_dept, cfm_new_psd)

        if duan_kou == 1:
            sql_1 = xue_sheng_1
            sql_2 = xue_sheng_2
            kai_qi = xue_sheng_duan
            guan_bi = xue_sheng

        elif duan_kou == 2:
            sql_1 = jiao_shi_1
            sql_2 = jiao_shi_2
            kai_qi = jiao_shi_duan
            guan_bi = jiao_shi

        try:
            cur.execute(sql_1)
            db.commit()
            if len(cur.fetchall()) == 0:
                try:
                    cur.execute(sql_2)
                    db.commit()

                    tkinter.messagebox.showinfo(message='注册成功！')
                    jie_mian_geng_ti(kai_qi, guan_bi)

                except Exception as e:
                    db.rollback()
                    print(str(e))

            else:
                tkinter.messagebox.showerror(message='该账号已存在！')

        except Exception as e:
            #有错打印错误信息
            db.rollback()
            print(str(e))

if __name__ == '__main__':
     zhu_jie_mian()
    #学生
    #xue_sheng_deng_ru()
    # xue_sheng_duan()
    # xue_sheng_yi_xuan_duan()
    #教师
    # jiao_shi_deng_ru()
    # jiao_shi_duan()
    # tian_ke_duan()
    # jiao_shi_cha_kan()
    #管理员
    # guan_li_yuan_deng_ru()
    # guan_li_yuan_duan()

    # zhu_ce_duan()
