from turtle import *
import keyboard
canvas = getcanvas()

def draw_ui():
    canvas.create_text(145, 350, text="W - Направить вперёд")
    canvas.create_text(0, 350, text="A,D - Направлять в стороны")
    canvas.create_text(-175, 350, text="T(англ) - PenUp(Отпустить кисть)")
    canvas.create_text(0, -350, text="Рисовка клавишами")
    canvas.create_text(240, 350, text="C - Стереть")
def game_loop():
    if keyboard.is_pressed("w"):
        forward(5)
    if keyboard.is_pressed("a"):
        left(5)
    if keyboard.is_pressed("s"):
        backward(5)
    if keyboard.is_pressed("d"):
        right(5)
    if keyboard.is_pressed("t"):
        penup()
    else:
        pendown()
    if keyboard.is_pressed("c"):
        clearscreen()
        draw_ui()

    ontimer(game_loop, 10)

game_loop()
draw_ui()
done()