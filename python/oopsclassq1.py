class student:
    def __init__(self, name , marks ):
     self.name = name 
     self.marks = marks
     
    def average(self):
        sum=0
        for val in self.marks:
            sum+=val
           
        print('your avg is',(sum/3))

           
        
s1=student('tony',[89,45,100])
s1.average()
print('hi',s1.name,"your score is",s1.marks )

