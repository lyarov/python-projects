from PIL import Image, ImageDraw, ImageFont
from tkinter import Tk, filedialog, simpledialog
import textwrap
import os

text_size = 50


def get_user_text():
    root = Tk()
    root.withdraw()
    user_text = simpledialog.askstring("Ввод", "Введите текст:")
    root.destroy()
    return user_text


def add_border_and_text(file_path, user_text, output_path):
    border_length = 10

    img = Image.open(file_path)
    font = ImageFont.truetype("arial.ttf", size=text_size)

    lines = user_text.splitlines()

    temp_img = Image.new('RGB', (img.width, img.height + border_length), 'white')
    temp_draw = ImageDraw.Draw(temp_img)

    y_text = 0
    for line in lines:
        line = textwrap.fill(line, width=40)
        width, height = temp_draw.textbbox((0, 0), line, align='center', font=font)[2:4]
        temp_draw.text(((img.width - width) / 2, y_text), line, font=font, fill="black")
        y_text += height

    border_img = Image.new('RGB', (img.width + border_length * 2, img.height + y_text + border_length + 3), 'white')
    border_img.paste(img, (border_length, border_length))

    draw = ImageDraw.Draw(border_img)
    y_text = img.height + border_length

    for line in lines:
        line = textwrap.fill(line, width=40)
        width, height = draw.textbbox((0, 0), line, align='center', font=font)[2:4]
        draw.text(((img.width - width) / 2, y_text), line, font=font, fill="black")
        y_text += height

    border_img.save(output_path)
    print(f"Изображение сохранено по пути: {output_path}")

    img.close()
    temp_img.close()
    border_img.close()


def main():
    root = Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(title="Выберите изображение",
                                           filetypes=[("Изображения", "*.png;*.jpg;*.jpeg")])
    root.destroy()

    if not file_path:
        print("Выбор файла отменен.")
        exit()

    user_text = get_user_text()
    output_path = 'output_photo.jpg'
    add_border_and_text(file_path, user_text, output_path)


if __name__ == "__main__":
    main()

