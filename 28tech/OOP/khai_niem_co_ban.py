class Person:
    # Class attribute: lớp chung cho mọi object  
    nationality = 'Viet Nam'
    # Instance attribute: thay đổi cho từng đối tượng 
    def __init__(self,name,job):
        self.name=name
        self.job=job
    def greet(self):
        return'xin chao'
    
    def info(self):
        return self.name+ ' '+ self.job

p1=Person("Teo", "Dev")
p2=Person('Ti',"Engineer")
print(p1.nationality,p1.name,p1.job)
print(p2.nationality,p2.name,p2.job)
print(p1.greet())
print(p1.info())