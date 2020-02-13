#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    string g;
    bool possible[11];
    memset(possible,1,sizeof(possible));
    while(cin>>n && n)
    {
        cin>>g;
        cin>>g;
        if(g=="high")
        {
            for(int i=1;i<11;i++)
            {
                if(i>=n)possible[i]=0;
            }
        }
        else if(g=="low")
        {
            for(int i=1;i<11;i++)
            {
                if(i<=n)possible[i]=0;
            }
        }
        else if(g=="on")
        {
            if(possible[n])cout<<"Stan may be honest"<<endl;
            else cout<<"Stan is dishonest"<<endl;
            memset(possible,1,sizeof(possible));
        }
    }

}
