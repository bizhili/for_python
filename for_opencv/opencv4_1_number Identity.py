import cv2
import numpy as np
def updateKnn(knn,train,train_labels,newData=None,newDataLabel=None):
    if newData !=None and newDatalabel !=None:
        print(train.shape,newData.shape)
        newData=newData.reshape(-1,400).astype(np.float32)
        train=np.vstack((train,newData))
        train_labels=np.hstack((train_labels,newDataLabel))
        knn.train(train,cv2.mi.ROW_SAMPLE,train_labels)
        return knn,train,train_labels
def main():
    img=cv2.imread('img/li2.jpg')
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    print(gray.shape)
    cv2.waitKey()
    cells=[np.hsplit(row,gray.shape[1]/20) for row in np.vsplit(gray,gray.shape[0]/20)]
    train=np.array(cells).reshape(-1,400).astype(np.float32)
    k = np.arange(10)
    train_labels = np.repeat(k,500)
    #创建一个K-Nearest Neighbour分类器，训练数据
    knn = cv2.ml.KNearest_create()
    #knn, train, trainLabel = updateKnn(knn, train, train_labels)
    cap=cv2.VideoCapture(0)
    count=0
    while True:
        ret,frame=cap.read()
        rois=[]
        
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
        element = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        gray2 = cv2.dilate(gray, element)
        gray2 = cv2.erode(gray2, element)
        edges = cv2.absdiff(gray, gray2)
    #运用Sobels算子去噪点

        x = cv2.Sobel(edges, cv2.CV_16S, 1, 0)

        y = cv2.Sobel(edges, cv2.CV_16S, 0, 1)

    #convertScaleAbs()函数将其转回原来的uint8形式，否则将无法显示图像

        absX = cv2.convertScaleAbs(x)

        absY = cv2.convertScaleAbs(y)

    #Sobel算子是在两个方向计算的，最后还需要用cv2.addWeighted(...)函数将其组合起来

        dst = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

    #设置一个阈值来对图像进行分类

        ret_1, ddst = cv2.threshold(dst, 50, 255, cv2.THRESH_BINARY)

    #找图片的轮廓
        print(ddst, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.imshow('xx',ddst)
        im,contours = cv2.findContours(ddst, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #把宽度大于10，高度大于20的轮廓用矩形画出

        for c in contours:
            x, y, w, h = cv2.boundingRect(c)
            if w > 10 and h > 20:
                rois.append((x, y, w, h))

    #找到ROI，把每个找到的图通过阈值分类再设置成20x20大小，再设置成一维数组400个灰度值代表这个数字的特征

        digits = []

        for r in rois:

            x, y, w, h = r

            ret_roi, th = cv2.threshold(edges[y:y+h,x:x+w], 50, 255, cv2.THRESH_BINARY)

            th = cv2.resize(th, (20, 20))
    
            out = th.reshape(-1, 400).astype(np.float32)

        #根据knn算法，找到这个数字特征和训练样本的特征进行分类，识别出是哪个数字

            ret_n, result, neighbours, dist = knn.findNearest(out, k=5)

            digit = int(result[0][0])

            digits.append(cv2.resize(th,(20,20)))

        #用矩形画出这个识别数字再写出这个识别数字

            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

            cv2.putText(frame, str(digit), (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

 

        newEdges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

        newFrame = np.hstack((frame, newEdges))

        cv2.imshow('frame', newFrame)

        key = cv2.waitKey(1) & 0xff

    #按空格退出程序

        if key == ord(' '):

            break





if __name__=="__main__":
    main()
