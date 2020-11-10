import cv2
import os
import numpy as np
#from PIL import Image

def framing(videofilename):

    if videofilename == "video_2.mp4":
        directoryName = videofilename[0:-4]+"_Frames" #directory name for the video frames
        if (os.path.isdir(directoryName) == False): #the video's directory does not exist. Create one.
            os.mkdir(directoryName)

        capture = cv2.VideoCapture(videofilename) #create VideoCapture object

        number = 0 #will be used when saving frames as jpg files
        while(capture.isOpened()):
            number += 1 #number of frames
            returnValue, imageFrame = capture.read()
            if returnValue: # frame read correctly
                imageFrame = cv2.rotate(imageFrame, cv2.ROTATE_90_CLOCKWISE)
                name = directoryName+"/frame_"+str(number)+".jpg"
                print("Creating " + name) #track the process
                cv2.imwrite(name, imageFrame) #save the frame as frame#N.jpg
            else: #when there is no frame left
                break
        capture.release()
        cv2.destroyAllWindows()
        return number





    else:

        directoryName = videofilename[0:-4]+"_Frames" #directory name for the video frames
        if (os.path.isdir(directoryName) == False): #the video's directory does not exist. Create one.
            os.mkdir(directoryName)

        capture = cv2.VideoCapture(videofilename) #create VideoCapture object

        number = 0 #will be used when saving frames as jpg files
        while(capture.isOpened()):
            number += 1 #number of frames
            returnValue, imageFrame = capture.read()
            if returnValue: # frame read correctly
                name = directoryName+"/frame_"+str(number)+".jpg"
                #print("Creating " + name) #track the process
                cv2.imwrite(name, imageFrame) #save the frame as frame#N.jpg
            else: #when there is no frame left
                break
        capture.release()
        cv2.destroyAllWindows()
        return number
