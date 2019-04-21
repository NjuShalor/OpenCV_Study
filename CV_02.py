#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   CV_02.py
@Time    :   2019/04/21 22:05:53
@Author  :   Shalor 
@Desc    :   手动实现取反色操作和利用CV2中的API来实现取反色操作，比对其实现时间
'''

# Here is the code

import cv2 as cv
import numpy as np


def access_pixels(image):
    """
    手动实现取反色操作，利用三个for循环
    """
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("height : %s,width : %s,channels : %s" % (height, width, channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                image[row, col, c] = 255 - image[row, col, c]
    cv.imshow("pixels_demo", image)


def create_image():
    """
    自己构造一个400*400,3通道数的随机噪声图
    """
    img = np.random.randint(1, 255, (400, 400, 3), np.uint8)
    cv.imshow("create image", img)


def inverse(image):
    """
    用CV2中的bitwise_not()来实现取反色操作
    """
    dst = cv.bitwise_not(image)
    cv.imshow("inverse image", dst)


# 对同样1920*1080的图片进行取反操作，利用API只要80ms,自己手动实现需要14000ms
src = cv.imread("G:/testdata/testIMG/doom.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
create_image()
t1 = cv.getTickCount()
# access_pixels(src)
inverse(src)
t2 = cv.getTickCount()
time = (t2 - t1) / cv.getTickFrequency()
print("time : %s ms" % (time * 1000))
cv.waitKey(0)
