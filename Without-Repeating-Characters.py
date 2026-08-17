text = "abcabcabcd"
seen = set()
left = 0
longest = 0
for right in range(len(text)):
    while text[right] in seen:
        seen.remove(text[left])
        left +=1
    seen.add(text[right])
    longest = max(longest, right - left +1)
print(longest)