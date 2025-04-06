class student:
    def __init__(self,name, phy, chem ,maths):
        self.name=name
        self.phy=phy
        self.chem=chem
        self.maths=maths
    def avgmarks(self):
        avg=(self.phy+self.maths+self.chem)/3
        
        print(avg)
        
s1=student("karan",89,99,92)
s1.avgmarks()

