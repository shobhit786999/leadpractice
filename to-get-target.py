# numbers = [2, 7, 11, 15]
# target = 9

# Output: [0, 1]
number = [2, 7, 11, 15]
target = 9
seen = {}
for i, num in enumerate(number):
    needed = target - num
    if needed in seen :
        print(seen[needed],i)
        break
    seen[num] = i