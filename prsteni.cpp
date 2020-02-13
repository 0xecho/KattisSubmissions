#include <bits/stdc++.h>

using namespace std;

void reduce_fraction (int &numerator, int &denominator)
{
        for (int i = denominator * numerator; i > 1; i--) {  
                if ((denominator % i == 0) && (numerator % i == 0)) {  
            denominator /= i;  
                numerator /= i;  
        }  
                  
         }
}

int main(){

    int T,temp;
    cin>>T;

    vector<int> v;

    for(int i=0;i<T;i++)
    {
        cin>>temp;

        v.emplace_back(temp);
    }

    for(int i=1;i<T;i++)
    {
        int n = v[0];
        int d = v[i];
        reduce_fraction(n,d);
        cout<<n<<"/"<<d<<endl;
    }

    return 0;
}