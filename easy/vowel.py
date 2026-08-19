# count vowel
text = input("enter the char : ")

count = 0
for char in text.lower():
    if char in "aeiou":
        count+=1
        
print("number of vowel :",count)