import tkinter
from utils import ans
window = tkinter.Tk()
window.title('my window')
window.geometry('1000x700')
 
def plus():
    n1 = e1.get()  # 获取输入框1的值
    
    t.delete(1.0, 'end')  # 清除文本框内容
    t.insert('insert',ans(n1)) # 将结果添加到文本框显示
 
l1 = tkinter.Label(window, text='输入名称')
l1.pack()

e1 = tkinter.Entry(window, width=15)
e1.pack()
 
b1 = tkinter.Button(window, text="显示文章", command=plus)
b1.pack()
# 定义文本框
t = tkinter.Text(window, state='normal', width=100, height=40)
t.pack()
b2 = tkinter.Button(window, text='退出', command=window.quit)
b2.pack()
 
window.mainloop()