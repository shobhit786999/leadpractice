num = int(input("enter the num "))
if num <2:
    print("not prime")
else:
    prime = True
    for i in range(2,num):
        if num %i ==0:
            prime = False
            break
        
    if prime:
        print("prime number")
    else:
        print("not prime")