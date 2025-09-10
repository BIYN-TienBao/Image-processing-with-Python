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
x_PIL=Image.new(imgPIL.mode, imgPIL.size)
y_PIL= Image.new(imgPIL.mode,imgPIL.size)
z_PIL= Image.new(imgPIL.mode,imgPIL.size)
xyz_PIL= Image.new(imgPIL.mode, imgPIL.size)

#lấy kích thước ảnh từ ảnh PIL
width=x_PIL.size[0]
height=x_PIL.size[1]

for x in range (width):
    for y in range(height):
        #đọc giá trị pixel tại x,y
        R, G, B=imgPIL.getpixel((x, y))

        xyz_parameter_matrix= np.array([[0.4124564, 0.3575761, 0.1804375],            # nhớ sau này hỏi
                                        [0.2126729, 0.7151522, 0.0721750],
                                        [0.0193339, 0.1191920, 0.9503041]])
        RGB_matrix = np.array([[R],
                               [G],
                               [B]])
        
        xyz_img_matrix = np.dot(xyz_parameter_matrix,RGB_matrix) #matmul và .product dùng để nhân 2 ma trận, 
        #riêng .product thì sẽ chuyển vị ma trận trước rồi mới nhân
        #dùng method .dot cũng có thể nhân 2 ma trận được
        kenh_x= np.uint8(xyz_img_matrix[0,0])
        kenh_y= np.uint8(xyz_img_matrix[1,0])
        kenh_z =np.uint8(xyz_img_matrix[2,0])

        #Tính 3 kênh màu XYZ
        # kenh_x = np.uint8(0.4124564 * R + 0.3575761 * G + 0.1804375 * B)
        # kenh_y = np.uint8(0.2126729 * R + 0.7151522 * G + 0.0721750 * B)
        # kenh_z =np.uint8(0.0193339 * R + 0.1191920 * G + 0.9503041 * B)

        #gán giá trị mức xám vừa tính cho ảnh xám
        x_PIL.putpixel((x, y),(kenh_x,kenh_x,kenh_x)) # vị trí màu trong python là B,G,R ngược với trong C#.NET
        y_PIL.putpixel((x, y),(kenh_y,kenh_y,kenh_y))
        z_PIL.putpixel((x, y),(kenh_z,kenh_z,kenh_z))
        xyz_PIL.putpixel((x,y),(kenh_z,kenh_y,kenh_x))

#chuyển ảnh từ thư viện PIL sang opencv để hiển thị bằng opencv 
x_cv=np.array(x_PIL)
y_cv= np.array(y_PIL)
z_cv= np.array(z_PIL)
xyz_cv=np.array(xyz_PIL)

#hiển thị ảnh
cv2.imshow('Anh mau RGB goc',img)
cv2.imshow('KENH MAU X',x_cv)
cv2.imshow('KENH MAU Y',y_cv)
cv2.imshow('KENH MAU Z',z_cv)
cv2.imshow('XYZ image',xyz_cv)

cv2.waitKey(0) #bấm bất kỳ nút nào để tắt ảnh
cv2.destroyAllWindows() #giải phóng bộ nhớ
# print(xyz_img_matrix.shape)
# print(xyz_img_matrix)