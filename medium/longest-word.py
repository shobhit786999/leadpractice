sentence = "Python programming is very interesting"
words = sentence.split()
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word
        
print("longes",longest)