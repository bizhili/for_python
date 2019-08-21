import code_source
import cv2
import numpy as np
from PIL import Image



def main():
    img1=cv2.imread('img/li8.jpg')
    font=cv2.FONT_HERSHEY_SIMPLEX
    camera=cv2.VideoCapture(0)
    while True:
        (grabbed,frame)=camera.read()
        if not grabbed:
            break
        box=code_source.detect(frame)
        if box !=None:
            min=np.min(box,axis=0)
            max=np.max(box,axis=0)
            roi=frame[min[1]-10:max[1]+10,min[0]-10:max[0]+10]
            #得到扫描区域
            roi=cv2.cvtColor(roi,cv2.COLOR_BGR2RGB)
            
    




if __name__=='__main__':
    main()
