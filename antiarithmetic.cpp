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

    string s;
    int x;
    while(cin>>x)
    {

        if(x==0)break;
        cin>>s;
        int inp;
        int v[10010],idx[10010];
        for(int i=0;i<x;i++)
        {
            cin>>inp;
            v[i]=inp;
            // idx[inp]=i;

        }
        bool done = 0;
        // for(int i=0;i<x-3;i++)
        // {
        //  for(int j=i+1;j<x;j++)
        //  {

        //      // cout<<x<<" "<<i<<" "<<j<<" "<<idx[2*v[j]-v[i]]<<endl;
        //      if(v[j]-v[i]>x-v[j])continue;
        //      if(2*v[j]-v[i]<x && 2*v[j]-v[i]>=0 && idx[2*v[j]-v[i]]>j)
        //      {
        //          done = 1;
        //          break;
        //      }

        //  }
        //  if(done)break;
        // }
        int before,after,diff;
        bool arr[100010] = {0};
        arr[v[0]]=1;
        // arr[x-1]=1;
        // cout<<v[1]<<endl;
        for(int i=1;i<x-1;i++)
        {
        	diff = (x)/2;
        	arr[v[i]]=1;
        	// cout<<diff<<endl;
            for(int j=1;j<=diff;j++)
            {
                before = v[i]-j; after = v[i]+j;
                if(before>=x||before<0||after<0 || after>=x)continue;
                if(arr[before]&&!arr[after])
                {
            	// cout<<before<<" "<<after<<endl;
             //        cout<<i<<" "<<j<<" "<<idx[v[i]+j]<<endl;
                    done=1;
                    break;
                }
                if(arr[after]&&!arr[before])
                {
                    // cout<<i<<" "<<j<<" "<<idx[v[i]+j]<<endl;
                    done=1;
                    break;
                }

            }
            if(done)break;
        }

        if(done)cout<<"no"<<endl;
        else cout<<"yes"<<endl;
    	// cout<<x<<endl;
    }

}


/*
2 4 3 5 0 1

0123456789

012 123 234 345 456 567 678 789
024 135 246 357 468 579
036 147 258 369
048 159



*/