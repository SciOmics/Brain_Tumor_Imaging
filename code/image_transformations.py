#function for creating horizontal reflections of all images in a folder

import os
import numpy as np
import cv2
import imutils
import matplotlib.pyplot as plt

dirname = os.getcwd() + "/data/training_images/test/folder1"

horizontal_reflect = True, 
vertical_reflect = True, 
rotation_90 = True, 
rotation_270 = True

for filename in os.listdir(dirname):
    
    #ignore hidden files
    if not filename.startswith('.'):
        
        print("Processing: ", dirname + "/" + filename)
        
        temp_img = cv2.imread(dirname + "/" + filename)
        temp_img = cv2.cvtColor(temp_img, cv2.COLOR_BGR2RGB)
        rows, cols, dim = temp_img.shape
        
        #horizontal reflection 
        if horizontal_reflect == True:
        
            horizontal_reflection = np.float32([[1,0,0],
                                   [0,-1,rows],
                                   [0, 0,1]])
        
            hreflection_img = cv2.warpPerspective(temp_img,
                                           horizontal_reflection,
                                          (int(cols), int(rows)))
        
            plt.imsave(dirname + "/" + filename.strip(".jpg") + "h.jpg", hreflection_img)
        
        #vertical reflection
        if vertical_reflect == True:
        
            vertical_reflection = np.float32([[-1,0,cols],
                                   [0,1,0],
                                   [0, 0,1]])
        
            vreflection_img = cv2.warpPerspective(temp_img,
                                           vertical_reflection,
                                           (int(cols), int(rows)))
        
            plt.imsave(dirname + "/" + filename.strip(".jpg") + "v.jpg", vreflection_img)
        
        #90 degree rotation
        if rotation_90 == True:
        
            r90_img = imutils.rotate(temp_img,
                                    angle = 90)
        
            plt.imsave(dirname + "/" + filename.strip(".jpg") + "r1.jpg", r90_img)
        
        #270 degree rotation
        if rotation_270 == True:
            
            r270_img = imutils.rotate(temp_img,
                                    angle = 270)
        
            plt.imsave(dirname + "/" + filename.strip(".jpg") + "r2.jpg", r270_img)
