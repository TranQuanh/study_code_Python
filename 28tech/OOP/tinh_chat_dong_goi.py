class Person:
    def __init__(self,name,job,salary):
        self.name = name #public
        self._job= job #protected
        self.__salary = salary
    def getSalary(self):
        return self.__salary
    def setSalary(self,salary):
        
        self.__salary=salary
        
p1= Person('Teo','job','salary')
print(p1.getSalary())
print(p1.setSalary('hello'))
print(p1.getSalary())