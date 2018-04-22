from tkinter import *
from Board import *

board_size = 600

master = Tk()

master.title("Chess")

canvas = Canvas(master, width=board_size, height=board_size)
canvas.pack()

board = Board(canvas, board_size)

mainloop()
