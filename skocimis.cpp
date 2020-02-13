#include <bits/stdc++.h>
#define min(x,y) x<y?x:y
#define max(x,y) x>=y?x:y


using namespace std;

int main()
{
    int a,b,c;
    cin>>a>>b>>c;
    int cnt=0,x;
    swap(a,min(min(a,b),c));
    swap(c,max(max(a,b),c));
    while(a+1!=b || b+1!=c)
    {


        if(abs(a-b)>=abs(b-c))
        {
            c=a+1;
        }
        else{
            a=b+1;
        }

        swap(a,min(min(a,b),c));
        swap(c,max(max(a,b),c));

        cnt++;
    }
    cout<<cnt;
}
