with open('numbers.txt','r') as f:
    data=f.read()
    list=data.split(',')
    print(list)
    print(len(list))
    count=0
    i=0
    while i<len(list):
        val=list[i]
        i+=1
        if int(val) % 2 == 0:
            count+=1
print(count)



