import cv2
import os
import numpy as np

def framing(videofilename):
    directoryName = videofilename[0:-4]+"_Frames"
    if (os.path.isdir(directoryName) == False): #this video's directory does not exist. Create one.
        os.mkdir(directoryName)

    capture = cv2.VideoCapture(videofilename)

    number = 0
    while(capture.isOpened()):
        number += 1
        returnValue, imageFrame = capture.read()
        if returnValue: # frame read correctly
            name = directoryName+"/frame#"+str(number)+".jpg"
            print("Creating " + name)
            cv2.imwrite(name, imageFrame)
        else:
            break


    capture.release()
    cv2.destroyAllWindows()


framing("ornek_video.mp4")
