import cv2
import os
import numpy as np
from stitch_2_images import stitch_2_images
from framing import framing
#from PIL import Image

#stitched_image = stitch_2_images("frame_1.jpg", "frame_100.jpg")
#cv2.imwrite("stitched_image.jpg", stitched_image)

def main(videofilename):
    number_of_frames = framing(videofilename) #create frames and return their number
    #print(number_of_frames)
    directoryName = videofilename[0:-4]+"_Frames" #directory name for the video
    #take the frames nad make a list
    frames = []
#    if direction == "right_to_left":
    for i in range(1, number_of_frames):
        img_name = directoryName + "/frame_"+str(i)+".jpg"
        img = cv2.imread(img_name)
        frames.append(img)

    """
    elif direction == "left_to_right":
        for i in range(number_of_frames-1, 0, -1):
            img_name = directoryName + "/frame_"+str(i)+".jpg"
            img = cv2.imread(img_name)
            frames.append(img)
    """

    #do stitching
    #print(len(frames))
    panorama = frames[0] #initialize the panorama to the first frame

    for k in range(1, len(frames)):
        panorama = stitch_2_images(panorama, frames[k])
        print("stitching " + str(k) + "th frame")


    panorama_name = videofilename[0:-4] + "_panorama.jpg"
    cv2.imwrite(panorama_name, panorama)

main("video_2.mp4")
#img1 = cv2.imread("deneme/panorama_0.jpg")
#img2 = cv2.imread("deneme/panorama_1.jpg")
#first_two = stitch_2_images(img1, img2)
#cv2.imwrite("deneme/first_two.jpg", first_two)
