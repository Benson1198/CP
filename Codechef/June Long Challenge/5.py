for _ in range(int(input())):
    n = int(input())
    bol = True
    for i in range(1,n**2+1,n):
        if bol:
            arr = [str(y) for y in range(i,i+n)]
            print(' '.join(arr))
            arr.clear()
            bol = False
        else:
            arr = [str(y) for y in range(i,i+n)]
            arr.reverse()
            print(' '.join(arr))
            arr.clear()
            bol = True

        

