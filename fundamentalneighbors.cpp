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

const int NN = 47000;

bool isp(ll x)
{
    if(x==2)return 1;
    if(x%2==0)return 0;
    for(int i=3;i<sqrt(x)+1;i++)
    {
        if(x%i==0)return 0;
    }
    return 1;
}


bool primes[NN];

int main()
{
    std::ios::sync_with_stdio(false);
    mem(primes,1);
    // primes[2]=1;
    for(int i=2;i<NN;i++)
    {
    	if(!primes[i])
    		continue;
    	for(int j=i+i;j<NN;j+=i)
    		primes[j]=0;
    }

    ll x,ox;

    while(cin>>x)
    {
    	map<int,int> m;

    	if(x<0)
    	{
    		m[-1]=1;
    		x=-x;
    	}
    	ox=x;
    	bool c = 0;

    	for(int i=2;i<=sqrt(x);i++)
    	{
    		if(!primes[i])continue;
    		if(i*i==x)
			{
				m[i]+=2;
				c=1;
			}
    		else if(x%i==0)
			{
				c=1;
				m[i]++;
				x/=i;
				i=1;
			}
			// cout<<x<<endl;
    	}
    	if(isp(x))
    		m[x]++;

    	ll sum=1;
    	for(auto n:m)
    	{
    		// cout<<n.f;
    		// if(n.s>1)
    		// 	cout<<"^"<<n.s;
 
    		// 	cout<<" ";
    		sum*=pow(n.s,n.f);
    	}
    	cout<<ox<<" "<<sum<<endl;
    }

    return 0;

}

