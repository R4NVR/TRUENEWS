print('hi, we will be counting the number of characters there are in your name')
confirm=input('would you like to continue, kindly respond with a yes or no?.....')
if(confirm=='yes'):
    name=input('please enter your name without leaving any spaces=  ')
    length=len(name)
    print('length of ur name is=.', length)
    
else:
    print('no problem , this is a test code')
    

print('end of program')
s=input('would you like to continue this test code?.... respond with yes if u want to continue')
if(s=="yes"):
    print('we can calculate the grades u will be getting')
    sub=input('enter the sujects=  ')
    sublists=sub.split()
    count=len(sublists)
    print('the total number of subjects are', count)
    marks=(input("enter the marks respectively= "))
    markslists=list(map(int,marks.split()))
    avg=sum(markslists)/count
    print('your average score is=',avg)
    if(avg>=95):
        print('your grade is A+')
    elif(avg>=90):
        print('your grade is A')
    elif(avg>=80):
        print('your grade is b')
    elif(avg>=70):
        print('your grade is c')
    elif(avg>=60):
        print('your grade is d')
    elif(avg>=50):
        print('your grade is e')
    else:
        print('your average score is=', avg,"you need to study as u have failed")
else:
    print('no problem, thankyou')
s=input()