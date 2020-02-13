    #include <bits/stdc++.h>
    #include <cstdio>
    #include <cstring>
    #include <cmath>
    #include <cstring>
    #include <chrono>
    #include <complex>
    #define endl "\n"
    #define ll long long int
    #define vi vector<int>
    #define vll vector<ll>
    #define vvi vector < vi >
    #define pii pair<int,int>
    #define pll pair<long long, long long>
    #define mod 1000000007
    #define inf 1000000000000000001
    #define all(c) c.begin(),c.end()
    #define mp(x,y) make_pair(x,y)
    #define mem(a,val) memset(a,val,sizeof(a))
    #define eb emplace_back
    #define f first
    #define s second
    #define pb push_back

    using namespace std;

    bitset<100000000> prime;

    int SieveOfEratosthenes(int n)
    {
        int c=0;
        prime[1]=true;
        for (int p=2; p*p<=n; p++)
        {
            if (prime[p] == false)
            {
                for (int i=p*p; i<=n; i += p)
                    prime[i] = true;
            }
        }
        for (int p=2; p<=n; p++)
           if (!prime[p])
              c++;
        return c;
    }

    int main()
    {
        std::ios::sync_with_stdio(false);
        int p,T,n,c=0;
        cin>>p>>T;
        cout<<SieveOfEratosthenes(p)<<endl;
        while(T--)
        {
            cin>>n;
            if( prime[n]) cout<<"0";
            else cout<<"1";
            cout<<endl;
        }
        return 0;

    }

