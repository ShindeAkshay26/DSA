def fibo(n):
    list1=[0,1]
    if n<1:
        return 0
    elif n==1:
        return 0
    
    while len(list1)<n:
        list1.append(list1[-1]+list1[-2])
        
    return list1



print(fibo(10))
