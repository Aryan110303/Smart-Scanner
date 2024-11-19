import numpy as np
import urllib.request as request
import cv2
from PIL import Image
import time

camera = cv2.VideoCapture(0)
while True:
    ret, img = camera.read()
    frame_cvt = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    frame_blur = cv2.GaussianBlur(frame_cvt, (5,5),-1)
    frame_edge = cv2.Canny(frame_blur, 30, 50)
    contours, h = cv2.findContours(frame_edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        max_contours = max(contours, key=cv2.contourArea)
        x,y,w,h = cv2.boundingRect(max_contours)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cv2.imshow('My Scanner', img)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            img_pil = Image.fromarray(img)
            time_str = time.strftime('%Y-%m-%d-%H-%M-%S')
            img_pil.save(f'{time_str}.pdf')
            print(time_str)
