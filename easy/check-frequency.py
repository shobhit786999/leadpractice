s =input("enter string ")
frequency ={}

for ch in s:
    if ch in frequency:
        frequency[ch] +=1
    else:
        frequency[ch] = 1
        
for ch,count in frequency.items():
    print(ch,":",count)