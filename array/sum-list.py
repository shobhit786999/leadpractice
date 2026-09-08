nobita = [52,74,84,96,51,34,29,51,34,29,83,84,19,65,74]
check = int(input("enter the number which you want to test "))
if check in nobita:
    print("the number present in list ")
    
else:
    print("befor adding ",nobita)
    nobita.append(check)
    print("number was not present but ii added ")
    print(nobita)