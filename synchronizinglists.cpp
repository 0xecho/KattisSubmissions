
#include <bits/stdc++.h>

using namespace std;

int main()
{
    int T,temp;

    while(cin>>T && T)
    {
        vector<int> v1,v2,v3;
        map<int,int> mep;
        for(int i=0;i<T;i++)
        {
            cin>>temp;
            v1.push_back(temp);
            v3.push_back(temp);

        }
        for(int i=0;i<T;i++)
        {
            cin>>temp;
            v2.push_back(temp);
//            v4.push_back(temp);

        }
        sort(v1.begin(),v1.end());
        sort(v2.begin(),v2.end());

        for(int i=0;i<T;i++)
        {
            mep[v1[i]]=v2[i];
        }

        for(int i=0;i<T;i++)
        {
            cout<<mep[v3[i]]<<endl;
        }
        cout<<endl;

    }

}
