#include <bits/stdc++.h>

using namespace std;

int roots[200010];
int sze[200010];
int N,M;

int root (int i)
{
    while(roots[ i ] != i)
    {
        roots[ i ] = roots[ roots[ i ] ] ;
i = roots[ i ];
    }
return i;
}

void _union(int A,int B)
{
    int root_A = root(A);
    int root_B = root(B);
    if(sze[root_A] < sze[root_B ])
    {
        roots[ root_A ] = roots[root_B];
        sze[root_B] += sze[root_A];
    }
    else
    {
        roots[ root_B ] = roots[root_A];
        sze[root_A] += sze[root_B];
    }

}



bool same_set(int A,int B)
{
    if( root(A)==root(B) )
        return true;
    else
        return false;
}

void initialize( int N)
{
    for(int i = 0; i<N; i++)
    {
        roots[ i ] = i ;
        sze[ i ] = 1;
    }
}

int main()
{
    int t,y;
    cin>>N>>M;

    initialize(N);
    for(int i=0; i<M; i++)
    {
        cin>>t>>y;
        if(!same_set(t,y))_union(t,y);
    }
    int c=0;
    for(int i=1; i<=N; i++)
    {
        if(!same_set(1,i))
        {
            cout<<i<<endl;
            c++;
        }
    }
    if(c==0)cout<<"Connected"<<endl;

}
