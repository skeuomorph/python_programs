def stringTest(s):
    d={"Upper_Case":0, "Lower_Case":0}
    for c in s:
        if c.isupper():
            d["Upper_Case"] += 1
        elif c.islower():
            d["Lower_Case"] += 1
        else:
            pass
    return ("Your original string was:", s, "No. of upper case characters:", d["Upper_Case"],"No. of lower case characters:", d["Lower_Case"])

print (stringTest('HeLlO'))
                
