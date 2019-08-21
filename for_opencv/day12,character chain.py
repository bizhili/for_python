import time
from math import sqrt
import re
def main():
    username=input('input your name,and the input your qq number,and then input\
your qq passward:\n')
    qq=re.search(r'^[0-9]\d{7,12}$',username)
    print(qq)
    print('stupid')


if __name__=='__main__':
    main()
