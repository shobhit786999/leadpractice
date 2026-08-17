number = [10,20,12,1,25,65]
largest = float("-inf")
second_largest = float("-inf")
for num in number:
    if num >largest:
        second_largest = largest
        largest = num 
    elif largest > num > second_largest:
        second_largest = num 

print(second_largest)        