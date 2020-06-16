# import math 

# def Log2(x): 
#     if x == 0: 
#         return false; 
  
#     return (math.log10(x) / math.log10(2))

# def isPowerOfTwo(n): 
#     return (math.ceil(Log2(n)) == math.floor(Log2(n)))

# for _ in range(int(input())):
#     ts = int(input())
    
#     ans = 0
#     if ts == 1:
#         ans = 0
#     elif isPowerOfTwo(ts):
#         ans = 0
#     elif ts % 2 != 0:
#         ans = int(ts/2)
#     elif ts % 2 == 0:
#         while ts % 2 == 0:
#             ts /= 2
#             ts = int(ts)
#         ans = int(ts/2)
    
#     print(ans)


//g++  7.4.0

#include <bits/stdc++.h>
using namespace std;

bool powerOfTwo(int n)
{
    return n <= 0 ? false : (n & (n - 1)) == 0;
}

int main()
{
    int a;
    cin >> a;
    while (a--)
    {
        long long int ts;
        
        cin >> ts;

        int ans(0);
        
        if (powerOfTwo(ts))
        {
            while (ts % 2 == 0)
            {
                ts /= 2;
            }
        }
        else if (ts % 2 == 0)
        {
            while (ts % 2 == 0)
            {
                ts = ts / 2;
            
        }

        cout << ts / 2 << endl;
    }
    }
}