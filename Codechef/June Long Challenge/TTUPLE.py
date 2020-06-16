from functools import reduce
import numpy as np


# All factors -ve and +ve
def all_factors(n):
    arr = []
    if n < 0:
        n *= -1
    p = set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    lst_p = list(p)
    arr = [(-1*y) for y in lst_p]
    arr = arr + lst_p
    return arr

# all difference equality
def all_diff_equal(p,q,r,a,b,c):
    if ((a-p) == (b-q)) and ((b-q) == (c-r)):
        return True
    else:
        return False

# all quotient equal
def all_quo_equal(p,q,r,a,b,c):
    if ((a/p) == (b/q)) and ((b/q) == (c/r)):
        return True
    else:
        return False

# any two diff equality
def any_2_diff(p,q,r,a,b,c):
    if ((a-p) == (b-q)) or ((b-q) == (c-r)) or ((a-p) == (c-r)):
        return True
    else:
        return False

# one is same and other two have dame difference
def one_same_2_diff_same(p,q,r,a,b,c):
    if (a-p) == (b-q) and c==r:
        return True
    elif (b-q) == (c-r) and a==p:
        return True
    elif (a-p) == (c-r) and b==q:
        return True
    else:
        return False

# any two quotient equality
def any_2_quo(p,q,r,a,b,c):
    if ((a/p) == (b/q)) or ((b/q) == (c/r)) or ((a/p) == (c/r)):
        return True
    else:
        return False

# any 2 of a,b,c == 0
def two_0_check(a,b,c):
    if a ==0 and b== 0:
        return True
    elif b ==0 and c== 0:
        return True
    elif c ==0 and a== 0:
        return True
    else:
        return False 

# two times addition (ans = 2)
def plus_plus(p,q,r,a,b,c):
    x = a-p
    y = b-q
    z = c-r

    if (x+y == z) or (y+z == x) or (x+z == y) or x==y or y==z or z==x:
        return True
    else:
        return False

# two times multiply (ans = 2)
def multiply_multiply(p,q,r,a,b,c):
    if (a%p == 0) and (b%q == 0) and (c%r == 0):
        x = a/p
        y = b/q
        z = c/r

        if (x*y == z) or (y*z == x) or (x*z == y) or x==y or y==z or z==x:
            return True
        else:
            return False
    else:
        return False

# fisrt plus then multiply
def plus_multiply(p,q,r,a,b,c):
    if a!=0:
        fact_a = all_factors(a)
        for i in fact_a:
            if a%i ==0:
                x = (a/i) - p
            else:
                x = a-p
            
            if (b-q == x or (b%q==0 and (b/i -q) == 0 or (b/i-q)== x)):
                if (c-r == x or (c%r==0 and (c/i -r) == 0 or (c/i-r)== x)):
                    return True

    if b!=0:
        fact_b = all_factors(b)
        for i in fact_b:
            if b%i ==0:
                x = (b/i) - q
            else:
                x = b-q
            
            if (a-p == x or (a%p==0 and (a/i -p) == 0 or (a/i-p)== x)):
                if (c-r == x or (c%r==0 and (c/i -r) == 0 or (c/i-r)== x)):
                    return True
    
    if c!=0:
        fact_c = all_factors(c)
        for i in fact_c:
            if c%i ==0:
                x = (c/i) - r
            else:
                x = c-r
            
            if (a-p == x or (a%p==0 and (a/i -p) == 0 or (a/i-p)== x)):
                if (b-q == x or (b%q==0 and (b/i -q) == 0 or (b/i-q)== x)):
                    return True
    
    return False

# fisrt multiply then plus
def multiply_plus(p,q,r,a,b,c):
    a1 = q-p
    b1 = r-q
    c1 = p-r

    x = b-a
    y = c-b
    z = a-c

    if a1 != 0:
        if x %a1 == 0:
            k = x/a1
            d = a-k*p
            if r* k + d == c or r*k == c or r+d ==c:
                return True
    elif b1 != 0:
        if y %b1 == 0:
            k = y/b1
            d = b-k*q
            if p* k + d == a or p*k == a or p+d ==a:
                return True
    elif c1 != 0:
        if z %c1 == 0:
            k = z/c1
            d = c-k*r
            if q* k + d == b or q*k == b or q+d ==b:
                return True
    
    d = a-p
    if p!= 0 and q!=0:
        if (b-d)%q == 0:
            k = (b-d)/q
            if r*k ==c or r*k +d == c:
                return True
            if b%q == 0:
                k = b/q
                if r*k == c or r*k+d == c:
                    return True
    d = b-q
    if q!= 0 and r!=0:
        if (c-d)%r == 0:
            k = (c-d)/r
            if p*k ==a or p*k +d == a:
                return True
            if c%r == 0:
                k = c/r
                if p*k == a or p*k+d == a:
                    return True
    d = c-r
    if r!= 0 and p!=0: 
        if (a-d)%p == 0:
            k = (a-d)/p
            if q*k ==b or q*k +d == b:
                return True
            if a%p == 0:
                k = a/p
                if q*k == b or q*k+d == b:
                    return True
    return False

