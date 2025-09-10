import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#Khai báo đường dẫn file
img = r'lena_color.png'
#Đọc ảnh từ thư viên PIL để thực hiện các tác vụ tính toán\

imgPIL =Image.open(img)

def Chuyendoianhmucxam (imgPIL):
    lumi = Image.new(imgPIL.mode, imgPIL.size)
    # lấy kích thước ảnh 
    W= lumi.size[0]
    H= lumi.size[1]
    #Dùng 2 vòng for để quét ảnh gốc
    for x in range(W):
        for y in range(H):
        #Lấy giá trị điểm ảnh
            R, G, B = imgPIL.getpixel((x, y))
            #Công thức chuyển đổi điểm ảnh RGB thành ảnh mức xám bằng phương pháp Luminance
            dentrang = np.uint8(0.2126*R + 0.7152*G + 0.0722*B)

            lumi.putpixel((x, y),(dentrang, dentrang, dentrang))
    return lumi

##Tính Histogram của ảnh xám---------------------------------------------------------------
def TinhHistogram(HinhxamPIL):
    # Mỗi pixel có giá trị từ 0-255
    his =np.zeros(256)
    #Kích thước ảnh
    W= HinhxamPIL.size[0]
    H= HinhxamPIL.size[1]
    #Dùng 2 vòng for để quét ảnh
    for x in range(W):
        for y in range(H):
            #Lấy giá trị xám tại  điểm ảnh (x,y)
            gR, gG, gB = HinhxamPIL.getpixel((x, y))

            his[gR] += 1
    return his

    
### Vẽ biểu đồ
def VeBieuDo(his):
    W = 5
    H = 4
    plt.figure('Biểu đồ Histogram ảnh xám', figsize =(((W, H))), dpi =100)
    trucX = np.zeros(256)
    trucX = np.linspace(0, 256, 256)
    plt.plot(trucX, his, color= 'orange')
    plt.title('Biểu đồ Histogram')
    plt.xlabel('Giá trị mức xám')
    plt.ylabel('Số điểm cùng giá trị mức xám')
    plt.show


## VIẾT CHƯƠNG TRÌNH
# Chuyển ảnh qua ảnh mức xám
HinhxamPIL = Chuyendoianhmucxam(imgPIL)
# Tính Histogram
his = TinhHistogram(HinhxamPIL)
# Chuyển ảnh PIL sang OpenCV
anhxam = np.array(HinhxamPIL)
cv2.imshow('Anh muc xam bang LUMINANCE <21146064- TRUONG TIEN BAO>',anhxam)
# Hiển thị biểu đồ Histogram
VeBieuDo(his)

#bấm phim bất kì để đóng cửa sổ
cv2.waitKey(0)

#Giải phóng bộ nhớ đã cấp cho cửa sổ
cv2.destroyAllWindows()
