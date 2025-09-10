import cv2;
from PIL import Image; #thư viện pillow hỗ trợ nhiều định dạng ảnh
import numpy as np;
import math;

#khai báo đường dẫn file ảnh
filehinh=r'lena_color-0000.jpg'

#đọc ảnh màu dùng emgucv
img=cv2.imread(filehinh,cv2.IMREAD_COLOR)

#đọc ảnh dùng PIL và dùng ảnh PIL để xử lý tính toán thay vì dùng emgucv
imgPIL=Image.open(filehinh)

#tạo 4 ảnh có cùng kích thước với ảnh PIL. Ta dùng ảnh này để chứa kết quả sau khi chuyển đổi RGB->HSI
Hue_PIL=Image.new(imgPIL.mode, imgPIL.size)
Saturation_PIL= Image.new(imgPIL.mode,imgPIL.size)
Intensity_PIL= Image.new(imgPIL.mode,imgPIL.size)
HSI_img_PIL= Image.new(imgPIL.mode, imgPIL.size)

#lấy kích thước ảnh từ ảnh PIL
width=Hue_PIL.size[0]
height=Hue_PIL.size[1]


for x in range (width):
    for y in range(height):
        #đọc giá trị pixel tại x,y
        R, G, B=imgPIL.getpixel((x, y))
        
        #Tính theta
        numerator = ((R-G)+(R-B))/2
        denominator = math.sqrt((R-G)**2+(R-B)*(G-B))
        theta = math.acos(numerator/denominator)
        
        #tính Hue
        H=0
        if B<=G:
            H=theta
        else:
            H=2*math.pi - theta
        #quy đổi từ degree về radian
        H=np.uint8(H*180/math.pi)

        #tính saturation
        Sat=(1-(3*min(R,G,B))/(R+G+B)) # chưa tính ra được đang sai về code lại
        S= np.uint8(Sat*255)
        
        #Tính intersity
        I=np.uint8((R+G+B)/3)

        #gán giá trị mức xám vừa tính cho ảnh xám
        Hue_PIL.putpixel((x, y),(H,H,H))
        Saturation_PIL.putpixel((x, y),(S,S,S))
        Intensity_PIL.putpixel((x, y),(I,I,I))
        HSI_img_PIL.putpixel((x,y),(I,S,H))

#chuyển ảnh từ thư viện PIL sang opencv để hiển thị bằng opencv 
hue_cv=np.array(Hue_PIL)
saturation_cv= np.array(Saturation_PIL)
intensity_cv= np.array(Intensity_PIL)
HSI_cv=np.array(HSI_img_PIL)

#hiển thị ảnh
cv2.imshow('Anh mau RGB goc',img)
cv2.imshow('HUE',hue_cv)
cv2.imshow('SATURATION',saturation_cv)
cv2.imshow('INTENSITY',intensity_cv)
cv2.imshow('HSI',HSI_cv)

cv2.waitKey(0) #bấm bất kỳ nút nào để tắt ảnh
cv2.destroyAllWindows() #giải phóng bộ nhớ
