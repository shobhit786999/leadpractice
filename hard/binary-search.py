arr = [2, 5, 8, 12, 16, 23, 38]
target = int(input("Enter target: "))

left = 0
right =len(arr) - 1
found = -1

while left <=right:
    mid= (left + right) // 2
    
    if arr[mid] == target:
        found = mid
        break
    elif arr[mid] < target:
        left =mid+1
        
    else:
        right = mid -1
        
print("index",found)