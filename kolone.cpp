
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
	bool in(string a,char b)
	{

		if(a.find(b)==string::npos)return 0;
		return 1;
	}

	int main()
	{
		std::ios::sync_with_stdio(false);
		int n1,n2,T;
		string s11,s2,s1="";
		cin>>n1>>n2>>s11>>s2>>T;
		for(int i=s11.length()-1;i>=0;i--)s1+=s11[i];
		string s=s1+s2;
		while(T--)
		{
			for(int i=0;i<s.length()-1;i++)
			{
				if(in(s1,s[i]))
				{
					if(in(s2,s[i+1]))
					{
						swap(s[i],s[i+1]);
						i++;
					}
				}

			}
		}
		cout<<s<<endl;

		return 0;

	}
