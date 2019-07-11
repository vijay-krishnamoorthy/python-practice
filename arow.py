def addd(*num):
    sum=0
    for i in num:
        sum=sum+i
    return sum
def dis(**emp):
    for i,j in emp.items():
        print(i,":\t ",j)
double = lambda x: x**2
