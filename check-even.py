def even(num):
    list =[]
    for i in num:
        if i % 2 ==0:
            list.append(i)
    return list
result=even([1,2,3,4,5,67,8,9,7,8,8,4])
print(result)