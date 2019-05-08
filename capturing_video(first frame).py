import cv2, time

#Use OpenCV for reading frames / images one by one using a forloop 

#method to create VideoCapture object. 
# 0 to trigger webcam and we can also give the path to the video file
video = cv2.VideoCapture(0)

#adding a frame to the video that we capture 
check, frame = video.read()
#check - returns true if the VideoCapture Object is read 
#frame - represents the first image that the video captures and is a 3D numpy array

# We need to trigger a time sleep 
time.sleep(3) #code paused for three seconds

cv2.imshow("Capturing", frame)

cv2.waitKey(0)
video.release() #will realease the video in some 
cv2.destroyAllWindows() 

