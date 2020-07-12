#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np

car_classifier=cv2.CascadeClassifier('cars.xml')
cap = cv2.VideoCapture('vehicles.mp4')

while cap.isOpened():
    ret,frame = cap.read()
    cars = car_classifier.detectMultiScale(frame,1.3,2)
    
    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.imshow('Cars',frame)
        
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

