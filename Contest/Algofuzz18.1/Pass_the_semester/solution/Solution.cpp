#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
vector<pair<ll,ll> > :: iterator it;

ll bf(  vector<pair<ll,ll> > *my,ll arr[],ll value,ll arr2[])
{
stack<ll> ym;
ym.push(value);
while(!ym.empty())
{
ll pp = ym.top();ym.pop();
arr2[pp]=1;
for(it = my[pp].begin();it!=my[pp].end();it++)
{
    if(arr2[(*it).first]==0)
    {
        ym.push((*it).first);
        arr2[(*it).first] =1;
        arr[(*it).first] = arr[pp] + (*it).second;
    }
}
}
}

int main()
{
    ll a,b,c,d,e,f,g,h,i;
    cin>>a;
    for(b=0;b<a;b++)
    {
        cin>>c;
        ll arr[c+1],arr2[c+1];
        memset(arr,0,sizeof(arr));
        memset(arr2,0,sizeof(arr2));
        vector<pair<ll,ll> > my[c+1];
        for(d=0;d<c-1;d++)
        {
            cin>>e>>f>>g;
            //cout<<e<<f<<g<<" "<<c<<" "<<d<<"\n";
            my[e].push_back(make_pair(f,g));
            my[f].push_back(make_pair(e,g));
        }
        i=1;
        bf(my,arr,i,arr2);
        ll oo=0,ii=0;
        for(i=1;i<=c;i++)
        {
            if(arr[i]>oo)
            {
                oo = arr[i];ii=i;
            }
        }
        //cout<<ii<<"\n";
        memset(arr,0,sizeof(arr));
        memset(arr2,0,sizeof(arr2));
        bf(my,arr,ii,arr2);
        for(i=1;i<=c;i++)
        {
           // cout<<i<<" "<<arr[i]<<"\n";
            oo = max(oo,arr[i]);
        }
        cout<<oo<<"\n";}}
