import os
import tkinter as tk
import tkinter.ttk as ttk
from bs4 import BeautifulSoup
import webview

class App(tk.Tk):
    def __init__(self, path):
        super().__init__()
        self.names_dict = {}
        self.title("Просмотрщик лекарственных трав")

        abspath = os.path.abspath(path)
        self.nodes = {}
        self.tree = ttk.Treeview(self)
        self.tree.heading("#0", text="Список лекарственных трав", anchor=tk.W)
        ysb = ttk.Scrollbar(self, orient=tk.VERTICAL,
                            command=self.tree.yview)
        xsb = ttk.Scrollbar(self, orient=tk.HORIZONTAL,
                            command=self.tree.xview)
        self.tree.configure(yscroll=ysb.set, xscroll=xsb.set)

        self.tree.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        ysb.grid(row=0, column=1, sticky=tk.N + tk.S)
        xsb.grid(row=1, column=0, sticky=tk.E + tk.W)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.tree.bind("<<TreeviewOpen>>", self.open_node)
        self.tree.bind("<ButtonRelease-1>", self.on_treeview_click)  # Добавлено событие клика на элемент

        self.populate_node("", abspath)

    def open_page(self, name, link):
        print(os.path.abspath(link))
        window = webview.create_window(name, link, width=800, height=600, x=270, y=50)
        webview.start()

    def on_treeview_click(self, event):
        item = self.tree.focus()
        if item:
            # Получите текст элемента
            selected_text = self.tree.item(item, "text")
            orig = selected_text + ' - Просмотрщик лекарственных растений'
            selected_text = self.names_dict[selected_text]
            # print(selected_text)
            # Получите полный путь к файлу
            file_path = os.path.abspath(os.path.join("Практика_2", "pythonProject40", "Documents", selected_text))
            file_url = "file:///" + file_path.replace("\\", "/")
            # Вызовите вашу функцию open_page
            self.open_page(orig, file_url)

    def populate_node(self, parent, abspath):
        for entry in os.listdir(abspath):
            entry_path = os.path.join(abspath, entry)
            # print(entry_path)
            node = self.tree.insert(parent, tk.END, text=entry, open=False)
            if os.path.isdir(entry_path):
                self.nodes[node] = entry_path
                self.tree.insert(node, tk.END)
            else:
                h1_text = self.get_h1_text(entry_path)
                self.tree.item(node, text=h1_text)
                self.names_dict[h1_text] = entry_path

    def open_node(self, event):
        item = self.tree.focus()
        abspath = self.nodes.pop(item, False)
        if abspath:
            children = self.tree.get_children(item)
            self.tree.delete(children)
            self.populate_node(item, abspath)

    def get_h1_text(self, html_file):
        with open(html_file, 'r', encoding='windows-1251') as file:
            content = file.read()
            soup = BeautifulSoup(content, 'html.parser')
            h1_tag = soup.find('h1')
            if h1_tag:
                return h1_tag.text
            else:
                return "h1 не найдено"

if __name__ == "__main__":
    app = App(path="Практика_2\pythonProject40\Documents")
    app.geometry('220x700+50+50')
    app.mainloop()
