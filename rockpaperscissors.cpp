#include <bits/stdc++.h>

using namespace std;

int check(int p1,string m1,int p2,string m2)
{
    if(m1=="rock")
        if(m2=="paper") return p2;
        else if(m2=="scissors") return p1;
        else return 0;
    if(m1=="paper")
        if(m2=="rock") return p1;
        else if(m2=="scissors") return p2;
        else return 0;
    if(m1=="scissors")
        if(m2=="paper") return p1;
        else if(m2=="rock") return p2;
        else return 0;

}

int main()
{
    int n,k;
    string m1,m2;
    int p1,p2,w,l;

    while(cin>>n && n)
    {
        int win[110],loss[110];
        bool played[110];
        fill(win,win+110,0);
        fill(loss,loss+110,0);
        fill(played,played+110,0);
        cin>>k;
        for(int i=0;i<(k*n*(n-1))/2;i++)
        {
            cin>>p1>>m1>>p2>>m2;
            w = check(p1,m1,p2,m2);
            if(w)
            {
                l = w==p2?p1:p2;
                played[p1]=true;
                played[p2]=true;
                win[w]++;
                loss[l]++;

            }

        }
        for(int i=1;i<n+1;i++)
        {


            if(!played[i])cout<<"-"<<endl;
            else
                if(win[i]+loss[i]) cout<<fixed<<setprecision(3)<<((float)win[i]/(float)(win[i]+loss[i]))<<endl;
                else cout<<fixed<<setprecision(3)<<(float)0<<endl;
        }
        cout<<endl;

    }



}
