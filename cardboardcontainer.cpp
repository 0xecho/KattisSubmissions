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
#define inf 1000000000000000001;
#define all(c) c.begin(),c.end()
#define mp(x,y) make_pair(x,y)
#define mem(a,val) memset(a,val,sizeof(a))
#define eb emplace_back
#define f first
#define s second

using namespace std;
int factor(int n)
{
	int a;
	if(n%2==0)return 2;
	for(a=3;a<=sqrt(n);a+=2)
	{
		if(n%a==0)
			return a;
	}
	return n;
}


int main()
{
	// std::ios::sync_with_stdio(false);
	
	ll n,r=inf;
	cin>>n;
	
	for(int i=1;i<=sqrt(n);i++)
		for(int j=1;j<=sqrt(n);j++)
		{
				double k = n/(i*j);
				if(i*j*(ll)k == n)
				{
					r=min(r,(ll)(2*(i*j+i*k+j*k)));
				}
		}

	cout<<r;
	return 0;
}
