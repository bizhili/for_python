from time import time,sleep
from random import randint
from multiprocessing import Process
from os import getpid
def main():
    start=time()
    p1=Process(target=download_task,args=('vvjdfkvbdk',))
    p1.start()
    p2=Process(target=download_task,args=('ghvgvu',))
    p2.start()
    p1.join()
    p2.join()
    end=time()
    print('总共花了%.3f秒'%(end-start))

def download_task(filename):
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(1)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))







if __name__=='__main__':
    main()
