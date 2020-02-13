#include<bits/stdc++.h>

using namespace std;

#define MX 32000

int primes[MX+10];

int main(){

    memset(primes,-1,sizeof(primes));

    for(int i=2;i<MX;i+=1)
    {
        if(primes[i]!=-1)continue;
        primes[i]=1;
        for(int j=i*2;j<MX;j+=i)
        {
            primes[j]=0;
        }
    }

    int t,x;
    cin>>t;
    vector<pair<int,int>>pos;
    while(t--)
    {
        cin>>x;
        for(int i=2;i<=x/2;i++)
        {
            if(primes[i]==1&&primes[x-i]==1)pos.emplace_back(make_pair(i,x-i));
        }
        cout<<x<<" has "<<pos.size()<<" representation(s)"<<endl;
        for(auto i:pos)
        {
            cout<<i.first<<"+"<<i.second<<endl;
        }
        cout<<endl;
        pos.clear();
    }

}
