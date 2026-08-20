numbers = [2,2,3,5,6,4,7,8,9,2,2,56]
for num in numbers:
    if numbers.count(num) > len(numbers) //2:
        print("majority element ",num)
        break