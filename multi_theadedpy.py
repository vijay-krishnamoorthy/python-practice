import multiprocessing, time, os
try:
    def fun1():
        for i in range(1,10):
            print("Function 1: ",i,end='')
            time.sleep(1)


    def fun2():
        for i in range(1, 10):
            print("Function 2: ", i, end='')
            time.sleep(1)


    def fun3():
        for i in range(1, 10):
            print("Function 3: ", i, end='')
            time.sleep(1)

    if __name__=='__main__':
        p0=multiprocessing.Process(target=fun1,args=())
        p1=multiprocessing.Process(target=fun2,args=())
        p2=multiprocessing.Process(target=fun3,args=())
        p0.start()
        p2.start()
        p1.start()

        for i in range(1,10):
            print(os.getpid())
except AttributeError as e:
    print(e)
