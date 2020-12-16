#include <bits/stdc++.h>
using namespace std;
int maximum = 0;

void fun(vector<int> adj[], int sr, int gone[], int dip[], int l)
{

    gone[sr] = 1;

    cout << "Explored  " << sr << " at depth " << dip[sr] << endl;

    maximum = max(maximum, dip[sr]);

    for (int i : adj[sr])
    {
        if (gone[i] == 0)
        {

            dip[i] = dip[sr] + 1;

            if (dip[i] > l)
            {
                continue;
            }

            else
                fun(adj, i, gone, dip, l);
        }
    }
}

int main()
{

    freopen("input.txt", "r", stdin);

    int n, v, a, b, source, l = 0, dest;

    cin >> n >> v;
    vector<int> adj[n];

    while (v--)
    {
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    cin >> source;
    while (l < 10)
    {
        int vis[10000] = {0};

        int dip[10000] = {0};
        cout << "When depth limit: " << l << endl
             << endl;
        fun(adj, source, vis, dip, l);
        l++;
    }
}