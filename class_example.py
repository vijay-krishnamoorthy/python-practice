class a:
    def f1(self):
        return "You're in function 1 of A class"
    def f2(self):
        return "You're in function 2 of A class"
class b(a):
    def f3(self):
        return "You're in function 3 of B class"
    def f4(self):
        return "You're in function 4 of B class"
class c(a):
    def f5(self):
        return "You're in function 5 of C class"
    def f6(self):
        return "You're in function 6 of C class"
class d(b,c):
    def f7(self):
        return "You're in function 7 of D class"
    def f8(self):
        return "You're in function 8 of D class"
o=a()
ob=b()
obj = c()
obje=d()
print(obje.f1())
print(obje.f2())
print(obje.f4())
print(issubclass(b,a))
