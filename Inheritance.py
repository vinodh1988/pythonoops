class A:
    def __init__(self,a):
        self.a=a
    
    def show(self):
        print('a is ', self.a)

class C:
    def __init__(self,c):
        self.c=c
    
    def show(self):
        print('c is' ,self.c)

class B(A,C):
    def __init__(self,a,b,c):
        A.__init__(self,a)
        C.__init__(self,c)
        self.b=b
    
    def show(self):
        A.show(self)
        C.show(self)
        print(self.b)


obj=B(34,35,56)
obj.show()

#allowing only essential features hiding background implementation
