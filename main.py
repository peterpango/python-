import tkinter
from utils import ans
window = tkinter.Tk()
window.title('window')
window.geometry('1000x700+200+100')
 
def plus():
    n1 = e1.get()
    t.delete(1.0, 'end')
    t.insert('insert',ans(n1))
 
l1 = tkinter.Label(window,
        text='输入名称:',
        font=('宋体',20),
        width=10,
        height=2).place(x=100,y=45)

e1 = tkinter.Entry(window,
                   width=20,
                   bg='#d3fbfb',
                   fg='black',
                   font=('宋体',32),
                   relief="groove",)
e1.place(x=300,y=50)
b1 = tkinter.Button(window,
                    bg='#d3fbfb',
                    fg='black',
                    font=('宋体',20),
                    width=8,
                    relief="raised",
                    text="显示文章",
                    command=plus).place(x=110,y=150)
t = tkinter.Text(window,
                 state='normal',   
                 bg='#d3fbfb',
                 fg='black',
                 font=('等线',12),
                 width=80,
                 height=30)
t.place(x=300,y=150) 
window.mainloop()
