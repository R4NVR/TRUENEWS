#oops ka concept
class student:
    collegename="ABC college"
    def __init__ ( self ,name, marks):
     self.name = name
     self.marks= marks
     #method defining
    def welcome(self):
     print("welcome student",self.name,'you have got',self.marks,'in your exams')
s1=student("karan",97)
s2=student('arjun',56)
print(s1.name,s1.marks)
print(s1.collegename)
print(s2.name,s2.marks)
print(s2.collegename)

#method ko aise call karte hai
s1.welcome()
s2.welcome()