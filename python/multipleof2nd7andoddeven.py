number=int(input('enter a number= '))
if(number%2==0):
    print('number is even')
else:
    print('the number is odd')
print("continuing with another program, click enter")
s=input()

print('we will find the greatest number of the 3 digits you have entered')
a=int(input('enter the first number= '))
b=int(input('enter the second number= '))
c=int(input('enter the third number= '))
if(a>b and b>c):
    print(a, 'is the greatest')
elif(b>c):
    print(b, 'is the greatest')
elif(c>a):
    print(c, 'is the greatest')

print('we will now check if a number is a multiple of 7 or not')
p=input()

number_=int(input('enter a number'))
if(number_%7==0):
    print('the number is a multiple of 7')
else:
    print('the number is not a multiple of seven')
print('end of the 3 programs , click enter to close the window')
q=input()