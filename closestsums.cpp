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
int main()
{
	std::ios::sync_with_stdio(false);
	cin.tie(0);
	ll n;
	ll counter =0;
	while(cin>>n)
	{
		counter++;
		vector<int> v,subs;
		ll tmp;
		for(int i=0;i<n;i++)
		{
			cin>>tmp;
			v.eb(tmp);
		}
		for(int i=0;i<v.size()-1;i++)
		{
			for(int j=i+1;j<v.size();j++)
			{
				subs.eb(v[i]+v[j]);
				// cout<<i<<" "<<j<<" "<<v[i]+v[j]<<endl;
			}
		}
		sort(all(subs));
		// cout<<endl;
		// for(auto x:subs)
		// {
		// 	cout<<x<<endl;
		// }
		// cout<<endl;
		cout<<"Case "<<counter<<":\n";
		int q,qq;
		cin>>q;
		while(q--)
		{
			cin>>qq;
			int x = lower_bound(all(subs),qq)-subs.begin();
			int mn = x;
			if(x>0)
			{
			
				if(abs(subs[mn]-qq)>abs(subs[x-1]-qq)){

				mn = x-1;
				}
			}
			
			if(x<subs.size()-1)
				if(abs(subs[mn]-qq)>abs(subs[x+1]-qq))
					mn = x+1;
			// cout<<mn<<" "<<subs[mn]<<endl;

			cout<<"Closest sum to "<< qq <<" is "<< subs[mn] <<".\n";

		}
	}

	return 0;
}
