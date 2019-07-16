# Enter your code here. Read input from STDIN. Print output to STDOUT
k, m = map(int, input().split())
sum = 0


def square(x): return x*x
for i in range(k):
    n = list(map(int, input().split()))
    val=max(n)
    sum+=square(val)
    smax=sum%m
print(smax)


