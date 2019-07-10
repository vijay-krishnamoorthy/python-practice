list1=[1,2,3,4,5,6,7,8,9,10]

def square_it(var):
    l=[]
    square = lambda x:x**2
    for i in var:
        l.append(square(i))
    file_object.append(l)
    print(l)
        
def return_odd(r):
    for i in range(0,r):
        val=odd(i)
        if(val):
            print(val,"is a odd number")

def odd(i):
    if(i%2!=0):
            return i

def sum_list(l):
    sum=0
    for i in l:
        sum=sum+i
    print("the list is : ",l)
    print("and addition of all the elements is :")
    return sum

def map_example():
    square = lambda x: x**2
    map_object=map(square,list1)
    return map_object

def _filter_(n):
    od=lambda x: x%2!=0
    l=[]
    for i in range(0,n):
        l.append(i)
    odd_object=filter(od,l)
    return odd_object
