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

bool in(int x, vector<int> v)
{
	sort(all(v));
	return binary_search(all(v),x);
}

int main()
{
	std::ios::sync_with_stdio(false);

	int T;
	while(cin>>T)
	{


	// vector<int> found,removed;
	vector<int> found(1000010),removed(1000010);
	
	int temp,c=0;

	while(T--)
	{
		cin>>temp; // 2 2
		if(removed[temp+1]) // false false 
		{
			removed[temp]+=1;
			removed[temp+1]-=1;
		}
		else if(found[temp+1]) //false false
		{
			removed[temp]+=1;
			found[temp+1]-=1;
		}
		else
		{
			found[temp]+=1; // { 2 }
			c++;	// 1
		}
	}
	cout<<c<<endl;// 2 2
	
	}
	return 0;
}
