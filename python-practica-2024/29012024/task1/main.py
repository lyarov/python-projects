import tkinter as tk
from tkinter import filedialog, ttk
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from PIL import Image, ImageTk

class ImageComparatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Comparator")

        self.images = []
        self.image_labels = []

        self.canvas = tk.Canvas(self.root, width=500, height=500)
        self.canvas.pack()

        self.add_button = tk.Button(self.root, text="Добавить фото", command=self.add_image)
        self.add_button.pack()

        self.compare_button = tk.Button(self.root, text="Сравнить", command=self.compare_images)
        self.compare_button.pack()

        self.tree = ttk.Treeview(self.root, columns=('Image 1', 'Image 2', 'Similarity (%)'), show='headings')
        self.tree.heading('Image 1', text='Картинка 1')
        self.tree.heading('Image 2', text='Картинка 2')
        self.tree.heading('Similarity (%)', text='Схожесть (%)')
        self.tree.pack()

    def add_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            img = cv2.imread(file_path)

            if img is None:
                tk.messagebox.showerror("Error", "Failed to read the image. Please select a valid image file.")
                return

            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            img.thumbnail((100, 100))  # Limit the size of displayed images
            photo = ImageTk.PhotoImage(img)

            label_text = f"Image {len(self.images) + 1}"
            label = tk.Label(self.canvas, text=label_text)
            label.grid(row=(len(self.images) // 5) * 2 + 1, column=len(self.images) % 5)

            label = tk.Label(self.canvas, image=photo)
            label.image = photo
            label.grid(row=(len(self.images) // 5) * 2, column=len(self.images) % 5)  # Place images in a grid
            self.images.append(img)
            self.image_labels.append(label)

    def compare_images(self):
        if len(self.images) < 2:
            tk.messagebox.showerror("Error", "Add at least two images for comparison.")
            return

        self.tree.delete(*self.tree.get_children())  # Clear the treeview before populating with new results

        # Resize all images to a common size
        resized_images = [cv2.resize(np.array(img), (100, 100)) for img in self.images]

        for i, img in enumerate(resized_images):
            for j, img2 in enumerate(resized_images[i + 1:], start=i + 1):
                # Convert images to grayscale
                gray_img1 = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
                gray_img2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)

                # Calculate structural similarity index
                similarity_index = ssim(gray_img1, gray_img2)

                # Add comparison results to the treeview
                self.tree.insert('', 'end', values=(f"Image {i+1}", f"Image {j+1}", f"{similarity_index*100:.2f}%"))

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageComparatorApp(root)
    root.mainloop()
