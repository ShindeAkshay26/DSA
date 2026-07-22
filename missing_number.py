list1=[1,2,3,4,6,7]

def missing_num(list1):
    n=list1[-1]
    sum1=0
    total=n*(n+1)//2
    sum1=sum(list1)
    
    return total-sum1


print(missing_num(list1))