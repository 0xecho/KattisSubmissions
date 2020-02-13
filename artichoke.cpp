
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

	int main()
	{
		std::ios::sync_with_stdio(false);

		int p,a,b,c,d,n;
		double ld=0.0;
		cin>>p>>a>>b>>c>>d>>n;
		vector<double> ps;
		for(int k=1;k<n+1;k++)
		{
			ps.emplace_back(p*(sin(a*k+b)+cos(c*k+d)+2));
		}
		int g=0;
		for(int i=0;i<ps.size();i++)
		{
			if(ps[i]>=ps[g])
			{
				g=i;
			}
			ld=max(ld,ps[g]-ps[i]);
		}
		cout<<fixed<<setprecision(8)<<ld<<endl;
		return 0;

	}