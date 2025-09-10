import torch
from gfpgan import GFPGANer
import cv2
import numpy as np
from PIL import Image

# Tải mô hình GFPGAN
model_path = 'https://github.com/TencentARC/GFPGAN/releases/download/v1.3.4/GFPGANv1.3.pth'
gfpgan = GFPGANer(model_path=model_path, upscale=4)

def enhance_image(image_path, output_path):
    # Đọc ảnh đầu vào
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Chạy GFPGAN để làm sắc nét ảnh
    _, _, enhanced_img = gfpgan.enhance(img_rgb, has_aligned=False, only_center_face=False, paste_back=True)

    # Chuyển đổi ảnh từ RGB sang BGR
    enhanced_img_bgr = cv2.cvtColor(enhanced_img, cv2.COLOR_RGB2BGR)

    # Lưu ảnh đã được làm sắc nét
    cv2.imwrite(output_path, enhanced_img_bgr)

    # Hiển thị kết quả
    original_img = Image.open(image_path)
    enhanced_img_pil = Image.fromarray(enhanced_img)

    original_img.show(title="Original Image")
    enhanced_img_pil.show(title="Enhanced Image")


# Sử dụng hàm để làm sắc nét ảnh
image_path = 'D:\Thi giac may\PYTHON/10045.png'
output_path = 'D:\Thi giac may\PYTHON/inputs/10045.png'
enhance_image(image_path, output_path)