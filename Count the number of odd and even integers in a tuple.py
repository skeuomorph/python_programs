def countEvenOdd(*t):
    countEven = 0
    countOdd = 0
    for x in t:
        if x % 2 == 0:
            countEven += 1
        else:
            countOdd += 1
    return {"Number of even numbers:": countEven, "Number of odd numbers:": countOdd}
print (countEvenOdd(50,45,30,35,6598243652843))


