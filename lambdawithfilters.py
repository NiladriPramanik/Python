#lambda functions with filters

#filtering odd numbers from a list

list1=[4,5,34,33,65,76,89,10,9]
final_list=list(filter(lambda x:x%2!=0,list1))

print("odd numbers are ",final_list)

#filtering even numbers

final_list=list(filter(lambda x:x%2==0,list1))
    
print("even numbers are",final_list)

    
