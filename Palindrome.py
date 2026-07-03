def palindrome(str):
    temp=str[::-1]

    if(temp==str):
        return True
    else:
        return False
    
print(palindrome("121"))
