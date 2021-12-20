from tkinter import *
from Paddle import Paddle
from Score import Score
from Ball import Ball
import time

tk = Tk()
tk.title('Game')
tk.resizable(0,0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=500, height=400, highlightthickness=0)
canvas.pack()
tk.update()
score = Score(canvas, 'green')
paddle = Paddle(canvas, 'brown')
ball = Ball(canvas, paddle, score, 'blue')
ball2 = Ball(canvas, paddle, score, 'red')

while not ball.hit_bottom:
    if paddle.started == True:
        ball.draw()
        ball2.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

time.sleep(3)