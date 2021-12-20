from tkinter import *
import random
from Paddle import Paddle
from Score import Score

class Ball:
    def __init__(self, canvas: Canvas, paddle: Paddle, score: Score, color: str) -> None:
        self.speed = random.uniform(0.5, 1.5)
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.id = canvas.create_oval(10,10,30,30, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-1, -1, 1, 2]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -1*self.speed
        self.canvas_heigth = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, pos) -> bool:
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.score.hit()
                return True
        return False

    def draw(self) -> None:
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 1*self.speed
        if pos[3] >= self.canvas_heigth:
            self.hit_bottom = True
            self.canvas.create_text(250, 120, text='Ви програли', font=('Courier', 30), fill='red')
        if self.hit_paddle(pos) == True:
            self.y = -1*self.speed
        if pos[0] <=0:
            self.x = 1*self.speed
        if pos[2] >= self.canvas_width:
            self.x = -1*self.speed
