def powerThree(n):
    while ( n % 3 == 0):
        n /= 3
    return n == 1

print (powerThree(9))
print (powerThree(81))
print (powerThree(21))
