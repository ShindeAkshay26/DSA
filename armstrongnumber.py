a=int(input("Enter a number"))

def armstrongnum(a):
    temp=a
    rem=0
    sum1=0
    l=len(str(a))
    while(a>0):
        rem=a%10
        sum1=sum1+rem**l
        a=a//10
    
    if(temp==sum1):
        print("Armstrong number")
    else:
        print("Not a armstrong")


print(armstrongnum(a))