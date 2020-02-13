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
	string inp;
	while(getline(cin,inp))
	{
		vector<int>v; int tmp;
		stringstream ss;
		ss<<inp;
		while(ss>>tmp)
		{
			v.eb(tmp);
		}

		bool found[3000]={0};
		bool pos= true;
		for(int i=0;i<v.size()-1;i++)
		{
			for(int j=i+1;j<v.size();j++)
			{
				if(found[abs(v[i]-v[j])])
				{
					pos=false;
					break;
				}
				found[abs(v[i]-v[j])]=1;
			}
			if(!pos)
				break;
		}
		bool perfect = 1;
		vector<int> x;
		if(pos)
		{
			for(int i=1;i<=(*max_element(v.begin(), v.end()));i++)
			{
				if(!found[i])
				{
					perfect=0;
					x.eb(i);
				}
				// cout<<found[i]<<" ";
			}
			if(perfect)
				cout<<"perfect"<<endl;
			else
			{
				cout<<"missing ";
				for(auto i:x)
					cout<<i<<" ";
				cout<<endl;
			}
		}

		else
		{
			cout<<"not a ruler\n";
		}

		// for(auto x : v)
		// {
		// 	cout<<x<<endl;
		// }
	}

	return 0;
}
