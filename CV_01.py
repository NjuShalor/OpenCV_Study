#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   CV_01.py
@Time    :   2019/04/21 22:10:32
@Author  :   Shalor 
@Desc    :   读取数据，以及不同色域空间的互相转换
'''

# Here is the code

import cv2 as cv


def get_image_info(image):
    """
    获取图像的基本信息
    """
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)


def video_demo():
    """
    打开摄像头，进行实时的数据读取
    """
    capture = cv.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        frame = cv.flip(frame, 1)
        cv.imshow("video", frame)
        c = cv.waitKey(50)
        if c == 27:
            break


def color_space_demo(image):
    """
    不同色域空间的互相转换
    """
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("gray", gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow("hsv", hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow("yuv", yuv)
    Ycrcb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
    cv.imshow("Ycrcb", Ycrcb)


# print("---------- Hello,Python! ----------")
# src = cv.imread("G:/testdata/testIMG/doom.jpg")
# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# cv.imshow("input image", src)
# get_image_info(src)
# gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
# cv.imwrite("G://testdata/testIMG/doom_gray.jpg", gray)
# video_demo()

src = cv.imread("G:/testdata/testIMG/loa.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
color_space_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()
