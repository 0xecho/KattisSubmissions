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
string rev(string b)
{
	string s="";
	for(int i=0;i<b.size();i++)
	{
		if(b[i]=='0')s+='1';
		else s+='0';
	}
	return s;
}
int main()
{

	std::ios::sync_with_stdio(false);
	int n;
	cin>>n;
	string a,b;
	cin>>a>>b;
	if(n%2)
	{
		string s=rev(b);
		if(a==s)cout<<"Deletion succeeded";
		else cout<<"Deletion failed";
	}
	else{
		if(a==b)cout<<"Deletion succeeded";
		else cout<<"Deletion failed";
	}
	return 0;
}
