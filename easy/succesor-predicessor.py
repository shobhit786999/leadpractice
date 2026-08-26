mylist = []
tn= str(input("how many item want to store in list"))
for i in range(tn):
    item = int(input("enter the number "))
    mylist.append(item)
    
mylist.sort()
print(mylist[-1]+1)
print(mylist[-1]-1) 