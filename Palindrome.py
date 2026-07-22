# def palindrome(str):
#     temp=str[::-1]

#     if(temp==str):
#         return True
#     else:
#         return False
    
# print(palindrome("121"))



def palin(n):
    temp=n
    rev=0
    rem=0
    while(n>0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    
    if rev==temp:
        print("Palindrome")
    else:
        print("Not a palindrome")

print(palin(121121))