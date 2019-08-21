#主关于边缘检测
import cv2
import numpy as np
def main():#canny检测
    img1=cv2.imread('img/li3.jpg',0)
    cv2.imwrite('img/li5.jpg',cv2.Canny(img1,50,50))
    cv2.imshow('img',cv2.imread('img/li5.jpg'))
    cv2.waitKey()
    cv2.destroyAllWindows()

def main2():#轮廓检测
    img1=np.zeros((200,200),dtype=np.uint8)
    img[50:150,50:150]=255
    ret,thresh=cv2.threshold(img1,127,255,0)
    
    
    
    
    



if __name__=='__main__':
    main()
