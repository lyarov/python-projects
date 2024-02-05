from tkinter import ttk
import tkinter as tk
class tr():
    def __init__(self,root):
        self.tree = ttk.Treeview(root)
        self.tree.pack()
        self.tree.insert("", 0, "item1", text="cities")
        self.tree.insert("", 1, "item2", text="Astana")
        self.tree.insert("", 2, "item3", text="Almaty")
        self.tree.insert('item2','end','Bayterek',text="Bayterek")
        self.tree.move('Bayterek', 'item2', 'end')
        self.tree.insert('item2', 'end', 'khan-shatyr',text="Khan-shatyr")
        self.tree.move('khan-shatyr', 'item2', 'end')
        self.tree.insert('item3', 'end', 'Medeo', text="Medeo")
        self.tree.move('Medeo', 'item3', 'end')
        self.tree.insert('item3', 'end', 'kok-tobe', text="Kok-tobe")
        self.tree.move('kok-tobe', 'item3', 'end')
        self.tree.move('item2', 'item1', 'end')
        self.tree.move('item3', 'item1', 'end')
        self.tree.bind("<ButtonRelease-1>",self.OnClick)
    def OnClick(self,event):
        item=str(self.tree.selection())
        item=item.replace("('","",1)
        item=item.replace("',)","",1)
        self.sh((item))

    def sh(self,item):

        if item=="Bayterek":
            lb.config(text="Байтерек - Смотровая башня высотой 105 метров")
            lb2.config(image=image_list[item])
        elif item == "khan-shatyr":
            lb.config(text="Хан Шатыр -ТЦ в виде огромного шатра")
            lb2.config(image=image_list[item])
        elif item == "kok-tobe":
            lb.config(text="Кок тобе - высокогорный ледяной каток")
            lb2.config(image=image_list[item])
        if item == "Medeo":
            lb.config(text="Медеу - высокогорный спортивный комплекс")
            lb2.config(image=image_list[item])


root = tk.Tk()
root.geometry('1024x720')
tree=tr(root)
lb=ttk.Label(root)
lb.pack()
lb2=ttk.Label(root)
lb2.pack()
image_list={"kok-tobe":tk.PhotoImage(file= r"./kok-tobe.png"),
            "Bayterek":tk.PhotoImage(file= r"./Bayterek.png"),
            "Medeo":tk.PhotoImage(file= r"./Medeo.png"),
            "khan-shatyr":tk.PhotoImage(file= r"./khan-shatyr.png"),
            }
root.mainloop()

