import cv2

img = cv2.imread("C:\\Users\\Hp\\Desktop\\picture\\TDMUNC.jpg", 0)

#displaying an image where the first argument is the name of the window 
cv2.imshow("My image", img)

#wait to close until a user presses a key
#cv2.waitKey(0) 

#wait to close for 2000 miliseconds 
cv2.waitKey(2000)

#the fucntion that actually closes all the windows depending on the parameters in the waitkey function 
cv2.destroyAllWindows()


#resizing an image 

#resized_image = cv2.resize(img, (650, 500))
resized_image = cv2.resize(img, (int(img.shape[1]/2) , int(img.shape[0]/2)))
cv2.imshow("New Image", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows() 