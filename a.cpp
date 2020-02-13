#include <bits/stdc++.h>

using namespace std;

int main()
{
    string inp;
    cin>>inp;
    int vals[3]={0,0,0};//T,C,G
    for (int i=0;i<inp.size();i++)
    {
        if(inp[i]=='T')vals[0]++;
        else if(inp[i]=='C')vals[1]++;
        else if(inp[i]=='G')vals[2]++;
    }
    int *mult = min_element(vals,vals+3);
    cout<<vals[0]*vals[0]+vals[1]*vals[1]+vals[2]*vals[2]+*mult*7;
    return 0;
}
