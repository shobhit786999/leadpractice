number = [1,2,3,2,4,5,6,2,3]
seen = set()
duplicate =set()
for num in number:
    if num in seen:
        duplicate.add(num)
        
    else:
        seen.add(num)

print(list(duplicate))        