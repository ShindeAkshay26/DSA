def prime_num(num):
    if num < 2:
        return False
    
    for i in range(2, int(num//2)+1 ):
        if(num%i==0):
            return False

    return True


print(prime_num(16))