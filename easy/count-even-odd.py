mylist =[1,2,3,4,5,6,7,8,9,10,11,12,14]
countereven=0
counterodd = 0
for number in mylist:
    if number %2==0:
        countereven+=1
        
    else:
        counterodd+=1       
        
print(countereven)
print(counterodd) 