from tkinter import ttk
import tkinter as tk

class tr():
    def __init__(self, root):
        self.tree = ttk.Treeview(root)
        self.tree.pack()
        self.tree.insert("", 0, "item1", text="cities")
        self.tree.insert("", 1, "item2", text="Astana")
        self.tree.insert("", 2, "item3", text="Almaty")
        self.tree.insert("", 3, "item4", text="Aktau")
        self.tree.insert("", 4, "item5", text="Karaganda")
        self.tree.insert("", 5, "item6", text="Taldykorgan")

        self.tree.insert('item2', 'end', 'Bayterek', text="Нурсултан Назарбаев")
        self.tree.move('Bayterek', 'item2', 'end')
        self.tree.insert('item2', 'end', 'khan-shatyr', text="Дарига Назарбаева")
        self.tree.move('khan-shatyr', 'item2', 'end')

        self.tree.insert('item3', 'end', 'Medeo', text="Дина Нурпеисова")
        self.tree.move('Medeo', 'item3', 'end')
        self.tree.insert('item3', 'end', 'kok-tobe', text="Олжас Сулейменов")
        self.tree.move('kok-tobe', 'item3', 'end')

        self.tree.insert('item4', 'end', 'SomePerson1', text="Some Person 1 (Aktau)")
        self.tree.move('SomePerson1', 'item4', 'end')
        self.tree.insert('item4', 'end', 'SomePerson2', text="Some Person 2 (Aktau)")
        self.tree.move('SomePerson2', 'item4', 'end')

        self.tree.insert('item5', 'end', 'AnotherPerson1', text="Another Person 1 (Karaganda)")
        self.tree.move('AnotherPerson1', 'item5', 'end')
        self.tree.insert('item5', 'end', 'AnotherPerson2', text="Another Person 2 (Karaganda)")
        self.tree.move('AnotherPerson2', 'item5', 'end')

        self.tree.insert('item6', 'end', 'Person1', text="Person 1 (Taldykorgan)")
        self.tree.move('Person1', 'item6', 'end')
        self.tree.insert('item6', 'end', 'Person2', text="Person 2 (Taldykorgan)")
        self.tree.move('Person2', 'item6', 'end')

        self.tree.move('item2', 'item1', 'end')
        self.tree.move('item3', 'item1', 'end')
        self.tree.move('item4', 'item1', 'end')
        self.tree.move('item5', 'item1', 'end')
        self.tree.move('item6', 'item1', 'end')

        self.tree.bind("<ButtonRelease-1>", self.OnClick)

    def OnClick(self, event):
        item = str(self.tree.selection())
        item = item.replace("('", "", 1)
        item = item.replace("',)", "", 1)
        self.show_person_info(item)

    def show_person_info(self, item):
        people_dict = {
            "Bayterek": "Нурсултан Назарбаев - первый Президент Республики Казахстан",
            "khan-shatyr": "Дарига Назарбаева - активист и депутат Мажилиса Парламента",
            "kok-tobe": "Дина Нурпеисова - казахстанская певица и композитор",
            "Medeo": "Олжас Сулейменов - казахстанский поэт и публицист",
            "SomePerson1": "Some Person 1 (Aktau) - Описание Some Person 1",
            "SomePerson2": "Some Person 2 (Aktau) - Описание Some Person 2",
            "AnotherPerson1": "Another Person 1 (Karaganda) - Описание Another Person 1",
            "AnotherPerson2": "Another Person 2 (Karaganda) - Описание Another Person 2",
            "Person1": "Person 1 (Taldykorgan) - Описание Person 1",
            "Person2": "Person 2 (Taldykorgan) - Описание Person 2",
        }

        if item in people_dict:
            lb.config(text=people_dict[item])
            lb2.config(image=image_list[item])
        else:
            lb.config(text="Выбран неизвестный объект")
            lb2.config(image=None)

root = tk.Tk()
root.geometry('1024x720')
tree = tr(root)

image_list = {
    "kok-tobe": tk.PhotoImage(file="22012024\\task1\\award.png"),
    "Bayterek": tk.PhotoImage(file="22012024\\task1\\art.png"),
    "Medeo": tk.PhotoImage(file="22012024\\task1\\award.png"),
    "khan-shatyr": tk.PhotoImage(file="22012024\\task1\\book.png"),
    "SomePerson1": tk.PhotoImage(file="22012024\\task1\\bug.png"),
    "SomePerson2": tk.PhotoImage(file="22012024\\task1\\cat.png"),
    "AnotherPerson1": tk.PhotoImage(file="22012024\\task1\\comic.png"),
    "AnotherPerson2": tk.PhotoImage(file="22012024\\task1\\gaming.png"),
    "Person1": tk.PhotoImage(file="22012024\\task1\\general.png"),
    "Person2": tk.PhotoImage(file="22012024\\task1\\groups.png"),
}

lb = ttk.Label(root)
lb.pack()
lb2 = ttk.Label(root)
lb2.pack()

root.mainloop()
