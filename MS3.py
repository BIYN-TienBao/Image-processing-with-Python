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
average = Image.new(imgPIL.mode, imgPIL.size)
light = Image.new(imgPIL.mode, imgPIL.size)
lumi = Image.new(imgPIL.mode, imgPIL.size)

# lấy kích thước ảnh 
W= average.size[0]
H= average.size[1]

#Dùng 2 vòng for để quét ảnh gốc
for x in range(W):
    for y in range(H):
        #Lấy giá trị điểm ảnh
        R, G, B = imgPIL.getpixel((x, y))

        #Công thức chuyển đổi điểm ảnh RGB thành ảnh mức xám bằng phương pháp Average
        gray = np.uint8((R + G + B)/3)

        #Công thức chuyển đổi điểm ảnh RGB thành ảnh mức xám bằng phương pháp Lightness
        MIN = min(R, G, B)
        MAX = max(R, G, B)
        xam= np.uint8((MIN + MAX)/2)

        #Công thức chuyển đổi điểm ảnh RGB thành ảnh mức xám bằng phương pháp Luminance
        dentrang = np.uint8(0.2126*R + 0.7152*G + 0.0722*B)
        
    #gán giá trị mức xám
        average.putpixel((x, y),(gray, gray, gray))
        light.putpixel((x, y),(xam, xam, xam))
        lumi.putpixel((x, y),(dentrang, dentrang, dentrang))

#chuyển ảnh từ PIL sang OpenCV
anhxam1 = np.array(average)
anhxam2 = np.array(light)
anhxam3 = np.array(lumi)

#Hiện thị ảnh
cv2.imshow('Hinh co gai lena goc <21146064- TRUONG TIEN BAO>',hinhgoc)
cv2.imshow('Anh muc xam bang AVERAGE <21146064- TRUONG TIEN BAO>',anhxam1)
cv2.imshow('Anh muc xam bang LIGHTNESS <21146064- TRUONG TIEN BAO>',anhxam2)
cv2.imshow('Anh muc xam bang LUMINANCE <21146064- TRUONG TIEN BAO>',anhxam3)
#bấm phim bất kì để đóng cửa sổ
cv2.waitKey(0)

#Giải phóng bộ nhớ đã cấp cho cửa sổ
cv2.destroyAllWindows()