num = int(input("enter the num : "))
sum = 0
while num > 0:
    digit = num % 10
    sum+=digit
    num =num//10
print("sum ",sum)