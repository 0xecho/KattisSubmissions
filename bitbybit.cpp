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
    int T,p1,p2;
    string cmd;
    while(cin>>T && T)
    {

        string bits="????????????????????????????????";
        while(T--)
        {
            
            cin>>cmd;
            
            cin>>p1;

            if(cmd[0]=='A' || cmd[0]=='O')cin>>p2;

            if(cmd[0]=='S')
            {
                bits[p1]='1';
            }
            else if(cmd[0]=='C')
            {
                bits[p1]='0';   
            }
            else if(cmd[0]=='O')
            {
                if(bits[p2]=='1')
                    bits[p1]='1';
                if(bits[p2]=='?' && bits[p1]=='0')
                    bits[p1]='?';
            }
            else
            {
                if(bits[p2]=='0')
                    bits[p1]='0';
                if(bits[p1]=='1' && bits[p2]=='?')
                    bits[p1]='?';
            }

        }
        reverse(bits.rbegin(),bits.rend());
        cout<<bits<<endl;


    }
    


    return 0;
}
