#include <bits/stdc++.h>

using namespace std;

int main()
{
    long long n,nq;
    cin>>n;
    long long c=1;
    while(n--)
    {
        int temp;
        vector<long long>v,v1;
        cin>>nq;
        for(long long i=0;i<nq;i++)
        {
            cin>>temp;
            v.push_back(temp);
        }
        for(long long i=0;i<nq;i++)
        {
            cin>>temp;
            v1.push_back(temp);
        }
        sort(v.begin(),v.end());
        sort(v1.begin(),v1.end());
        long long sum=0;
        for(long long i=0;i<nq;i++)
        {
            sum+=v[i]*v1[nq-i-1];
        }
        cout<<"Case #"<<c++<<": "<<sum<<endl;
    }

}
