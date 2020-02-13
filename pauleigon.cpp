#include <bits/stdc++.h>
#define min(x,y) x<y?x:y
#define max(x,y) x>=y?x:y


using namespace std;

int main()
{
    int a,b,c;
    cin>>a>>b>>c;


    if((int)floor((b+c)/a)%2==0)cout<<"paul";
    else cout<<"opponent";
}

