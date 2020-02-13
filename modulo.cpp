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


bool in(vi a, int b)
{
	for(int i=0;i<a.size();i++)
	{
		if(a[i]==b)
			return true;
	}
	return false;
}

int main()
{
	std::ios::sync_with_stdio(false);
	int T=10;
	// cin.ignore(); must be there when using getline(cin, s)
	int n;
	vi ns;

	while(T--)
	{
		cin>>n;
		if (!in(ns,n%42))
		{
			ns.push_back(n%42);
		}
	}
	cout<<ns.size();
	return 0;
}
