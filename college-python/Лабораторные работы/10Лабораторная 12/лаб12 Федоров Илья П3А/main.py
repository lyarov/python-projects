import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
Root = Tk()
Root.title("Тестирование")
Root.geometry('500x400')
chk = IntVar()
chk.set(0)
i = 0
ball = 0
f = open("test.txt", "r", encoding='utf8')
vopros = f.readline().strip()
text = Label(Root, text=vopros, font=("Arial", 14))
text.pack(anchor=W)
otv1 = Radiobutton(Root, text=f.readline().strip(), font=("Arial", 14), value=1, variable=chk)
otv1.pack(anchor=W)
otv2 = Radiobutton(Root, text=f.readline().strip(), font=("Arial", 14), value=2, variable=chk)
otv2.pack(anchor=W)
otv3 = Radiobutton(Root, text=f.readline().strip(), font=("Arial", 14), value=3, variable=chk)
otv3.pack(anchor=W)

ans = f.readline().strip()
test = int(ans)
src = f.readline().strip()
openedImage = Image.open(src)
openedImage = openedImage.resize((200, 200))
image = ImageTk.PhotoImage(openedImage)
imageView = tkinter.Label(image=image)
imageView.pack(anchor=W)

def com():
    global ball
    global i
    global test
    global src
    global image
    if chk.get() == test:
        ball += 1
    if i < 5:
        vopros = f.readline().strip()
        text.config(text = vopros)
        otv1.config(text = f.readline().strip())
        otv2.config(text = f.readline().strip())
        otv3.config(text = f.readline().strip())
        chk.set(0)
        ans = f.readline().strip()
        test = int(ans)
        src = f.readline().strip()
        openedImage = Image.open(src).resize((200, 200))
        image = ImageTk.PhotoImage(openedImage)
        imageView.config(image=image)
        i += 1
    else:
        messagebox.showinfo('ВЫВОД', 'Вы ответили правильно на ' + str(ball) + ' из 6 вопросов')
        Root.destroy()

bot = Button(Root, text='ДАЛЕЕ', font=("Arial", 14), command=com, pady = 10)
bot.pack(anchor=W)
Root.mainloop()
