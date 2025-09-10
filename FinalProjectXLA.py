import cv2
import cvzone
import tkinter as tk
from tkinter import filedialog
from ultralytics import YOLO
import datetime
import numpy as np
import math
from tkinter import *
from PIL import Image, ImageTk

#Tạo cửa sổ ứng dụng
app = tk.Tk()
app.title('Nhận dạng hạt cà phê rang chưa')
app_w = 1100
app_h = 600
screen_w = app.winfo_screenwidth()
screen_h = app.winfo_screenheight()
X = (screen_w/3) - (app_w/3)
Y = (screen_h/3) - (app_h/3)
app.geometry(f'{app_w}x{app_h}+{int(X)}+{int(Y)}')
#Hiện thị Logo trường
image = PhotoImage(file= r'ute.jpg')
img = image.subsample(2, 2)
logo = Label(app,image=img)
logo.pack()