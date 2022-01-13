from tkinter import *
import os

def btn_clicked():
    print("Button Clicked")

def Mask_detection():
	os.system('python detect_mask_video.py')
def Face_recognition():
	os.system('python test_tkinter.py')
def train():
	os.system('python train_mask_detector.py')
window = Tk()

window.geometry("725x422")
window.configure(bg = "#bfeaf8")
canvas = Canvas(
    window,
    bg = "#bfeaf8",
    height = 422,
    width = 725,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

canvas.create_text(
    362.5, 56.0,
    text = "Secure X ",
    fill = "#000000",
    font = ("Sansita-Regular", int(48.0)))

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = Mask_detection,
    relief = "flat")

b0.place(
    x = 72, y = 122,
    width = 230,
    height = 53)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = Face_recognition,
    relief = "flat")

b1.place(
    x = 423, y = 122,
    width = 230,
    height = 53)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 688, y = 0,
    width = 37,
    height = 37)

window.resizable(False, False)
window.mainloop()
