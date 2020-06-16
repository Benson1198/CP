for _ in range(int(input())):
    s = list(input())
    num_of_pairs = 0
    prev = s[0]

    for i in range(len(s)-1):
        if s[i] != prev:
            num_of_pairs += 1
            prev = s[i+1]
        elif i == len(s)-2:
            if s[i+1] != prev:
                num_of_pairs += 1
        else:
            pass
    
    print(num_of_pairs)

