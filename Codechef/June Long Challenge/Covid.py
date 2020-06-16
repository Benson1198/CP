for _ in range(int(input())):
    n,p = [int(y) for y in input().split()]
    a = []
    
    if n==1:
        for i in range(1,n+1):
            for j in range(1,n+1):
                print('1',str(i),str(j),str(i),str(j))
                x = int(input())
                if x == 1:
                    a.append(1)
                elif x == 0:
                    a.append(0)
        
    elif n%2 == 0:
        for i in range(1,n+1):
            for j in range(1,n+1,2):
                print('1',str(i),str(j),str(i),str(j+1))
                x = int(input())
                if x == 2:
                    a.append(1)
                    a.append(1)
                elif x == 1:
                    print('1',str(i),str(j),str(i),str(j))
                    x = int(input())
                    if x == 0:
                        a.append(0)
                        a.append(1)
                    elif x ==1:
                        a.append(1)
                        a.append(0)
                elif x == 0:
                    a.append(0)
                    a.append(0)

    elif n%2 ==1:
        for i in range(1,n+1):
            for j in range(1,n+1,2):
                if j == n:
                    print('1',str(i),str(n),str(i),str(n))
                    x = int(input())
                    if x == 1:
                        a.append(1)
                    elif x == 0:
                        a.append(0)
                else:
                    print('1',str(i),str(j),str(i),str(j+1))
                    x = int(input())
                    if x == 2:
                        a.append(1)
                        a.append(1)
                    elif x == 1:
                        print('1',str(i),str(j),str(i),str(j))
                        x = int(input())
                        if x == 0:
                            a.append(0)
                            a.append(1)
                        elif x ==1:
                            a.append(1)
                            a.append(0)
                    elif x == 0:
                        a.append(0)
                        a.append(0)
    
    print(2)
    for i in range(0,(n*n),n):
        st = ' '.join(str(y) for y in a[i:i+n])
        print(st)
    a.clear()
    x1 = int(input())

    
    if x1 == 1:
        continue
    elif x1 == -1:
        break