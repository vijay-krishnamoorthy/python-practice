from threading import Thread
import time

class a(Thread):
    def run(self):
        for i in range(1,10):
            print(i**2)
            time.sleep(1)

def b(Thread):
    def run(self):
        for i in range(1,10):
            print(i**3)
            time.sleep(1)
object_a=a()
object_b=b()

a.start()
b.start()


a.join()

b.join()


for i in range(1,10):
    print("Hello, World!")
    time.sleep(1)