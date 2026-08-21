n = int(input("enter the number : "))
binary = ""

if n==0:
    binary = "0"
    
while n>0:
    reminder = n%2
    binary=str(reminder) + binary
    n =n//2
    
print(binary)