def perfectNumber(n):
    tot = 0
    for i in range (1 , n):
        if n % i == 0:
            tot = tot + i

    if tot == n/2:
        return ("The number entered is a perfect number.")
    else:
        return ("The number entered is not a perfect number.")


print(perfectNumber(6))            
        
                
