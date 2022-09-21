from PIL import Image
from pytesseract import pytesseract
import numpy as np
import cv2
import os

#Define path to tessaract
path_to_tesseract = r'/opt/homebrew/Cellar/tesseract/5.2.0/bin/tesseract'

#Define path to image
path_to_images = r'/Users/mohamedibrahim/Documents/gitrepos/4_Semester/Python/read_image/imgs/'

#Point tessaract_cmd
pytesseract.tesseract_cmd = path_to_tesseract

for root, dirs, file_names in os.walk(path_to_images):
    #Iterate over each file_name in the folder
    for file_name in file_names:

        if file_name == '.DS_Store':
            continue
        #Open image with cv2
        img = cv2.imread(path_to_images + file_name)
        #Resize if under 300 dpi
        # img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
        
        #grey scale
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        #remove noise
        kernel = np.ones((1,1), np.uint8)
        print(kernel)
        img = cv2.dilate(img, kernel, iterations=1)
        img = cv2.erode(img, kernel, iterations=1)

        #blur to smooth edges
        #img = cv2.GaussianBlur(img,(5,5), 0)

        # Binarization
        img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


        #Extract text from image
        text = pytesseract.image_to_string(img, lang="eng")
        newtext = text.split()
        serialNumber =[x for x in newtext if x[:2] == '14']

        print("------------")
        print(file_name, ":",text)