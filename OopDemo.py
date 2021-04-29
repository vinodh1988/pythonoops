

#Encapsulation
#Abstraction
#Inheritance
#Polymorphism


class Person:
    def __init__(self,sno,name): #constructor is used to instantiate the class
        self.sno=sno
        self.name=name
   
    def __str__(self):
        return "Sno:{0} , name : {1}".format(self.sno,self.name)

    def Show(self):
        print("Sno:{0} , name : {1}".format(self.sno,self.name))


first=Person(1,"Prakash")
second=Person(2,"Roger")

first.Show()
second.Show()

print(first)
print(second)