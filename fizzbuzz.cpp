#fizzbuzz question

n=45
i=1
while i<=n:

    if i%15==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")

    
    else :
        print(i)
    i=i+1

print("n is ",n)
