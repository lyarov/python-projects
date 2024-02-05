import re
import tkinter as tk
from tkinter import filedialog
from bs4 import BeautifulSoup

def parse_fb2(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    title = soup.title.text
    author = soup.author.text
    year = soup.year.text if soup.year else "-"
    genre = soup.genre.text
    annotation = soup.annotation.text

    translator = soup.translator.text

    return f"Название: {title}\nАвтор: {author}\nГод выпуска: {year}\nЖанр: {genre}\n Аннотация: {annotation}\nПереводчик: {translator}\nДоп.Инфо:"

def clean_filename(name):
    # Очищаем имя файла от недопустимых символов
    return re.sub(r'[\\/*?:"<>|]', '', name)

def save_book(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    title = clean_filename(soup.title.text)
    author = clean_filename(soup.author.text)
    year = clean_filename(soup.year.text if soup.year else "UnknownYear")
    
    new_file_name = f"{title}-{author}-{year}.fb2"
    
    with open(new_file_name, 'w', encoding='utf-8') as new_file:
        new_file.write(content)
    
    return f"Книга сохранена как {new_file_name}"

def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[('FB2 Files', '*.fb2')])
    if file_path:
        book_info = parse_fb2(file_path)
        result_label.config(text=book_info)

        save_button['state'] = tk.NORMAL
        save_button['command'] = lambda: save_book(file_path)

# Создаем основное окно
root = tk.Tk()
root.title("FB2 Parser")

# Создаем метку для вывода информации о книге
result_label = tk.Label(root, text="Выберите файл FB2")
result_label.pack(pady=10)

# Создаем кнопку для открытия диалога выбора файла
open_button = tk.Button(root, text="Открыть FB2 файл", command=open_file_dialog)
open_button.pack(pady=10)

# Создаем кнопку для сохранения выбранной книги
save_button = tk.Button(root, text="Сохранить", state=tk.DISABLED)
save_button.pack(pady=10)

# Запускаем основной цикл событий
root.mainloop()
