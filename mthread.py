import threading
import time


def s():
    for i in range(1,10):
        print("\tcubes :",i**2,end='')
        time.sleep(1)

def c():
    for i in range(1,10):
        print('Square :',i**3,end='')
        time.sleep(1)

if __name__=='__main__':
    tc=threading.Thread(target=c,args=())
    ts=threading.Thread(target=s,args=())

    tc.start()
    ts.start()
    #thread names
    tc.getName()
    ts.getName()
    ##setting thread setting names
    tc.setName('t1')
    ts.setName('t2')
    #gettig name again
    tc.getName()
    ts.getName()
    for i in range(1,10):
        print("\tmain :",i)
        time.sleep(1)
    if(tc.is_alive()):
        print("Thread 1 is alive")
    else:
        print("Thread 2 is Not alive")