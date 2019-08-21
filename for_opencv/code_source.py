import numpy as np
import cv2

def detect(image):
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    #转灰度
    gradX = cv2.Sobel(gray,ddepth = cv2.cv2.CV_32F, dx = 1, dy = 0, ksize = -1)
    gradY=cv2.Sobel(gray,ddepth=cv2.cv2.CV_32F,dx=0,dy=1,ksize=-1)
    #构造梯度幅值
    gradient=cv2.subtract(gradX,gradY)
    gradient=cv2.convertScaleAbs(gradient)
    #从X梯度减去Y梯度
    blurred=cv2.blur(gradient,(9,9))
    (_,thresh)=cv2.threshold(blurred,225,225,cv2.THRESH_BINARY)
    #模糊去噪，与二值化
    kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(21,7))
    closed=cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel)
    ##我们首先使用cv2.getStructuringElement构造一个长方形内核。
    #这个内核的宽度大于长度，
    #因此我们可以消除条形码中垂直条之间的缝隙。
    # 这里进行形态学操作，将上一步得到的内核应用到我们的二值图中，
    #以此来消除竖杠间的缝隙
    closed=cv2.erode(closed,None,iterations=4)
    closed=cv2.dilate(closed,None,iterations=4)
    #膨胀腐蚀去噪点
    (cnts,_)=cv2.findContours(closed.copy(),cv2.RETR_EXTERNAL,
                              cv2.CHAIN_APPROX_SIMPLE)
    if len(cnts)==0:
        return None
    #找到就通过面积排序，计算旋转角
    #给最大轮廓找边框
    c=sorted(cnts,key=cv2.contourArea,reverse=True)[0]
    rect=cv2.minAreaRect(c)
    box=np.int0(cv2.boxPoints(rect))
    #box含四个顶点
    cv2.imshow('hh',closed)
    return box
    
    
    
    

def main():
    print('1')
    img1=cv2.imread('img/li9.jpg',4)
    print(detect(img1))
    




if __name__=='__main__':
    main()
