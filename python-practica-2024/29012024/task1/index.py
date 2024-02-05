import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def CalcImageHash(FileName):
    image = cv2.imread(FileName)  
    if image is None:  
        messagebox.showerror("Ошибка", f"Не удалось прочитать изображение: {FileName}")
        return None
    
    resized = cv2.resize(image, (8, 8), interpolation=cv2.INTER_AREA)  
    gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    avg = gray_image.mean()  
    ret, threshold_image = cv2.threshold(gray_image, avg, 255, 0)  

    _hash = ""
    for x in range(8):
        for y in range(8):
            val = threshold_image[x, y]
            if val == 255:
                _hash += "1"
            else:
                _hash += "0"

    return _hash

def CompareHash(hash1, hash2):
    count = sum(c1 != c2 for c1, c2 in zip(hash1, hash2))
    return count

def analyze_images(folder_path):
    tree_images = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.jpeg')):
            img_path = os.path.join(folder_path, filename)
            try:
                img_hash = CalcImageHash(img_path)
                if img_hash is not None:
                    tree_images.append(img_path)
            except Exception as e:
                print(f"Error processing {img_path}: {e}")

    if not tree_images:
        messagebox.showinfo("Предупреждение", "В выбранной папке нет изображений для анализа.")
        return

    for i, img1_path in enumerate(tree_images):
        img1_hash = CalcImageHash(img1_path)
        if img1_hash is None:
            continue
        for j, img2_path in enumerate(tree_images):
            if i != j:
                img2_hash = CalcImageHash(img2_path)
                if img2_hash is None:
                    continue
                diff = CompareHash(img1_hash, img2_hash)
                if diff == 0:
                    messagebox.showinfo("Похожие изображения", f"Картинка {os.path.basename(img1_path)} похожа на {os.path.basename(img2_path)}")

def choose_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        analyze_images(folder_path)
    else:
        messagebox.showinfo("Отменено", "Выбор папки отменен.")

root = tk.Tk()
root.title("Сравнение изображений")

select_folder_btn = tk.Button(root, text="Выбрать папку с изображениями", command=choose_folder)
select_folder_btn.pack(pady=10)

root.mainloop()