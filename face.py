import cv2
#load somepre trained data on face frontals from opencv
trained_face_data=cv2.CascadeClassifier('C:\\Users\\Education\\Downloads\\haarcascade_frontalface_default.xml')
## To capture video from webcam
webcam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
while True:
    

    successful_frame_read, frame=webcam.read()

    # convert image into grayscale
    grayscaled_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 

    #Detect faces
    face_coordinates= trained_face_data.detectMultiScale(grayscaled_img)

    #draw circle around the faces
    
    for (x,y,w,h) in face_coordinates:
        center_coordinates = x + w // 2, y + h // 2
        radius = w // 2 
        cv2.circle(frame, center_coordinates, radius, (0, 255, 0), 3)

    cv2.imshow('Clever Programmer Face Detector',frame)
    
    key=cv2.waitKey(1)  
    #to stop while loop
    if key==81 or key==113:
        break
    
cv2.destroyAllWindows()