#include<bits/stdc++.h>
using namespace std;

vector< pair<int, int> > v;

int main()
{
	int n,idx=0,c=0;
	cin>>n;
	int arr[n+1];
	for(int i = 0; i < n; i++)
	{
		cin>>arr[i];
	}
	arr[n]=1000000;
	sort(arr,arr+n);
	int first,second;
	v.push_back(make_pair(arr[idx],0));
	while(idx<n)
	{
		if(arr[idx+1]-1 == arr[idx])
		{
			v[c].second=arr[idx+1];
			idx++;
		}
		else
		{
			c++;
			v.push_back(make_pair(arr[idx+1] , 0 ));
			idx++;
		}
	}
	for(int i = 0; i < v.size(); i++)
	{
		if(v[i].first ==1000000 || v[i].second==1000000)
		{
			continue;
		}
		else if(v[i].second - v[i].first ==1)
		{
			cout<<v[i].first<<" "<<v[i].second<<" ";
			continue;
			
		}
		cout<<v[i].first;
		if(v[i].second != 0 && v[i].second - v[i].first !=1)
		{
			cout<<"-"<<v[i].second<<" ";
		}

		else
		{
			cout<<" ";
		}
	}

}