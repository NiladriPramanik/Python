f=open("text.txt")                            #opeing the file
word=input("enter the number to be searched ")#input of word to be searched 
s=f.read()                                    #storing the elements of the file in string s  
list=s.split()                                #storing the elements of the string as a list 
count=0                                       #count  is the variable which stores the number of words 
for i in list :                               #creating ta for loop
    if (i==word):                             #if i is equal to the word that iuis entered  
        count=count+1                         #count is incresed 

print(count)                                  #print the output (count)
     
f.close()                                     #closing the file            
