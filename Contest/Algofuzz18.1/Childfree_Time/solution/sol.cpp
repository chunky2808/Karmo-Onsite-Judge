#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define endl "\n"
#define X first
#define Y second
bool visit[1000001];
long long n,m,k;
vector<long long> vec[1000001];
vector<pair<long long,long long> > vec1[1000001];
long long c[1000001];
long long d[1000005];
long long result;
void dfs(long long index)
{
	long long g=0;
	for(long long i=0;i<vec1[index].size();i++)
	{
		if(c[vec1[index][i].first]==-1)
		{
			dfs(vec1[index][i].first);
			
			//cout<<vec1[index][i].first<<" "<<index<<" "<<vec1[index][i].second<<endl;
		}
		g=max(g,c[vec1[index][i].first]+vec1[index][i].second);
	}
	c[index]=g;
	result=max(result,g);
	//cout<<g<<endl;
}
int main()
{
	ios_base::sync_with_stdio(false);
  	cin.tie(NULL);
  	cout.tie(NULL);
 
  	cin>>n>>m;
  	for (long long i = 0; i < m; ++i)
  	{
  		long long u,v,t;
  		cin>>u>>v>>t;
  		vec1[u].pb(mp(v,t+2));
  		//vec1[v].pb(mp(u,t));
  	}
  	memset(visit,false,sizeof(visit));
  	memset(c,-1,sizeof(c));
  	result=0;
  	for(long long i=1;i<=n;i++)
  	{
  		if(!visit[i])
  		{
  			dfs(i);
  		}
  	}
  	cout<<result<<endl;
	return 0;
}
