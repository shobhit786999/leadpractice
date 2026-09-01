arr = [1,2,3,4,56,4,9,-1]
small = arr[0]
for i in arr:
    if i < small:
        small = i
print(small)