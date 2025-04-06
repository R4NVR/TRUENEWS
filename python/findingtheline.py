#check for the line in which the word "learning" comes
word=input('enter the word u need to find')
linenumber=1
data=True 
with open('newfile.txt','r') as f:
     while data:
         data=f.readline()
         if(word in data):
             print(linenumber)
             linenumber+=1