
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
	#define pb push_back
	
	using namespace std;
	ll a[100];
	ll fib(ll n) 
	{ 
		if (n <= 1) 
			return n; 
		if (a[n]!=0)
			return a[n];
		a[n]=fib(n-1) + fib(n-2);
		return a[n]; 
	} 

	int main()
	{
		std::ios::sync_with_stdio(false);
		ll n,f;
		cin>>n;
		mem(a,0);
		cout<<fib(n-1)<<" "<<fib(n);
		return 0;

	}
