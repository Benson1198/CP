def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

for _ in range(int(input())):
    p,q,r = [int(y) for y in input().split()]
    a,b,c = [int(y) for y in input().split()]

    trpt1 = [a-p,b-q,c-r]

    trpt2 = [int(a/p),int(b/q),int(c/r)]

    lst = intersection(trpt1,trpt2)

    ans = len(lst)
    print(ans)


    