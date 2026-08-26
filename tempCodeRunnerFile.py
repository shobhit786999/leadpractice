punc ='''!@#$%^&*();:{}[]-_~<>,\.?/'''
string = input("enter anything here ")
empty = ""
for i in string:
    if i not in punc:
        empty+=i