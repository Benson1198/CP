for _ in range(int(input())):
    n = int(input())
    arr = [int(y) for y in input().split()]
    price = {'5':0,'10':0,'15':0}
    ans = "YES"
    
    price[str(arr[0])] += 1
    
    if arr[0] != 5:
        ans = "NO"

    for i in arr[1:]:
        if i == 5:
            price['5'] += 1
        elif i == 10:
            price['10'] += 1
            if price['5'] > 0:
                price['5'] -= 1
            else:
                ans = "NO"
                break
        elif i == 15:
            price['15'] += 1
            if price['10'] > 0:
                price['10'] -= 1
            elif price['5'] > 1:
                price['5'] -= 2
            else:
                ans = "NO"
                break
    print(ans)


        
         

