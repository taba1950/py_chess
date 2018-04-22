from tkinter import *
from Board import *
from GamePlay import *


def graphics():
    board_size = 640

    master = Tk()

    master.title("Chess")
    master.resizable(width=NO, height=NO)

    canvas = Canvas(master, width=board_size, height=board_size)

    canvas.pack()

    board = Board(canvas, board_size)

    game_play = GamePlay(board)

    canvas.bind("<Button-1>", lambda event: game_play.got_event(event))

    mainloop()




graphics()
