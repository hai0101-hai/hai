#这是一个简单的登录，注册系统
from tkinter import *
from tkinter import messagebox
from pathlib import *
import os

root = Tk()
class App:
    def __init__(self,master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        fm = Frame(self.master)
        fm.pack(pady=100)
        w = Label(fm,text="办 公 系 统",fg='red',font=('宋体',30,'bold'))
        w.pack(side=TOP)

        la_name = Label(text="用户名")
        la_name.place(x=screenwidth/2,y=screenheight/2)
        #把这个变设置为全局变量
        global var_user
        var_user=StringVar()
        tx_name = Entry(root,textvariable=var_user)
        tx_name['width'] = 10
        tx_name.place(x=screenwidth/2+50,y=screenheight/2)

        #把这个变设置为全局变量
        global var_pass
        var_pass=StringVar()
        la_pass = Label(text='密码')
        la_pass.place(x=screenwidth/2,y=screenheight/2+50)
        tx_pass = Entry(show='*',textvariable=var_pass)
        tx_pass['width'] = 10
        tx_pass.place(x=screenwidth/2+50,y=screenheight/2+50)

        fm1 = Frame(self.master)
        fm1.pack(side=BOTTOM,pady=100)
        login = Button(fm1,text='登录',width=10,command=self.usr_log_in)
        login.pack(side=LEFT,padx=10)
        sign_up = Button(fm1,text='注册',width=10,command=self.usr_sign_up)
        sign_up.pack(side=LEFT,padx=10)
        bnc = Button(fm1,text='取消',width=10,command=root.destroy)
        bnc.pack(side=LEFT,padx=10)

    def usr_log_in(self):
        usr_name = var_user.get()
        usr_pass = var_pass.get()
        if usr_name == '' or usr_pass == '':
            messagebox.showerror(message='用户名或密码为空')
        if usr_name != '' and usr_pass != '': 
            f = open('user_log.txt','r',True)
            count = f.readlines()
            for ch in count:
                strlist = ch.split('@')
                user_tuple = (strlist[0],strlist[1])
                n,p = user_tuple
                #因为密码的后面有个\n换行符，所以要用p[:-1]把它去掉
                if usr_name == n and usr_pass == p[:-1]:
                    messagebox.showinfo(title='提示',message='登录成功！！！')
                    break
            else:
                messagebox.showerror(message='用户或密码不正确')

    def usr_sign_up(self):
       
        window=Toplevel(root)
        window.geometry("350x300") #这里的x是小写的x
        window.title('注册')

        la_name = Label(window,text="用户名").place(x=20,y=10)
        var_usr_name=StringVar()
        tx_name = Entry(window,textvariable=var_usr_name)
        tx_name['width'] = 10
        tx_name.place(x=100,y=10)

        var_passx=StringVar()
        la_pass = Label(window,text='密码')
        la_pass.place(x=20,y=50)
        tx_pass = Entry(window,show='*',textvariable=var_passx)
        tx_pass['width'] = 10
        tx_pass.place(x=100,y=50)
        def usr_sign():
           n = var_usr_name.get()
           p = var_passx.get()
           f = open('user_log.txt','a',True)
           f.write(n+"@"+p+'\n')
           f.close()
           messagebox.showinfo(title='提示信息',message='注册成功')
           window.destroy()

        sign_up_button = Button(window,text='注册',width = 10,command=usr_sign)
        sign_up_button.pack(side=LEFT,padx=10)
        cal_button = Button(window,text='取消',width=10,command=window.destroy)
        cal_button.pack(side=LEFT,padx=10)

screenheight = root.winfo_screenheight()
screenwidth = root.winfo_screenwidth()
#窗口填充满屏幕
root.geometry("%dx%d" % (screenwidth,screenheight))
root.resizable(width=False,height=False)
root.title("天天好办公系统")
App(root)
root.mainloop()