# Misc Cases
# plus multiply nad multiply plus case
def equations(p,q,r,a,b,c):
    try:
        A = np.array([[p, 1], [q, 1]])
        B = np.array([a, b])
        X = np.linalg.solve(A,B)
        x = X[0]
        y = X[1]
        if x == int(x) and y == int(y):
            if c == x*r + y:
                return True
    except:
        pass
    
    try:
        A = np.array([[p, 1], [q, 0]])
        B = np.array([a, b])
        X = np.linalg.solve(A,B)
        x = X[0]
        y = X[1]
        if x == int(x) and y == int(y):
            if c == r + y:
                return True
    except:
        pass
    
    try:
        A = np.array([[p, 1], [0, 1]])
        B = np.array([a, b-q])
        X = np.linalg.solve(A,B)
        x = X[0]
        y = X[1]
        if x == int(x) and y == int(y):
            if c == x*r:
                return True
    except:
        pass
    
    try:
        A = np.array([[p, 1], [q, 0]])
        B = np.array([a, b])
        X = np.linalg.solve(A,B)
        x = X[0]
        y = X[1]
        if x == int(x) and y == int(y):
            if c == x*r:
                return True
    except:
        pass

    try:
        A = np.array([[p, 1], [0, 1]])
        B = np.array([a, b-q])
        X = np.linalg.solve(A,B)
        x = X[0]
        y = X[1]
        if x == int(x) and y == int(y):
            if c == r + y:
                return True
    except:
        pass
    
    try:
        A = np.array([[p, 1], [q, 1]])
        B = np.array([a, b])
        X = np.linalg.solve(A,B)
        x = X[0]
        y = X[1]
        if x == int(x) and y == int(y):
            if c == x*r:
                return True
    except:
        pass

    try:
        A = np.array([[p, 1], [q, 1]])
        B = np.array([a, b])
        X = np.linalg.solve(A,B)
        x = X[0]
        y = X[1]
        if x == int(x) and y == int(y):
            if c == r + y:
                return True
    except:
        pass
    
    return False

def any_one_equal_diff(p,q,r,a,b,c):
    if a==p and b!=q and c!=r:
        if b-q != c-r:
            return True
    elif b==q and a!=p and c!=r:
        if a-p != c-r:
            return True
    elif c==r and b!=q and a!=p:
        if b-q != a-p:
            return True
    else:
        return False

def any_one_equal_diffprod(p,q,r,a,b,c):
    if a==p and b!=q and c!=r:
        if (b-q != c-r) and (b/q != c/r) :
            return True
    elif b==q and a!=p and c!=r:
        if (a-p != c-r) and (a/p != c/r):
            return True
    elif c==r and b!=q and a!=p:
        if (b-q != a-p) and (b/q != a/p):
            return True
    else:
        return False
        
    
for _ in range(int(input())):
    p,q,r = [int(y) for y in input().split()]
    a,b,c = [int(y) for y in input().split()]

    ans = 3

    # Case where ans == 0

    if p==a and q==b and r==c:
        ans = 0

    # Case with ans == 1
    elif all_diff_equal(p,q,r,a,b,c) :
        ans = 1
    
    elif a==b and b==c and c == 0:
        ans = 1
    
    elif one_same_2_diff_same(p,q,r,a,b,c):
        ans = 1

    elif p != 0 and q != 0 and r != 0:
        # Case where ans == 1
        if all_quo_equal(p,q,r,a,b,c):
            ans = 1
        
        # ans == 2
        elif any_one_equal_diffprod(p,q,r,a,b,c):
            ans = 2

        elif any_2_diff(p,q,r,a,b,c):
            ans = 2
        
        elif any_2_quo(p,q,r,a,b,c):
            ans = 2

        elif a == b and b == c:
            ans = 2

        elif two_0_check(a,b,c):
            ans = 2
        
        elif plus_plus(p,q,r,a,b,c):
            ans = 2
        
        elif multiply_multiply(p,q,r,a,b,c):
            ans = 2

        elif equations(p,q,r,a,b,c):
            ans = 2
        
        elif equations(r,p,q,c,a,b):
            ans = 2
        
        elif equations(q,r,p,b,c,a):
            ans = 2
        
        elif equations(q,p,r,b,a,c):
            ans = 2
        
        elif equations(p,r,q,a,c,b):
            ans = 2
        
        elif equations(r,q,p,c,b,a):
            ans = 2
        
        elif plus_multiply(p,q,r,a,b,c):
            ans = 2
        
        elif multiply_plus(p,q,r,a,b,c):
            ans = 2
        
        else:
            ans = 3
        

    else:
        if any_2_diff(p,q,r,a,b,c):
            ans = 2
        elif a == b and b == c:
            ans = 2

        elif any_one_equal_diff(p,q,r,a,b,c):
            ans = 2

        elif two_0_check(a,b,c):
            ans = 2
        
        elif plus_plus(p,q,r,a,b,c):
            ans = 2

        elif equations(p,q,r,a,b,c):
            ans = 2
        
        elif equations(r,p,q,c,a,b):
            ans = 2
        
        elif equations(q,r,p,b,c,a):
            ans = 2
        
        elif equations(q,p,r,b,a,c):
            ans = 2
        
        elif equations(p,r,q,a,c,b):
            ans = 2
        
        elif equations(r,q,p,c,b,a):
            ans = 2
        
        elif multiply_plus(p,q,r,a,b,c):
            ans = 2
        
        else:
            ans = 3
    
    print(ans)
    



# def all_factors(n):
#     arr = []
#     if n < 0:
#         n *= -1
#     elif n ==0:
#         pass
#     else:
#         p = set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
#         lst_p = list(p)
#         arr = [(-1*y) for y in lst_p]
#         arr = arr + lst_p
#     if n==0:
#         arr = [0]
#     return arr