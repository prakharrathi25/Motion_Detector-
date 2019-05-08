#Step 1: Create a cascade classifier. It will contain the features of the face 
#Step 2: OpenCV will read the image and the features file 
#Step 3: Display the image with the rectangular face box 


#Working 
import cv2 

#Create a CascadeClassifier Object 
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

#Reading the image as it is
img = cv2.imread("C:\\Users\\Hp\\Desktop\\Image Recognition using CV\\Images\\ronaldo1.jpg")

#Reading the image as a grayscale image
#by converting an existing colored image to gray using cvtColor
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img2 = cv2.imread("C:\\Users\\Hp\\Desktop\\Image Recognition using CV\\Images\\ronaldo1.jpg", 0)

#method to search for the face rectangular coordinates of the image 
#ScaleFactor decreases the shape value by 5%, until the face is found ( smaller the value, larger the accuracy )
faces = face_cascade.detectMultiScale(gray_image, scaleFactor = 1.5, minNeighbors = 5)
eyes = eye_cascade.detectMultiScale(gray_image, scaleFactor = 1.005, minNeighbors = 5)
#Adding the rectangular facebox 
for x, y, w, h in faces: 
	img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), (2))

#rectangle function arguments 
# 1. Image to be read 
# 2. x and y coordinates of one corner 
# 3. x and y coordinates of the other corner 
# 4. RGB value of the rectangular outline ( Green )
# 5. Width of the box boundary 

#Adding the eye box 
for x, y, w, h in eyes: 
	img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), (1))
resized = cv2.resize(img, (int(img.shape[1]), int(img.shape[0])))
cv2.imshow('Gray', resized)

cv2.waitKey(0)