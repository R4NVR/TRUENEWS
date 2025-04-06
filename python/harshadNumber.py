#harshad number
n=int(input('enter a 3 digit number='))
a= (n // 100) 
b= (n // 10) % 10
c= n % 10
print('the given number is= ',n)
print(a,b,c)
sum=a+b+c
print(sum)
if n%sum==0:
    print("the number is harshad number")
else:
    print('the number is not a harshad number')

#logic that should work for any digit number
'''
number = 12345  # You can change this to any integer
digits = []

while number > 0:
    digit = number % 10  # Get the last digit
    digits.append(digit)  # Append it to the list
    number //= 10  # Remove the last digit

# The digits will be in reverse order
digits.reverse()  # Optional: reverse to maintain original order

print(digits)
'''

    