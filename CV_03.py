#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   CV_03.py
@Time    :   2019/04/21 22:01:43
@Author  :   Shalor 
@Desc    :   读取一段视屏文件，并检测其中的某个目标
'''

# Here is the code

import cv2 as cv
import numpy as np


def extrace_object_demo():
    """
    目的读取视屏文件，检测其中绿色的目标
    """
    capture = cv.VideoCapture("G:/testdata/Test.mp4")
    while True:
        ret, frame = capture.read()
        if not ret:
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)  # 将RGB色彩空间转换为HSV色彩空间
        # 用inRange函数，输入绿色色域的取值范围，检测绿色的目标
        lower_hsv = np.array([35, 43, 46])
        upper_hsv = np.array([77, 255, 255])
        mask = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)
        cv.imshow("video", frame)
        cv.imshow("mask", mask)
        c = cv.waitKey(40)
        if c == 27:
            break


extrace_object_demo()
