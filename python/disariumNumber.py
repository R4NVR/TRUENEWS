
n=int(input('enter a 3 digit number='))
a= (n // 100) 
b= (n // 10) % 10
c= n % 10
print('the given number is= ',n)
print(a,b,c)
disarium=((a)+(b**2)+(c**3))
if disarium==n:
    print('the number is a disarium numner')
else:
    print("not a disarium number")
 