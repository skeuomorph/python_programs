def isPalindrome(s):
    sback = ''
    index = len(s) - 1
    while index > -1:
        sback += s[index]
        index -= 1
    if sback == s:
        print (sback)
        return ("This string is a palindrome.")
    else:
        print (sback)
        return ("This string is not a palindrome.")

print (isPalindrome('aza'))
        
                
