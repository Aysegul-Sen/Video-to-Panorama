import cv2
import os
import numpy as np

def framing(videofilename):
    directoryName = videofilename[0:-4]+"_Frames" #directory name for the video
    if (os.path.isdir(directoryName) == False): #the video's directory does not exist. Create one.
        os.mkdir(directoryName)

    capture = cv2.VideoCapture(videofilename) #create VideoCapture object

    number = 0 #will be used when saving frames as jpg files
    while(capture.isOpened()):
        number += 1 #number of frames
        returnValue, imageFrame = capture.read()
        if returnValue: # frame read correctly
            name = directoryName+"/frame#"+str(number)+".jpg"
            print("Creating " + name) #track the process
            cv2.imwrite(name, imageFrame) #save the frame as frame#N.jpg
        else: #when there is no frame left
            break


    capture.release()
    cv2.destroyAllWindows()


framing("ornek_video.mp4")
