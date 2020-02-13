
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

int g[111][111];

int main()
{
	std::ios::sync_with_stdio(false);
	cin.tie(0);

	int n,m,a,b;
	double f;


	while(cin>>n>>m && n)
	{
		vector<pair<double,int>> g[10010];
		for(int i=0;i<m;i++)
		{
			cin>>a>>b>>f;
			g[a].push_back({f,b});
			g[b].push_back({f,a});
		}
		priority_queue<pair<double,int>> q;
		double _size[10010];
		for(int i=1;i<=n;i++) _size[i]=0.00000000;
		_size[0] = 1;
		q.push({1,0});

		bool done[10010];
		mem(done,0);

		while(!q.empty())
		{
			int necst = q.top().second; q.pop();
			if(done[necst])continue;
			done[necst]=1;
			for(auto u:g[necst])
			{
				int nn = u.second;
				double factor = u.first;
				// cout<<_size[necst]<<" ";
				// cout<<nn<<" "<<_size[nn]<<" "<<factor<<" == "<<necst<<" "<<_size[necst]<<endl;
				if( _size[necst]*factor > _size[nn])
				{
					_size[nn] = _size[necst]*factor;
					q.push({_size[nn],nn});
				}
			}
		}

		cout<<fixed<<setprecision(4)<<_size[n-1]<<endl;
		// for(int i=1;i<=n;i++)
		// {
		// 	cout<<_size[i]<<" ";
		// }
		// cout<<endl;

	}
	
	
	return 0;
}
