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
#ảnh này dùng để chưa kết quả chuyển đổi BINARY
binary = Image.new(imgPIL.mode, imgPIL.size)


# lấy kích thước ảnh 
W= binary.size[0]
H= binary.size[1]
#Thiêt lập giá trị ngưỡng để so sánh
nguong = 120

#Dùng 2 vòng for để quét ảnh gốc
for x in range(W):
    for y in range(H):
        #Lấy giá trị điểm ảnh
        R, G, B = imgPIL.getpixel((x, y))

        #Công thức chuyển đổi điểm ảnh RGB thành ảnh mức xám bằng phương pháp Luminance
        dentrang = np.uint8(0.2126*R + 0.7152*G + 0.0722*B)
        
    #Xác định giá trị điểm ảnh nhị phân
        if (dentrang < nguong):
            binary.putpixel((x, y),(0, 0, 0))
        else:
            binary.putpixel((x, y),(255, 255, 255))

            

#chuyển ảnh từ PIL sang OpenCV

anhxam1 = np.array(binary)

#Hiện thị ảnh
cv2.imshow('Hinh co gai lena goc <21146064- TRUONG TIEN BAO>',hinhgoc)
cv2.imshow('Anh muc xam bang AVERAGE <21146064- TRUONG TIEN BAO>',anhxam1)

#bấm phim bất kì để đóng cửa sổ
cv2.waitKey(0)

#Giải phóng bộ nhớ đã cấp cho cửa sổ
cv2.destroyAllWindows()