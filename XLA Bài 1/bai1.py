import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog
from tkinter import Tk

#Chọn ảnh từ máy tính
def select_image():
    root = Tk()
    root.withdraw()  # Ẩn cửa sổ chính của Tkinter
    file_path = filedialog.askopenfilename()  # Hộp thoại chọn tệp
    print(f"File selected: {file_path}")
    return file_path

#Đọc ảnh đầu vào
def load_image(path, grayscale=True):
    if grayscale:
        return cv2.imread(path, cv2.IMREAD_GRAYSCALE)  # Đọc ảnh đen trắng
    return cv2.imread(path)  # Đọc ảnh màu

#Ảnh âm tính
def negative_image(image):
    return 255 - image

#Tăng độ tương phản (Linear Stretching)
def increase_contrast(image):
    alpha = 1.5  # Hệ số khuếch đại (alpha > 1 làm tăng độ tương phản)
    beta = 0     # Điều chỉnh độ sáng
    return cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

#Biến đổi log (Log Transform)
def log_transform(image):
    c = 255 / np.log(1 + np.max(image))  # Hằng số c để chuẩn hóa đầu ra
    log_image = c * (np.log(image + 1))
    return np.array(log_image, dtype=np.uint8)

#Cân bằng Histogram
def equalize_histogram(image):
    return cv2.equalizeHist(image)

#Hiển thị kết quả
def display_images(images, titles):
    plt.figure(figsize=(12, 8))  # Tạo cửa sổ hiển thị lớn hơn
    for i in range(len(images)):
        plt.subplot(2, 3, i + 1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])  # Ẩn trục x và y
    plt.show()

#Hàm chính để thực hiện các thao tác xử lý ảnh
def main():
    #Chọn và tải ảnh
    image_path = select_image()
    original_image = load_image(image_path)

    #Thực hiện các thao tác trên ảnh
    negative_img = negative_image(original_image)  # Ảnh âm tính
    contrast_img = increase_contrast(original_image)  # Tăng độ tương phản
    log_img = log_transform(original_image)  # Biến đổi log
    equalized_img = equalize_histogram(original_image)  # Cân bằng histogram

    #Hiển thị kết quả
    images = [original_image, negative_img, contrast_img, log_img, equalized_img]
    titles = ['Original Image', 'Negative Image', 'Increased Contrast', 'Log Transform', 'Histogram Equalized']
    
    display_images(images, titles)

if __name__ == "__main__":
    main()
