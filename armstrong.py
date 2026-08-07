# start = int(input("enter the number "))
# end = int(input("enter the ending number "))
# for number in range(start,end+1):
#     temp = number
#     sum = 0
#     while number > 0:
#        rem = number % 10 
#        sum += rem**3
#        number  =  number //10
#     if temp == sum :
#         print(" armstrong number ", temp,end ="") 
        
start = int(input("enter the number"))
end = int(input("enter the last number"))
for num in range(start,end+1):
    temp = num
    sum = 0
    while num>0:
        rem = num%10
        sum+=rem**3
        num = num//10
    if temp == sum:
        print("armstrong", temp,end ="")
        
    