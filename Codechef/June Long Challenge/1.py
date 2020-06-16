for _ in range(int(input())):
    n,k = [int(y) for y in input().split()]
    arr = [int(y) for y in input().split()]

    loss = 0

    for i in arr:
        if i > k:
            loss += i-k

    print(loss)