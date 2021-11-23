import tkinter as tk
from PIL import ImageTk
import PIL.Image
from tkinter import *
from config.log import  get_logger
from os import listdir
from events import relaxingEvent, programmingEvent, gamingEvent, studyingEvent, workoutEvent

logger = get_logger(__name__)
logger.info("App has started")

# Reading pictures for labels
def readPictures():
    pictureDict = {}
    try:
        for i in listdir("./pikturez"):
            split = i.split(".")
            pictureDict[split[0].strip()] = i.strip()
        logger.info("Pictures read successfully")
        return pictureDict
    except:
        logger.error("Pictures could not be read")

# Creating base for GUI
pictureDict = readPictures()
root = tk.Tk()
canvas = tk.Canvas(root, width=1920, height=1080, bg="#007a5a")
root.attributes("-fullscreen", True)

# Creating Labels with pictures
try:
    img1 = ImageTk.PhotoImage(PIL.Image.open("./pikturez/"+pictureDict["gaming"]))
    frame1 = Label(root, bg="black", image = img1)
    frame1.place(width=400, height=250, x=250, y=100)
    frame1.bind("<ButtonPress-1>",lambda event : gamingEvent())
    frame1.pack

    img2 = ImageTk.PhotoImage(PIL.Image.open("./pikturez/"+pictureDict["programming"]))
    frame2 = Label(root, bg="black", image = img2)
    frame2.place(width=400, height=250, x=750, y=100)
    frame2.bind("<Button-1>",lambda event : programmingEvent())
    frame2.pack

    img3 = ImageTk.PhotoImage(PIL.Image.open("./pikturez/"+pictureDict["relaxing"]))
    frame3 = Label(root, bg="black", image = img3)
    frame3.place(width=400, height=250, x=1250, y=100)
    frame3.bind("<Button-1>",lambda event : relaxingEvent())
    frame3.pack

    img4 = ImageTk.PhotoImage(PIL.Image.open("./pikturez/"+pictureDict["studying"]))
    frame2_1 = Label(root, bg="black", image = img4)
    frame2_1.place(width=400, height=250, x=250, y=420)
    frame2_1.bind("<Button-1>",lambda event : studyingEvent())
    frame2_1.pack

    img5 = ImageTk.PhotoImage(PIL.Image.open("./pikturez/"+pictureDict["workout"]))
    frame2_2 = Label(root, bg="black", image = img5)
    frame2_2.place(width=400, height=250, x=750, y=420)
    frame2_2.bind("<Button-1>",lambda event : workoutEvent())
    frame2_2.pack
except Exception as e:
    logger.critical('Frames could not be created\n'+"Err: "+e)

logger.info("All of the frames were created")
canvas.pack()
root.mainloop()


