#include <bits/stdc++.h>

using namespace std;

long long findDigits(int n) {
	if (n < 0) 
		return 0;  
	if (n <= 1) 
		return 1; 
	double x = ((n * log10(n / M_E) + 
				log10(2 * M_PI * n) / 
				2.0)); 

	return floor(x) + 1; 
} 

int len(double x)
{

	string s=to_string(x);
	return s.length();
}

int main()
{
	map<int,int> f
	{
		{1 ,1},
		{2,2},
		{6,3},
		{24,4},
		{120,5},
		{720,6},
	};



	
	string x;
	cin>>x;
	if(x=="1")cout<<1<<endl;
	else if (x=="2")cout<<2<<endl;
	else if (x=="6")cout<<3<<endl;
	else if (x=="24")cout<<4<<endl;
	else if (x=="120")cout<<5<<endl;
	else if (x=="720")cout<<6<<endl;
	else
	{
		int l = x.length();
		// cout<<l<<endl;
		for(int i=6;i<205050;i++)
		{
			if((long long)l==findDigits(i))
			{
				cout<<i<<endl;
				return 0;
			}
		}
	}


// len(str(x))==int(find_dig(m))+1:
          


}