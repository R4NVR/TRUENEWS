#file input output ipo
file=open('sample.txt','a')
file.write("something")
file.close()

#'with' syntax
with open('sample.txt','a') as file  
# deleting file
#koi external module download karke laana ho toh write pip or pip3 name
import os 
os.remove('sample.txt')
    