num=int(input("Enter an number"))

def fact(num):
    fact=1
    if num==0:
        return 1
    else:
        for i in range(1,num+1):
            fact=fact*i
        return fact
    


print(fact(num))