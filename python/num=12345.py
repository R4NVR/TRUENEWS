num=12345
for digit in str(num):
    print(int(digit))


number = 12345
digits = []

while number > 0:
    digit = number % 10
    digits.append(digit)
    number //= 10

for digit in reversed(digits):
    print(digit)

    # to get individual digits of a number