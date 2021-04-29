
class Complex:
    def __init__(self,real=0,image=0):
        self.real=real
        self.image=image
    
    def __str__(self):
        if(self.real==0 and self.image==0):
            return str(0)
        if(self.image<0): 
            return str(self.real)+"-i"+str(abs(self.image))
        else:
            return str(self.real)+"+i"+str(self.image)
#polymorphism
    def __add__(self,op2): #operator overloading
        result=Complex()
        result.real=self.real+op2.real
        result.image=self.image+op2.image
        return result

number1=Complex(2,3)
number2=Complex(2,-9)
number3=number1+number2

print(number1)
print(number2)
print(number3)