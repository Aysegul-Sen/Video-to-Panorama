import cv2
import os
import numpy as np
#from PIL import Image

#this code works when camera moves from right to left
def stitch_2_images(img1, img2): #arguments are cv2 images
    #load images and turn to grayscale
    #img1 = cv2.imread(image_name1)
    img_grey1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

    #img2 = cv2.imread(image_name2)
    img_grey2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

    #detect keypoints and descriptors using SIFT
    #sift_descriptor = cv2.xfeatures2d.SIFT_create()
    #key_point_1, descriptor_1 = sift_descriptor.detectAndCompute(img_grey1,None)
    #key_point_2, descriptor_2 = sift_descriptor.detectAndCompute(img_grey2,None)

    #detect keypoints and descriptors using ORB
    orb = cv2.ORB_create()
    key_point_1, descriptor_1 = orb.detectAndCompute(img_grey1, None)
    key_point_2, descriptor_2 = orb.detectAndCompute(img_grey2, None)

    #match these keypoints and descriptors
    match = cv2.BFMatcher()
    matches = match.knnMatch(descriptor_1,descriptor_2, k=2) #matches list consist of lists of 2 best matches

    #filter best matches by ratio test
    best_matches = []
    for i,j in matches:
        if i.distance < 0.75*j.distance:
            best_matches.append(i)

    #estimate the homography and stitch
    minimum_match_count = 7
    if len(best_matches) > minimum_match_count:
        source_points = np.float32([ key_point_1[i.queryIdx].pt for i in best_matches ]).reshape(-1,1,2)
        destination_pts = np.float32([ key_point_2[i.trainIdx].pt for i in best_matches ]).reshape(-1,1,2)

        Homo, mask = cv2.findHomography(source_points, destination_pts, cv2.RANSAC,5.0)
        hight,width = img_grey1.shape
        points = np.float32([ [0,0],[0,hight-1],[width-1,hight-1],[width-1,0] ]).reshape(-1,1,2)
        destination = cv2.perspectiveTransform(points,Homo)

        img_grey2 = cv2.polylines(img_grey2,[np.int32(destination)],True,255,3, cv2.LINE_AA)

        result = cv2.warpPerspective(img1, Homo, (img2.shape[1] + img1.shape[1], img2.shape[0]))
        result[0:img2.shape[0], 0:img2.shape[1]] = img2
        return crop(result)
    else:
        print ("Not enough matches - %d/%d" % (len(best_matches),minimum_match_count))
        return None



#crop black regions of the final image
def crop(image):
    #top
    if not np.sum(image[0]):
        return crop(image[1:])
    #bottom
    elif not np.sum(image[-1]):
        return crop(image[:-2])
    #left
    elif not np.sum(image[:,0]):
        return crop(image[:,1:])
    #right
    elif not np.sum(image[:,-1]):
        return crop(image[:,:-2])
    return image
