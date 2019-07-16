import threading
from datetime import datetime


def s():
    for i in range(1,10):
        print("cubes :",i**2)
        time.sleep(5)

def c():
    for i in range(1,10):
        print('Square :',i**3)
        time.sleep(5)

if __name__=='__main__':
    tc=threading.Thread(target=c,args=())
    ts=threading.Thread(target=s,args=())

    tc.start()
    ts.start()

    for i in range(1,10):
        print("main :",i)
        time.sleep(5)
