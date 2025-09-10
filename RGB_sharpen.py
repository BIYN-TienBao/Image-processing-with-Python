import cv2;
from PIL import Image; #thư viện pillow hỗ trợ nhiều định dạng ảnh
import numpy as np;
from scipy import signal;

#khai báo đường dẫn file ảnh
filehinh=r'lena_color.png'

#đọc ảnh màu dùng emgucv
img=cv2.imread(filehinh,cv2.IMREAD_COLOR)

#đọc ảnh dùng PIL và dùng ảnh PIL để xử lý tính toán thay vì dùng emgucv
imgPIL=Image.open(filehinh)

#tạo 2 ảnh có cùng kích thước với ảnh PIL.
sharp_PIL=Image.new(imgPIL.mode, imgPIL.size)


width=sharp_PIL.size[0]
height=sharp_PIL.size[1]
mask_x=3
mask_y=3
filter_mask=np.array([[0,1,0],
                      [1,-4,1],
                      [0,1,0]])


for x in range (1,width-1):
    for y in range(1,height-1):
        RED=0
        GREEN=0
        BLUE=0
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                R, G, B=imgPIL.getpixel((i,j))  #dang sai
                lap_red=(R*filter_mask[i-x+1,j-y+1])
                lap_green=(G*filter_mask[i-x+1,j-y+1])
                lap_blue=(B*filter_mask[i-x+1,j-y+1])
                

                RED += lap_red
                GREEN +=lap_green
                BLUE +=lap_blue
        
                Rs,Gs,Bs=imgPIL.getpixel((x,y))
                kenh_R=(Rs+(-RED))  #sau khi da lam sac net
                kenh_G=(Gs+(-GREEN))
                kenh_B=(Bs+(-BLUE))
                sharp_PIL.putpixel((x, y),(kenh_B,kenh_G,kenh_R))            
                
sharp_cv=np.array(sharp_PIL)

cv2.imshow('Anh mau RGB goc',img)
cv2.imshow('sharpen',sharp_cv)

cv2.waitKey(0) #bấm bất kỳ nút nào để tắt ảnh
cv2.destroyAllWindows() #giải phóng bộ nhớ