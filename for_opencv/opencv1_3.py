import cv2
import numpy as np
from scipy import ndimage
def main():
    k3x3=np.array([[-1,-1,-1],
                   [-1,18,-1],
                   [-1,-1,-1]])
    k5x5=np.array([[-1,-1,-1,-1,-1],
                   [-1,1,2,1,-1],
                   [-1,2,8,2,-1],
                   [-1,2,2,1,-1],
                   [-1,-1,-1,-1,-1]])
    img1=cv2.imread('img/li3.jpg',0)
    k3=ndimage.convolve(img1,k3x3)
    k5=ndimage.convolve(img1,k5x5)
    blurred=cv2.GaussianBlur(img1,(11,11),0)
    g_hpf=img1-blurred
    cv2.imshow('hh',img1)
    cv2.imshow('k3',k3)
    cv2.imshow('k5',k5)
    cv2.imshow('g_hpf',g_hpf)
    cv2.waitKey()
    cv2.destroyAllWindows()
    














if __name__=='__main__':
    main()
