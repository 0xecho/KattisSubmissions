
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
		string a,o="";
		int j=0;
		char vow[5]={'a','e','i','o','u'};
		while(cin>>a)
		{
			for(int i=0;i<a.length();i++)
			{
				for(j=0;j<5;j++)
				{
					if(a[i]==vow[j])
					{
						o+=a[i];
						i+=2;
						break;
					}
				}
				if(a[i]!=vow[j])
				{
					 o+=a[i];
				}
			}
			o+=" ";
		}
		cout<<o.substr(0,o.length()-1);

		return 0;

	}