#include <bits/stdc++.h>
#define min(x,y) x<y?x:y
#define max(x,y) x>=y?x:y


using namespace std;

int main()
{
    int a,b,c,cnt=0;
    cin>>a>>b>>c;

    a+=b;
    while(a>=c)
    {
        cnt+=a/c;
        a= a/c + a%c;
    }
    cout<<cnt;
}
