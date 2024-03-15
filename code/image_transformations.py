#function for creating horizontal reflections of all images in a folder

#if __name__ == "__main__":

import os
import numpy as np
import cv2
import imutils
import matplotlib.pyplot as plt

#dirname = os.getcwd() + "/data/training_images/test/folder1"

#horizontal_reflect = True 
#vertical_reflect = True
#rotation_90 = True
#rotation_270 = True

def image_transformations(dirname, 
                          horizontal_reflect = True, 
                          vertical_reflect = True, 
                          rotation_90 = True, 
                          rotation_270 = True):

    #counter
    number_of_images = 0
    
    for filename in os.listdir(dirname):
    
        #ignore hidden files
        if not filename.startswith('.'):
            
            number_of_images += 1
        
            print("Processing: ", dirname + "/" + filename)
        
            temp_img = cv2.imread(dirname + "/" + filename)
            temp_img = cv2.cvtColor(temp_img, cv2.COLOR_BGR2RGB)
            rows, cols, dim = temp_img.shape
        
            #horizontal reflection 
            if horizontal_reflect == True:
            
                print("Performing horizational reflection.")
        
                horizontal_reflection = np.float32([[1,0,0],
                                   [0,-1,rows],
                                   [0, 0,1]])
        
                hreflection_img = cv2.warpPerspective(temp_img,
                                           horizontal_reflection,
                                          (int(cols), int(rows)))
        
                plt.imsave(dirname + "/" + filename.strip(".jpg") + "h.jpg", hreflection_img)
        
            #vertical reflection
            if vertical_reflect == True:
            
                print("Performing vertical reflection.")
        
                vertical_reflection = np.float32([[-1,0,cols],
                                   [0,1,0],
                                   [0, 0,1]])
        
                vreflection_img = cv2.warpPerspective(temp_img,
                                           vertical_reflection,
                                           (int(cols), int(rows)))
        
                plt.imsave(dirname + "/" + filename.strip(".jpg") + "v.jpg", vreflection_img)
        
            #90 degree rotation
            if rotation_90 == True:
            
                print("Performing 90 degree rotation.")
        
                r90_img = imutils.rotate(temp_img,
                                    angle = 90)
        
                plt.imsave(dirname + "/" + filename.strip(".jpg") + "r1.jpg", r90_img)
        
            #270 degree rotation
            if rotation_270 == True:
            
                print("Performing 270 degree rotation.")
            
                r270_img = imutils.rotate(temp_img,
                                    angle = 270)
        
                plt.imsave(dirname + "/" + filename.strip(".jpg") + "r2.jpg", r270_img)
                
    print(f"{number_of_images} images processed.")
