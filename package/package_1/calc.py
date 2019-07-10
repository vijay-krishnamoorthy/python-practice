def add(*num):
    sum=0
    for i in num.items():
        sum=sum+i
    return sum
def mul(*num):
    pro=1
    for i in num:
        pro=pro*i
    return pro
def div(a,b):
    return a/b
def sub(a,b):
    return a-b if(a>b) else b-a
