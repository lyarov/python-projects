import tkinter as tk
from pygame import mixer  # Для воспроизведения аудио
from tkinter import PhotoImage

class AudioPlayerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Аудиосказка")
        self.master.geometry("800x600")

        self.current_slide = 1
        self.total_slides = 6

        # Инициализация Pygame mixer
        mixer.init()

        # Загрузка аудиофайлов
        self.audio_files = [f"slide{i}.mp3" for i in range(1, self.total_slides + 1)]

        # Создание виджетов
        self.image_label = tk.Label(master, width=400, height=400)
        self.image_label.pack(pady=10)

        self.play_button = tk.Button(master, text="Воспроизвести", command=self.play_audio)
        self.play_button.pack(pady=10)

        self.prev_button = tk.Button(master, text="Назад", command=self.prev_slide)
        self.prev_button.pack(side=tk.LEFT, padx=10)

        self.next_button = tk.Button(master, text="Вперед", command=self.next_slide)
        self.next_button.pack(side=tk.RIGHT, padx=10)

        # Показать первый слайд
        self.show_current_slide()

    def play_audio(self):
        audio_file = self.audio_files[self.current_slide - 1]
        mixer.music.load(audio_file)
        mixer.music.play()

    def show_current_slide(self):
        image_path = f"slide{self.current_slide}.png"
        original_image = tk.PhotoImage(file=image_path)
        resized_image = original_image.subsample(2)  # Уменьшим изображение
        self.image_label.config(image=resized_image)
        self.image_label.image = resized_image

    def prev_slide(self):
        if self.current_slide > 1:
            self.current_slide -= 1
            self.show_current_slide()

    def next_slide(self):
        if self.current_slide < self.total_slides:
            self.current_slide += 1
            self.show_current_slide()

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioPlayerApp(root)
    root.mainloop()
