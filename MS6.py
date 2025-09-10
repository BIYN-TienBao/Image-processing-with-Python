import cv2
from PIL import Image
import numpy as np

#Khai báo đường dẫn file
img = r'lena_color.png'
#Đọc ảnh màu dùng thư viện OpenCV
hinhgoc= cv2.imread (img,cv2.IMREAD_COLOR)

#Đọc ảnh từ thư viên PIL để thực hiện các tác vụ tính toán\

imgPIL=Image.open(img)

#tạo các ảnh có cùng kích thước và mode với ảnh imgPIL
#ảnh này dùng để chưa kết quả chuyển đổi
Cyan = Image.new(imgPIL.mode, imgPIL.size)
Magenta = Image.new(imgPIL.mode, imgPIL.size)
Yellow = Image.new(imgPIL.mode, imgPIL.size)
Black = Image.new(imgPIL.mode, imgPIL.size)

# lấy kích thước ảnh 
W= Cyan.size[0]
H= Cyan.size[1]

#Dùng 2 vòng for để quét ảnh gốc
for x in range(W):
    for y in range(H):
        #Lấy giá trị điểm ảnh
        R, G, B = imgPIL.getpixel((x, y))

        #gán giá trị mức xám
        Cyan.putpixel((x, y),(B, G, 0))
        Magenta.putpixel((x, y),(B, 0, R))
        Yellow.putpixel((x, y),(0, G, R))

        MIN = min(R, G, B)
        Black.putpixel((x, y),(MIN, MIN, MIN))

#chuyển ảnh sang OpenCV
anhcyan = np.array(Cyan)
anhmagenta = np.array(Magenta)
anhyellow = np.array(Yellow)
anhblack = np.array(Black)

#Hiện thị ảnh
cv2.imshow('Hinh co gai lena goc <21146064- TRUONG TIEN BAO>',hinhgoc)
cv2.imshow('Ảnh kênh màu Cyan <21146064- TRUONG TIEN BAO>',anhcyan)
cv2.imshow('Ảnh kênh màu Magenta <21146064- TRUONG TIEN BAO>',anhmagenta)
cv2.imshow('Ảnh kênh màu Yellow <21146064- TRUONG TIEN BAO>',anhyellow)
cv2.imshow('Ảnh kênh màu Black <21146064- TRUONG TIEN BAO>',anhblack)

#bấm phim bất kì để đóng cửa sổ
cv2.waitKey(0)

#Giải phóng bộ nhớ đã cấp cho cửa sổ
cv2.destroyAllWindows()