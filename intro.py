import cv2 

#colored image - makes a 3D NumPy array
img1 = cv2.imread("C:\\Users\\Hp\\Desktop\\picture\\TDMUNC.jpg", 1)

#black and white image - makes a 2D NumPy array
img = cv2.imread("C:\\Users\\Hp\\Desktop\\picture\\TDMUNC.jpg", 0)

print('The size of the emage can be found using image.shape: {}'.format(img.shape))
print('The size of the emage can be found using image.shape: {}'.format(img1.shape))