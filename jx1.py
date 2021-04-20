import tkinter
import tkinter.messagebox
import _sqlite3

#idkp1-10.txt

#查询
list11=[]
list22=[]
result=[]
c1=0
max_last = 0


def find(result=[]):
    win1 = tkinter.Toplevel()
    win1.title('查询数据')
    win1.geometry('500x300')
    sw = win1.winfo_screenwidth()
    sh = win1.winfo_screenheight()
    win1.geometry('+%d+%d' % ((sw - 500) / 2, (sh - 300) / 2))

    tkinter.messagebox.showinfo("结果如下",result)
    win1.destroy()

#绘制散点图

def paint(list11=[],list22=[]):
    import numpy as np
    import matplotlib.pyplot as plt
    plt.scatter(list11,list22)
    plt.show()

#排序

def sort(list11=[],list22=[]):
    win1 = tkinter.Toplevel()
    win1.title('数据排序')
    win1.geometry('500x300')
    sw = win1.winfo_screenwidth()
    sh = win1.winfo_screenheight()
    win1.geometry('+%d+%d' % ((sw - 500) / 2, (sh - 300) / 2))
    list4=[]
    for i in range(2,len(list11)+1):
        if i%3==0:
            list4.append(round(int(list11[i-1])/int(list22[i-1]),3))
    list4.sort(reverse=True)
        
    tkinter.messagebox.showinfo("按照性价比的非递增排序",list4)
    win1.destroy()
   
#选择算法

def solve(c1,s=[],y=[]):
    win1 = tkinter.Toplevel()
    win1.title('算法结果')
    win1.geometry('500x300')
    sw = win1.winfo_screenwidth()
    sh = win1.winfo_screenheight()
    win1.geometry('+%d+%d' % ((sw - 500) / 2, (sh - 300) / 2))
    n=len(list11)
    import datetime

    starttime = datetime.datetime.now()
    n=len(list11)
    list11.insert(0,0)
    list22.insert(0,0)
    x=[]
    f=[]
    for i in range(n+1):
        x.append(0)
    for i in range(n+1):
        f.append([])

    for i in range(n+1):
        for j in range(c1+1):
            f[i].append(0)
    
    for i in range(1,n+1):
        for j in range(1,c1+1):
            if j<int(list11[i]):
                f[i][j]=f[i-1][j]
            else:
                f[i][j]=max(f[i-1][j],f[i-1][j-int(list11[i])]+int(list22[i]));
            
    x33="背包能装的最大价值是："+str(f[n][c1])

    j=c1
    for i in range(n,0,-1):
        if f[i][j]>f[i-1][j]:
            x[i]=1
            j=j-int(list11[i])
        else:
            x[i]=0
    x32="\n装入背包的物品是："+str(x)
    endtime = datetime.datetime.now()
    x30='\n运行时间为：'+str(endtime - starttime)
    x31=x33+'\n'+x32+'\n'+x30
    tkinter.messagebox.showinfo("动态规划算法",x31)
    win1.destroy()

if __name__ == '__main__':
    def secondMain():
        
        n=name.get()
        p1=ph.get()
        p=int(p1)
        with open(n,'r') as f:
                message=f.readlines()
        a='The profit of items are:'
        b='The weight of items are:'
        d='the cubage of knapsack is'
       
        file1=open("y1.txt",'w')
        file2=open("y3.txt",'w')
        l1=[]

        for i in range(len(message)):
            if message[i][:24]==a:
                file1.write(message[i+1])
                e=message[i-1]
                e1="the cubage of knapsack is"
                e2=e.index(e1)
                l1.append(int(e[e2+len(e1)+1:-2]))
            if message[i][:24]==b:
                file2.write(message[i+1])
        c1=l1[p]
        file1.close()
        file2.close()

        file1=open("y1.txt",'w')#价值
        file2=open("y2.txt",'w')#重量
        for i in range(len(message)):
            if message[i][:24]==a:
                file1.write(message[i+1])
        if message[i][:24]==b:
            file2.write(message[i+1])
        file1.close()
        file2.close()
        with open("y3.txt",'r') as file11:
            message1=file11.readlines()
        with open("y1.txt",'r') as file22:
            message2=file22.readlines()
        list2=[]#存放重量
        list3=[]#存放价值
        for i in message1:
            str1=i[:-2].split(',')
            list1=[]
            for j in str1:
                list1.append(int(j))
            list2.append(list1)
        for i in message2:
            str1=i[:-2].split(',')
            list1=[]
            for j in str1:
                list1.append(int(j))
            list3.append(list1)
            
        for i in range(len(list2)):
            for j in range(len(list2[i])):
                c.execute('insert into bp (weight,value) values (?,?)',(list2[i][j],list3[i][j]))
        ok=0
        for i in range(p):
            xx1=10**(i+1)
            ok=3*xx1+ok
        xx1=10**(p+1)
        ok1=3*xx1
        c.execute('select * from bp limit ?,?',(ok,ok1))
        result=c.fetchall()
        list11=[]
        list22=[]
        for i in range(len(result)):
            list11.append(result[i][0])
            list22.append(result[i][1])
        print(result)
        op = v.get()
        if op==1:
            find(result)
        elif op==2:
            paint(list11,list22)
        elif op==3:
            sort(list11,list22)
        elif op==4:
            solve(c1,list11,list22)
    
     # 数据库
    conn = _sqlite3.connect(":memory:")
    c = conn.cursor()
    c.execute("create table bp(weight char(10),value char(20))")
    
    # 设置窗口位置
    win = tkinter.Tk()
    win.title('D{0-1}背包问题')
    win.geometry('500x300')
    sw = win.winfo_screenwidth()
    sh = win.winfo_screenheight()
    win.geometry('+%d+%d'%((sw-500)/2,(sh-300)/2))
    # 欢迎语
    l = tkinter.Label(win,text='欢迎进入D{0-1}KP实例数据集算法实验平台',font=('华文行楷',24),fg='green')
    l.place(relx=0.5,rely=0.1,anchor='center')

    # 选择数据集
    Lname = tkinter.Label(win, text='数据集文件名',font=('华文行楷',20),fg='green')
    Lname.place(relx=0.2, rely=0.3, anchor='center')
    nu = tkinter.StringVar()
    name = tkinter.Entry(win, textvariable=nu)
    name.place(relx=0.26, rely=0.28, width=90)
    # 选择第几组数据
    Lph = tkinter.Label(win, text='第几组数据（0-9）',font=('华文行楷',20),fg='green')
    Lph.place(relx=0.7, rely=0.3, anchor='center')
    nu = tkinter.StringVar()
    ph = tkinter.Entry(win, textvariable=nu)
    ph.place(relx=0.78, rely=0.28, width=140)

    # 单选按钮
    choose = [('1.进行数据的查询',1),('2.绘制数据散点图',2),('3.对数据进行排序',3),('4.选择算法来求解',4)]
    v = tkinter.IntVar()
    v.set(1)
    x,y = 0.5,0.5,
    for a,b in choose:
        cc = tkinter.Radiobutton(win,text=a,variable=v,value=b,font=('华文行楷',20),fg='green')
        cc.place(relx=x,rely=y,anchor='center')
        y += 0.1
    # 按钮
    b = tkinter.Button(win,text='确定',width=10,height=3,bg='gray',command=secondMain)
    b.place(relx=0,rely=1,anchor='sw')
    b2 = tkinter.Button(win, text='退出', width=10, height=3,bg='gray',command=win.quit)
    b2.place(relx=1, rely=1, anchor='se')
    
win.mainloop()
