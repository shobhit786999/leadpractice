list1=[1,2,2,3,4,5]
list2=[2,2,4,5]
result =[]
for num in list1:
    if num in list2 and num not in result:
        result.append(num)
        
print(result)