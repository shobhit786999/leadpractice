def cal_fact(num):
    fact = 1
    for num in range(1,num+1):
        fact*=num
        
    print(fact)
    
cal_fact(5)