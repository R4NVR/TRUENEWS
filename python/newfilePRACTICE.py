with open('newfile.txt','w') as f:
   data=f.write("hi i am learning python\n")
   data=f.write('python is a very interesting language')

#replace every python word with java
with open('newfile.txt','r') as f:
    data=f.read()
    newdata=data.replace('python','java')
    print(newdata)

with open('newfile.txt','w') as f:
    f.write(newdata)

#search for the word "learning" in the file
with open("newfile.txt",'r') as f:
     WORD=input('enter the word to be found')
     data=f.read()
     if(data.find(WORD)!=-1):
        #-1 isiliye kia h coz agar -1 nahi mila iska matlab ki koi valid index pe h voh word
         print('found')
     else:
         print('not found')
