#finding the value of nCr
from math import factorial


n=int(input('enter the value of n='))
r=int(input('enter the value of r='))
if r>n:
    print('ERROR, n cannot be greater than r')
else:
    
    print(factorial(n)/(factorial(n-r)*factorial(r)))