#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

void solve()
{
    ll n;
    cin >> n;
    int k = 1;
    ll low = 1, high = n;
    ll t = n;

    while (low <=high)
    {
        ll mid = (ll)(high + low) / 2;
        cout << mid << "\n"<< flush;
        char c;
        cin >> c;
        if (c == 'E')
        {
            break;
        }
        if (low == high)
        {
            low = 1;
            high = n;
            k++;
            break;
        }

        if (k % 2 == 1)
        {
            if (c == 'G')
            {
                low = mid + 1;
            }
            else
            {
                high = mid - 1;
            }
        }

        k++;
    }

    // Assuming truth on odd k
    while (low <=high)
    {
        ll mid = (ll)(high + low) / 2;
        cout << mid << "\n"<< flush;
        char c;
        cin >> c;
        if (c == 'E')
        {
            break;
        }

        if (k % 2 == 0)
        {
            if (c == 'G')
            {
                low = mid + 1;
            }
            else
            {
                high = mid - 1;
            }
        }

        k++;
    }
}

int main()
{
    solve();
}