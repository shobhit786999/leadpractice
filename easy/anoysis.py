n =int(input("enter the  number "))
nterms = int(input("enter the number "))

result = list (map(lambda x : n**x , range(nterms+1)))

for i in range (nterms+1):
     print(result[i])