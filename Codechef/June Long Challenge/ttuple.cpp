#include <bits/stdc++.h>
using namespace std;

long long a, b, c, p, q, r, t;
long long p1, q1, r1;
long long gcd(long long a, long long b) { return b == 0 ? a : gcd(b, a % b); }

bool equiprop(long long a, long long p1, long long b, long long q1)
{
    if ((!p1 && a) || (!q1 && b) || (a && !b && q1) || (!a && b && p1))
    {
        return false;
    }

    if (gcd(a, p1) && gcd(b, q1))
    {
        return !(a % p1) && !(b % q1) && a / gcd(a, p1) == b / gcd(b, q1) && p1 / gcd(a, p1) == q1 / gcd(b, q1);
    }

    if (p1)
    {
        return !(a % p1);
    }

    if (q1)
    {
        return !(b % q1);
    }

    return true;
}

int ans(long long p1, long long q1, long long r1)
{
    if ((a == p1) + (b == q1) + (c == r1) > 1)
    {
        return 3 - (a == p1) - (b == q1) - (c == r1);
    }

    if ((a - p1 == b - q1 && a - p1 == c - r1) || (equiprop(a, p1, b, q1) && equiprop(a, p1, c, r1) && equiprop(b, q1, c, r1)))
    {
        return 1;
    }

    if (c == r1)
    {
        return 1 + (a - p1 != b - q1 && !equiprop(a, p1, b, q1));
    }

    if (a == p1)
    {
        return 1 + (c - r1 != b - q1 && !equiprop(c, r1, b, q1));
    }

    if (b == q1)
    {
        return 1 + (a - p1 != c - r1 && !equiprop(a, p1, c, r1));
    }

    if (a == p1 || b == q1 || c == r1)
    {
        return 2;
    }

    int remain = 3;
    if (equiprop(a - b, p1 - q1, b - c, q1 - r1))
    {
        return 2;
    }

    remain = min(remain, ans(p1 + c - r1, q1 + c - r1, r1 + c - r1));
    remain = min(remain, ans(p1 + b - q1, q1 + b - q1, r1 + b - q1));
    remain = min(remain, ans(p1 + a - p1, q1 + a - p1, r1 + a - p1));

    if (r1 && !(c % r1))
    {
        remain = min(remain, ans(p1 * c / r1, q1 * c / r1, r1 * c / r1));
    }

    if (q1 && !(b % q1))
    {
        remain = min(remain, ans(p1 * b / q1, q1 * b / q1, r1 * b / q1));
    }

    if (p1 && !(a % p1))
    {
        remain = min(remain, ans(p1 * a / p1, q1 * a / p1, r1 * a / p1));
    }

    if (equiprop(a + r1 - c, p1, b + r1 - c, q1) + equiprop(a + q1 - b, p1, c + q1 - b, r1) + equiprop(b + p1 - a, q1, c + p1 - a, r1))
    {
        return 2;
    }

    remain = min(remain, ans(p1, q1 + c - r1, r1 + c - r1));
    remain = min(remain, ans(p1 + c - r1, q1, r1 + c - r1));
    remain = min(remain, ans(p1, q1 + b - q1, r1 + b - q1));
    remain = min(remain, ans(p1 + b - q1, q1 + b - q1, r1));
    remain = min(remain, ans(p1 + a - p1, q1, r1 + a - p1));
    remain = min(remain, ans(p1 + a - p1, q1 + a - p1, r1));

    if (r1 && !(c % r1))
    {
        remain = min(remain, ans(p1, q1 * c / r1, r1 * c / r1));
    }

    if (r1 && !(c % r1))
    {
        remain = min(remain, ans(p1 * c / r1, q1, r1 * c / r1));
    }

    if (q1 && !(b % q1))
    {
        remain = min(remain, ans(p1, q1 * b / q1, r1 * b / q1));
    }

    if (q1 && !(b % q1))
    {
        remain = min(remain, ans(p1 * b / q1, q1 * b / q1, r1));
    }

    if (p1 && !(a % p1))
    {
        remain = min(remain, ans(p1 * a / p1, q1, r1 * a / p1));
    }

    if (p1 && !(a % p1))
    {
        remain = min(remain, ans(p1 * a / p1, q1 * a / p1, r1));
    }

    return 1 + remain;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> t;
    while (cin >> p >> q >> r >> a >> b >> c)
        cout << ans(p, q, r) << '\n';
    return 0;
}