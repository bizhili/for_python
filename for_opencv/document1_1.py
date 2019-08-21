import time
from math import sqrt
def is_prime(n):
    for c in range(2,int(sqrt(n))+1):
        if n%c==0:
            return False
    return True if n!=1 else False
def main():
    filenames=('a.txt','b.txt','c.txt')
    fs=[]
    for f in filenames:
        fs.append(open(f,'w'))
    for number in range(1,10000):
        if is_prime(number):
            if number<100:
                fs[0].write(str(number) + '\t')
            elif number<1000:
                fs[1].write(str(number)+'\t')
            else:
                fs[2].write(str(number)+'\t')
    print('that s ok')

def main1():
    try:
        with open('li2.jpg','rb') as p1:
            data=p1.read()
        with open('li3.jpg','wb') as p2:
            p2.write(data)
    except FILENOTFOUND:
        print('dadada')
    print('ok')
    



if __name__=='__main__':
    main1()
