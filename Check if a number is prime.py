def primeNum(n):
    if (n < 1) or (n == 1) :
        return ("The number you entered is invalid, please try again.")
    elif (n == 2):
        return ("The number you entered is prime.")
    else:
        for x in range(2,n):
            if (n % x == 0):
                return ("The number you entered is not prime.")
        else:
            return ("The number you entered is prime.")
print (primeNum(9))
        
        
                
