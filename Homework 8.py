# -------------------------------------------------------------------------------
# Name:        IS 602 Assignment 8
# Purpose:
#
# Author:      OluwakemiOmotunde
#
# Created:     06/04/2017
# Copyright:   (c) OluwakemiOmotunde 2017
# Licence:     <your licence>
# -------------------------------------------------------------------------------

def main():
    pass


if __name__ == '__main__':
    main()

# This homework will give you a chance to explore some image processing techniques in Python.  These are some of the most basic tasks done in image processing.  First, download the image package attached to this lesson.  On each image you will count the number of objects in the image and find their center points.  The images in order of complexity are circles.png, objects.png and peppers.png. Using Python's built-in functionality, scipy, or any other module, perform the following tasks:

# Thresholding: First convert the image to a binary image.  This is done with a technique called thresholding, which is covered in the reading.  There are functions for it in scipy, although it is very easy to do manually.  Essentially read each pixel and if it above a specified gray level make it white, otherwise make it black.

import scipy as mdimage
from scipy import ndimage
from matplotlib import pyplot as plt
import scipy.misc as misc
import numpy as np
import mahotas as mh


# Now that we have imported our needed modules, we can begin with the peppers image.

peppers = mh.imread('peppers.png')
plt.imshow(peppers)
plt.show()

#Finding the threshold for the peppers image

peppers_thres = mh.otsu(peppers)
peppers_F = (peppers > peppers_thres)
peppers_sm = mh.gaussian_filter(peppers_F, 28)
peppers_regmax = mh.regmax(peppers_sm)
labelsPeppers, near = mh.label(peppers_regmax)
plt.imshow(peppers_sm)
plt.show()


#Now to count the number of objects in the peppers image.

km, peppers_Count = mh.label(peppers_regmax)
print peppers_Count

#Finding center points

peppers_center = mh.center_of_mass(peppers, labelsPeppers)[1:]
print peppers_center



#I have tested out the above for the peppers, so I am hoping to be able to copy and paste for the different images.

objects = mh.imread('objects.png')
plt.imshow(objects)
plt.show()

#Finding the threshold for the peppers image

object_thres = (objects > objects.mean())
object_F = mh.gaussian_filter(objects, 10)
object_regmax = mh.regmax(object_F)
labels_objects, near = mh.label(object_regmax)
plt.imshow(object_regmax)
plt.show()


#Now to count the number of objects in the peppers image.

km, object_Count = mh.label(object_regmax)
print object_Count

#Finding center points

object_center = mh.center_of_mass(objects, labels_objects)[1:]
print object_center



#finally to work with the circles image

circles = mh.imread('circles.png')
plt.imshow(circles)
plt.show()

#Finding the threshold for the peppers image

thres = mh.otsu(circles)
circles_thres = (circles > thres)
circles_F = mh.gaussian_filter(circles, 33)
circles_regmax = mh.regmax(circles_F)
labels_circles, near = mh.label(circles_regmax)
plt.imshow(circles_regmax)
plt.show()


#Now to count the number of objects in the peppers image.

km, circles_Count = mh.label(circles_regmax)
print circles_Count

#Finding center points

circles_center = mh.center_of_mass(circles, labels_circles)[1:]
print circles_center
