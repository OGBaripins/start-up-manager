import tkinter as tk
from tkinter import filedialog, Text
from log import get_logger
from configSetup import *
from dataBase import *

import os


logger = get_logger(__name__)
logger.info('Logger has been initialized')
root = tk.Tk()

# DBChecker()
# addData("spotify", "1.0.1.0.9")
# addData("Discord", "1.0.0.0")
# readData()


canvas = tk.Canvas(root, width=1920, height=1080, bg="#007a5a")
root.attributes("-fullscreen", True)
canvas.pack()


try:
    frame1 = tk.Frame(root, bg="black")
    frame1.place(width=400, height=250, x=250, y=100)

    frame2 = tk.Frame(root, bg="black")
    frame2.place(width=400, height=250, x=750, y=100)

    frame3 = tk.Frame(root, bg="black")
    frame3.place(width=400, height=250, x=1250, y=100)

    frame2_1 = tk.Frame(root, bg="black")
    frame2_1.place(width=400, height=250, x=250, y=420)

    frame2_2 = tk.Frame(root, bg="black")
    frame2_2.place(width=400, height=250, x=750, y=420)

    frame2_3 = tk.Frame(root, bg="black")
    frame2_3.place(width=400, height=250, x=1250, y=420)

    frame3_1 = tk.Frame(root, bg="black")
    frame3_1.place(width=400, height=250, x=250, y=740)

    frame3_2 = tk.Frame(root, bg="black")
    frame3_2.place(width=400, height=250, x=750, y=740)

    frame3_3 = tk.Frame(root, bg="black")
    frame3_3.place(width=400, height=250, x=1250, y=740)
except:
    logger.critical('Frames could not be created')

logger.info("All of the frames were created")


root.mainloop()
