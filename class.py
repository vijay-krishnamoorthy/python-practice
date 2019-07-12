class Class_name():
    school='School name'
    def __init__(self,name,roll,age,mark):
        self.name=name
        self.roll=roll
        self.age=age
        self.mark=mark

    def display(self):
        s=[]
        s.append(self.name)
        s.append(self.roll)
        s.append(self.age)
        s.append(self.mark)
        return s

s=Class_name('vijay',36,22,90)
#result=s.display()
print(s.display())
        
