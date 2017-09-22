'第一步导入Tkinter包的所有内容'
# from tkinter import *
# '第二步是从 Frame 派生一个Application类,这是所有 Widget 的父容器'
# class Application(Frame):
#     def __init__(self,master = None):
#         Frame.__init__(self,master)
#         self.pack()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.hellowLabel = Label(self,text = 'Hellow,World!')
#         self.hellowLabel.pack()
#         self.quitButton = Button(self,text = '离开',command = self.quit())
#         self.quitButton.pack()
#
# app = Application()
# # 设置窗口标题
# app.master.title('标题')
# # 主消息循环
# app.mainloop()


'我们再对这个GUI程序改进一下,加入一个文本框,让用户可以输入文本,然后点按钮后,弹出消息对话框'
from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self,text = 'Hellow',command = self.hellow)
        self.alertButton.pack()

    def hellow(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message','Hellow,%s' % name)

app = Application()
app.master.title('标题')
app.mainloop()








