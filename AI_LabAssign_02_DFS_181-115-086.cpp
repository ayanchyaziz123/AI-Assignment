#include <bits/stdc++.h>
#define ll long long int
#define INF 2e18
using namespace std;

vector<ll> graph[100000];
vector<ll> mx;

void dfs(ll node, ll parn, ll height[], ll vis[])
{
  if (node != parn)
  {
    height[node] = 1 + height[parn];
    parn = node;
    cout << "Explored " << node << " at depth " << height[node] << endl;
    ll c = height[node];
    mx.push_back(c);
  }
  vis[node] = 1;

  for (ll i = 0; i < graph[node].size(); i++)
  {
    ll child = graph[node][i];
    if (vis[child] == -1)
    {
      dfs(child, parn, height, vis);
    }
  }
}

int main()
{
#ifndef ONLINE_JUDGE
  //freopen("input.txt", "r", stdin);
  //freopen("output.txt", "w", stdout);
#endif
  ll v, e;
  cin >> v >> e;
  ll height[v + 1];
  ll vis[v + 1];
  memset(vis, -1, sizeof(vis));
  memset(height, -1, sizeof(height));
  for (ll i = 0; i < e; i++)
  {
    ll node1, node2;
    cin >> node1 >> node2;
    graph[node1].push_back(node2);
    graph[node2].push_back(node1);
  }
  ll source;
  cin >> source;
  height[source] = 0;
  cout << "Explored " << source << " at depth " << height[source];
  mx.push_back(height[source]);
  cout << endl;
  dfs(source, source, height, vis);
  cout << endl;
  cout << "Maximum Depth reached: " << *max_element(mx.begin(), mx.end()) << endl;
  return 0;
}