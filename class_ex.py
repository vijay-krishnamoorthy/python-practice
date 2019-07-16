from datetime import datetime

#class syntax
class emp:
    #local variable for the class
    bonus=5000
    #constructor function
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    def getSalary(self):
        return self.salary
    
    def applyHike(self):
        self.salary*=1.04
        return self.salary
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    @classmethod
    def setBonus(cls,amount):
        cls.bonus=amount
    
    @staticmethod
    def isWorkingDay():
        day=datetime.now().strftime('%w')
        if day == '0' or day == '6':
            return False
        else: 
            return True

e_1=emp('vijay',15000)
e_2=emp('Nithil', 15000)
print(e_1.salary)
print(e_2.getSalary())
print(e_1.name)
print(e_2.name)
print(e_1.bonus)
print(e_2.bonus)
emp.setBonus(12000)
print(e_1.bonus)
print(e_2.bonus)
e_1.applyHike()
e_2.applyHike()
print(e_1.__dict__)
print(e_2.__dict__)
print(e_1.__str__())
print(emp.isWorkingDay())