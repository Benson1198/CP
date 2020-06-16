def gcd(a,b):
    if b==0:
        return a
    else:
        gcd(b,a%b)

def equiprop(a,p,b,q):
    if ((not p and a) or (not q and b) or (a and (not b) and q) or (not a and b and p)):
        return False
    if(gcd(a,p) and gcd(b,q)):
        return not(a%p) and not(b%q) and a/gcd(a,p)==b/gcd(b,q) and p/gcd(a,p)==q/gcd(b,q)
    if(p):
        return not(a%p)
    if(q):
        return not(b%q)
    return True

def ans(p,q,r):
    if((a==p)+(b==q)+(c==r)>1):
        return 3-(a==p)-(b==q)-(c==r)
    if((a-p==b-q and a-p==c-r) or (equiprop(a, p, b, q) and equiprop(a, p, c, r) and equiprop(b, q, c, r))):
        return 1
    if(c==r):
        return 1 + (a-p!=b-q and not equiprop(a, p, b, q))
    if(a==p):
        return 1 + (c-r!=b-q and not equiprop(c, r, b, q))
    if(b==q):
        return 1 + (a-p!=c-r and not equiprop(a, p, c, r))
    if(a==p or b==q or c==r):
        return 2

    remain=3   
    if(equiprop(a-b, p-q, b-c, q-r)):
        return 2
    remain=min(remain, ans(p+c-r, q+c-r, r+c-r))
    remain=min(remain, ans(p+b-q, q+b-q, r+b-q))
    remain=min(remain, ans(p+a-p, q+a-p, r+a-p))
    
    if(r and not (c%r)):
        remain=min(remain, ans(p*c/r, q*c/r, r*c/r))
    if(q and not (b%q)):
        remain=min(remain, ans(p*b/q, q*b/q, r*b/q))
    if(p and not (a%p)):
        remain=min(remain, ans(p*a/p, q*a/p, r*a/p))
    if(equiprop(a+r-c,p,b+r-c,q)+equiprop(a+q-b,p,c+q-b,r)+equiprop(b+p-a,q,c+p-a,r)):
        return 2
    
    remain=min(remain, ans(p, q+c-r, r+c-r)) 
    remain=min(remain, ans(p+c-r, q, r+c-r))
    remain=min(remain, ans(p, q+b-q, r+b-q))
    remain=min(remain, ans(p+b-q, q+b-q, r))
    remain=min(remain, ans(p+a-p, q, r+a-p))
    remain=min(remain, ans(p+a-p, q+a-p, r))
    
    if(r and not (c%r)):
        remain=min(remain, ans(p, q*c/r, r*c/r))
    if(r and not (c%r)):
        remain=min(remain, ans(p*c/r, q, r*c/r))
    if(q and not (b%q)):
        remain=min(remain, ans(p, q*b/q, r*b/q))
    if(q and not (b%q)):
        remain=min(remain, ans(p*b/q, q*b/q, r))
    if(p and not (a%p)):
        remain=min(remain, ans(p*a/p, q, r*a/p))
    if(p and not (a%p)):
        remain=min(remain, ans(p*a/p, q*a/p, r))
    
    
    return 1 + remain


for _ in range(int(input())):
    p,q,r = [int(y) for y in input().split()]
    a,b,c = [int(y) for y in input().split()]

    print(ans(p,q,r))