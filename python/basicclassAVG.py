class Student:
    def __init__ (self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
    
    def avg(self):
        avg=(self.math+self.phy+self.chem)/3
        print(avg)
maths=int(input("enter maths= "))
phy=int(input("enter phy= "))
chem=int(input("enter chem= "))
s1=Student(phy,chem,maths)
s1.avg()