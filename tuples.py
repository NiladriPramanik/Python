tup1=(1,"a",True,2,"b",False)

#printing elements of tuple
print(tup1)

#extracting elements of tuple

print(tup1[1:4])

#to extract the last element we need to write index of last + 1.
print(tup1[0:6])  

#finding length of tuple
print(len(tup1))

#concatenating tuples
tup2=(1,'a',2,3)
tup3=(4,'b',5,6)
print(tup2+tup3)

#repeating elements of tuple
tup1=(1,'a',2)
print(tup1*3)

#repeating and concatenating
tup1=(1,'a',2)
tup2=(4,5,6)
print(tup1*2+tup2)

#minimum and maximum value of tuple
tup1=(1,3,2)
print(min(tup1))
print(max(tup1))
