i_list=[int(x) for x in input("Enter numbers :").split()]

tgt=int(input("Enter a target value :"))

def two_sum(i_list,tgt):
    n_hashmap={}
    for i,num in enumerate(i_list):
        if tgt-num in n_hashmap:
            return [n_hashmap[tgt-num],i]
        n_hashmap[num]=i
        
    return []


print(two_sum(i_list,tgt))