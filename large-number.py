num = int(input("enter the number "))
if num >0:
    fact = 1
    for i in range(1,num+1):
      fact = fact*i
    print(fact)    
    
else:
    print("enter the possitive numbeter")    