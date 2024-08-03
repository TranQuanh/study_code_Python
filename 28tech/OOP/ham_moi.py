class Person:
    def __init__(self,name,job):
        self.name=name
        self.job=job
    def __str__(self):
        return f'{self.name} {self.job}'
p1=Person('Nam','dev')
print(p1)