from tkinter import *

class Score:
    def __init__(self, canvas: Canvas, color: str) -> None:
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(450, 10, text=self.score, font=('Courier', 15), fill=color)

    def hit(self) -> None:
        self.score += 1
        self.canvas.itemconfig(self.id, text=self.score) # ??