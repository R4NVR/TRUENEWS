#printing a value n number of times

i=1
while i<=100:
    print(i)
    i+=1
# printing a multiplication table
i=1
n=int(input('enter a number of which u want the table'))
q=int(input('enter a number till which u want the table'))
while i<=q:
    
    print(n,'x',i,'=',n*i)
    i+=1

q=int(input('till what number do u want the given value multiplied by itself= '))
i=1
n=int(input('enter how many number u want to see= '))
while i<=n:
    print(i**q)
    i+=1

nums=[1,4,9,16,25,36,49,64,81,100]
idx=0
while idx< len(nums):
    print(nums[idx])
    idx+=1
