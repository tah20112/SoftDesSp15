""" Experiment with face detection and image filtering using OpenCV """

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml')
kernel = np.ones((10,10),'uint8')

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()
	faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(40,40))
	for (x,y,w,h) in faces:
		frame[y:y+h,x:x+w,:] = cv2.dilate(frame[y:y+h,x:x+w,:], kernel)
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255))
		cv2.ellipse(frame,(x+int(w/2.0),y+int(2*h/3.0)),(int(w/4.0),int(h/6.0)),0,0,180,(0,0,0),thickness = 5, shift = 0)
		cv2.circle(frame,(x+int(w/3.0),y+int(h/3.0)),int(w/20),(255,255,255),thickness = 10)
		cv2.circle(frame,(x+int(2*w/3.0),y+int(h/3.0)),int(w/20),(255,255,255),thickness = 10)
		cv2.circle(frame,(x+int(w/3.0),y+int(h/3.0)),int(w/50),(255,0,0),thickness = 7)
		cv2.circle(frame,(x+int(2*w/3.0),y+int(h/3.0)),int(w/50),(255,0,0),thickness = 7)
		cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()