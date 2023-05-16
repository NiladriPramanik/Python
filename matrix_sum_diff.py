#program to add 2 matrices using nested loop
X=[[3,4,2],
   [8,9,4],
   [7,4,1]]
Y=[[5,7,2],
   [5,9,3],
   [5,2,1]]

result=[[3,5,8],
        [5,9,1],
        [7,3,1]]
#iterate through rows
for i in range(len(X)):
    #iterate through columns
    for j in range(len(X[0])):
        result[i][j]=X[i][j]+Y[i][j]

for r in result:
    print(r)