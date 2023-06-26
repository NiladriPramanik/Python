#code for linear search

#creating function
def linear_search(list1, item):
    for i in range(len(list1)):
        if str(list1[i]) == item:
            return i
    return -1


#creating list
list1 = [ 'e',1, 2, 3 ,4 , 5,'a','b','c','#','aman','atul','shantanu','@']

#storing input value from the user
item_input= input("Enter a number , letter , or name for search its index value: ")
item_to_search = item_input.split()

#storing the input item in variable result
result = linear_search(list1, item_input)

#forloop condition for input item to search in the list
for item in item_to_search:
    result=linear_search(list1, item)

    if result == -1:
       print("Element not found")
    else:
       print("Element ",item,"is at", result) #printing the index value of the item
