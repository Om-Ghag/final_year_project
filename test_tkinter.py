import tkinter as tk
from tkinter import filedialog
import cv2
import face_recognition
import glob
import os

root = tk.Tk()
root.minsize(500,500)
root.title("Face Recognition")

#T = tk.Text(root, height=10, width=30)
#T.pack()
#import image_comparison
output = ""
img_dir = "images/" # Enter Directory of all images 
data_path = os.path.join(img_dir,'*g') 
files = glob.glob(data_path) 
#print(files)
Known_Images = []
images_name=[]
for f1 in files: 
    img1 = cv2.imread(f1) 
    #print(os.path.name)
    Known_Images.append(img1)

def UploadAction(event=None):
    global output 
    filename = filedialog.askopenfilename()
    print(type(filename))
    img = cv2.imread(filename)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_encoding = face_recognition.face_encodings(rgb_img)[0]

    for i in range(0,len(Known_Images)):
        rgb_img2 = cv2.cvtColor(Known_Images[i], cv2.COLOR_BGR2RGB)
        img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]
        result = face_recognition.compare_faces([img_encoding], img_encoding2)
        if result == [True]:
            print("Result: ", result)
            print(files[i])
            output = files[i]
            name = output[7:-4]
           # T.insert(tk.END, output)
            w = tk.Label(root, text=name)
            w.pack()
            break

    
    print('Selected:', filename)

button = tk.Button(root, text='Open', command=UploadAction)
button.pack()

root.mainloop()