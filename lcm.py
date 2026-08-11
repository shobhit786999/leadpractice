def lcm(a,b):
    grater = max(a, b)
    while True:
        if grater % a == 0 and grater % b == 0:
            return grater
        grater +=1
        
        
num1 = int(input("enter the number"))
num2 = int(input("enter the second number"))
print("lcm", lcm(num1,num2))
