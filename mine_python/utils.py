#用于保存滤波器模块
import cv2
import numpy
import scipy.interpolate
def main():
    def k1():
        k1=numpy.array([[-1,-1,-1],
                       [-1,18,-1],
                       [-1,-1,-1]])
        return k1
    def k2():
        k2=numpy.array([[-1,-1,-1,-1,-1],
                       [-1,1,2,1,-1],
                       [-1,2,8,2,-1],
                       [-1,2,2,1,-1],
                       [-1,-1,-1,-1,-1]])
        return k2
    print('1')
    
    
if __name__=='__main__':
    main()
