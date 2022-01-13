from tkinter import * 
import os
root = Tk()
root.minsize(200,200)
def run():
	os.system('python detect_mask_video.py')
def detect():
	os.system('python test_tkinter.py')
def train():
	os.system('python train_mask_detector.py')
redbutton = Button(root, text = "Run", fg = "red", command=run)  
redbutton.grid(column=0,row=0)  
greenbutton = Button(root, text = "Detect", fg = "green", command=detect)  
greenbutton.grid(column=0,row=1)  
#bluebutton = Button(root, text = "Train", fg = "blue", command=train)  
#bluebutton.pack( side = TOP )  
blackbutton = Button(root, text = "Quit", fg = "black")  
blackbutton.grid(column=0,row=2)
root.mainloop()