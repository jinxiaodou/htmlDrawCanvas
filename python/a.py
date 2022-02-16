#!/usr/bin/env python
#coding=utf-8
import cv2
import numpy as np
import math

img = cv2.imread("sub/20.jpg")
#打开窗口展示原始图
cv2.imshow("原始图", img) 

#cv2.findContours()函数接受的参数为二值图，即黑白的（不是灰度图），所以读取的图像要先转成灰度的
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
#转成二值图
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
#定义轮廓和层次结构

#检测轮廓
# 第一个参数是寻找轮廓的图像
# 第二个参数是轮廓的检索模式，有四种
# cv2.RETR_EXTERNAL 表示只检测外轮廓
# cv2.RETR_LIST 检测的轮廓不建立等级关系
# cv2.RETR_CCOMP 建立两个等级的轮廓，上面的一层为外边界，里面的一层为内孔的边界信息。如果内孔内还有一个连通物体，这个物体的边界也在顶层。
# cv2.RETR_TREE 建立一个等级树结构的轮廓。
# 第三个参数method为轮廓的近似办法
# cv2.CHAIN_APPROX_NONE 存储所有的轮廓点，相邻的两个点的像素位置差不超过1，即max（abs（x1-x2），abs（y2-y1））==1
# cv2.CHAIN_APPROX_SIMPLE 压缩水平方向，垂直方向，对角线方向的元素，只保留该方向的终点坐标，例如一个矩形轮廓只需4个点来保存轮廓信息
# cv2.CHAIN_APPROX_TC89_L1，CV_CHAIN_APPROX_TC89_KCOS 使用teh-Chinl chain 近似算法
# 返回值
# cv2.findContours()函数返回两个值，一个是轮廓本身，还有一个是每条轮廓对应的属性。
# contour返回值是矩阵[[2,3,4],[4,6,5]]
# hierarchy返回值
contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 
cnt=contours[1]

print(cnt.tolist())
#M提取阈值小于250的部分
#img = img < 250
#cv2.imshow("阈值",img)
#waitKey(50)


#绘制轮廓 第三个参数-1指绘制所有，0 1则是数组下标
# 第一个参数是指明在哪幅图像上绘制轮廓；
# 第二个参数是轮廓本身，在Python中是一个list。
# 第三个参数指定绘制轮廓list中的哪条轮廓，如果是-1，则绘制其中的所有轮廓。后面的参数很简单。
# 第四个参数应该是颜色
# 其中thickness表明轮廓线的宽度，如果是-1（cv2.FILLED），则为填充模式。绘制参数将在以后独立详细介绍。
cv2.drawContours(img,contours,1,(0,0,255),2)  
 
cv2.imshow("img", img)  
#等待5000ms后窗口自动关闭
cv2.waitKey(5000)  
