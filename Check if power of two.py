def powerTwo(n):
    return n > 0 and (n & ( n - 1 ) ) == 0 #bit operand, converts nums to binary in this case and if the numbers are both powers of two then the result will be 0, resulting in True

print (powerTwo(8))
print (powerTwo(9))
