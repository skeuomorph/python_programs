s = input("Please enter a word")
index = len(s) - 1
snew = ''
while index > -1:
    snew += s[index]
    index -= 1

print (snew)
