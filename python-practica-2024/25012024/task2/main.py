import tkinter as tk
from PIL import Image, ImageTk

def move(event):
    global player_x, player_y

    if event.keysym == 'Up':
        canvas.move(player, 0, -5)
        rotate_player(90)
    elif event.keysym == 'Down':
        canvas.move(player, 0, 5)
        rotate_player(270)
    elif event.keysym == 'Left':
        canvas.move(player, -5, 0)
        rotate_player(180)
    elif event.keysym == 'Right':
        canvas.move(player, 5, 0)
        rotate_player(0)

def rotate_player(angle):
    # Поворот изображения персонажа
    rotated_image = original_player_image.rotate(angle)
    player_image = ImageTk.PhotoImage(rotated_image)
    canvas.itemconfig(player, image=player_image)
    canvas.player_image = player_image  # сохраняем ссылку на изображение, чтобы избежать удаления

root = tk.Tk()
root.title("Управление персонажем")

# Получение размеров экрана
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Загрузка изображения для фона
background_image = Image.open("background.png")
background_image = background_image.resize((screen_width, screen_height), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(background_image)

# Создание холста с фоном
canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
canvas.pack()

# Загрузка изображения для персонажа
original_player_image = Image.open("player.png")
player_image = ImageTk.PhotoImage(original_player_image)

# Создание персонажа в центре экрана
player = canvas.create_image(screen_width//2, screen_height//2, anchor=tk.CENTER, image=player_image)
canvas.player_image = player_image  # сохраняем ссылку на изображение

# Привязка функции move к событиям клавиш
root.bind('<Up>', move)
root.bind('<Down>', move)
root.bind('<Left>', move)
root.bind('<Right>', move)

root.mainloop()
