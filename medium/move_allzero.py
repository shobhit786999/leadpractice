numbers = [0,1,2,3,0,12,14,0]
result = []
zero_count = 0
for num in numbers:
    if num==0:
        zero_count+=1
    else:
        result.append(num)
        
result.extend([0]*zero_count)
print(result)