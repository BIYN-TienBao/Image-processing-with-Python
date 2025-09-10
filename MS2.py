import numpy as np #thư viện toán học
import cv2     #thư viện xử lí ảnh cho python

#################################################
#21146064- TRƯƠNG TIẾN BẢO

#đọc ảnh màu dùng thư viên opencv
img= cv2.imread('lena_color.png',cv2.IMREAD_COLOR)

#lấy kích thước của ảnh
cao= len(img[0])
rong=len(img[1])

#Khai báo biến để chứa 3 kênh R G B
red =np.zeros((rong,cao,3),np.uint8) #số 3 là 3 kênh
green =np.zeros((rong,cao,3),np.uint8)
blue =np.zeros((rong,cao,3),np.uint8)
#print(red)

#Set zero có các điểm ảnh
# red[:] = [0, 0, 0]
# green[:] = [0, 0, 0]
# blue[:] = [0, 0, 0]

#quét hình
for x in range(rong):
    for y in range(cao):
        
        #lấy giá trị điểm ảnh
        R=img[x, y, 2]
        G=img[x, y, 1]
        B=img[x, y, 0]
        
         #thiết lập màu 
        red [x, y, 2]=R
        green [x, y, 1]=G
        blue[x, y, 0]=B





#Hiện thị hình dùng thư viên opencv
cv2.imshow('Hinh co gai lena goc <21146064- TRUONG TIEN BAO>',img)
cv2.imshow('Kenh RED <21146064- TRUONG TIEN BAO>',red)
cv2.imshow('Kenh GREEN <21146064- TRUONG TIEN BAO>',green)
cv2.imshow('Kenh BLUE <21146064- TRUONG TIEN BAO>',blue)



#bấm phim bất kì để đóng cửa sổ
cv2.waitKey(0)

#Giải phóng bộ nhớ đã cấp cho cửa sổ
cv2.destroyAllWindows()