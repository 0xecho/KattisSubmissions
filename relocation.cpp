#include <bits/stdc++.h>
#define min(x,y) x<y?x:y
#define max(x,y) x>=y?x:y


using namespace std;

int main()
{
    unordered_map<long,long> mep;
    int N,Q,temp,a1,a2;
    cin>>N>>Q;

    for(int i=1;i<=N;i++)
    {
        cin>>temp;
        mep[i]=temp;
    }

    for(int i=0;i<Q;i++)
    {
        cin>>temp>>a1>>a2;
        if(temp==1){
            mep[a1]=a2;
        }else{
            cout<<abs(mep[a1]-mep[a2])<<endl;
        }
    }
}
