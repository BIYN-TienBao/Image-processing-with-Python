import cv2;
from PIL import Image; #thư viện pillow hỗ trợ nhiều định dạng ảnh
import numpy as np;

#khai báo đường dẫn file ảnh
filehinh=r'lena_color-0000.jpg'

#đọc ảnh màu dùng emgucv
img=cv2.imread(filehinh,cv2.IMREAD_COLOR)

#đọc ảnh dùng PIL và dùng ảnh PIL để xử lý tính toán thay vì dùng emgucv
imgPIL=Image.open(filehinh)

#tạo 4 ảnh có cùng kích thước với ảnh PIL. Ta dùng ảnh này để chứa kết quả sau khi chuyển đổi RGB->CMYK
Y_channel_PIL=Image.new(imgPIL.mode, imgPIL.size)
Cr_channel_PIL= Image.new(imgPIL.mode,imgPIL.size)
Cb_channel_PIL= Image.new(imgPIL.mode,imgPIL.size)
YCrCb_PIL= Image.new(imgPIL.mode, imgPIL.size)

#lấy kích thước ảnh từ ảnh PIL
width=Y_channel_PIL.size[0]
height=Y_channel_PIL.size[1]

for x in range (width):
    for y in range(height):
        #đọc giá trị pixel tại x,y
        R, G, B=imgPIL.getpixel((x, y))

        #Tính 3 kênh màu XYZ
        kenh_y = np.uint8(16 + (65.738 * R + 129.057 * G + 25.064 * B) / 256)
        kenh_Cr = np.uint8(128 + (-37.945 * R - 74.494 * G + 112.439 * B) / 256)
        kenh_Cb =np.uint8(128 + (112.439 * R - 94.154 * G - 18.285 * B) / 256)

        #gán giá trị mức xám vừa tính cho ảnh xám
        Y_channel_PIL.putpixel((x, y),(kenh_y,kenh_y,kenh_y)) # vị trí màu trong python là B,G,R ngược với trong C#.NET
        Cr_channel_PIL.putpixel((x, y),(kenh_Cr,kenh_Cr,kenh_Cr))
        Cb_channel_PIL.putpixel((x, y),(kenh_Cb,kenh_Cb,kenh_Cb))
        YCrCb_PIL.putpixel((x,y),(kenh_Cb,kenh_Cr,kenh_y))

#chuyển ảnh từ thư viện PIL sang opencv để hiển thị bằng opencv 
Y_cv=np.array(Y_channel_PIL)
Cr_cv= np.array(Cr_channel_PIL)
Cb_cv= np.array(Cb_channel_PIL)
YCrCb_cv=np.array(YCrCb_PIL)

#hiển thị ảnh
cv2.imshow('Anh mau RGB goc',img)
cv2.imshow('KENH MAU Y',Y_cv)
cv2.imshow('KENH MAU Cr',Cr_cv)
cv2.imshow('KENH MAU Cb',Cb_cv)
cv2.imshow('HINH YCrCb',YCrCb_cv)

cv2.waitKey(0) #bấm bất kỳ nút nào để tắt ảnh
cv2.destroyAllWindows() #giải phóng bộ nhớ