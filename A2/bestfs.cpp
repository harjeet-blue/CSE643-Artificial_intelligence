#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> pii;

vector<vector<pii>> graph;
vector<int> heuristic = {1, 8, 6, 2, 7, 3, 2, 0, 9, 11, 13, 4};

void addEdge(int u, int v, int cost){
    graph[u].push_back({v, cost});
}

void bestFirstSearch(int start, int goal){

    priority_queue<pii, vector<pii>, greater<pii>> pq;

    vector<bool> visited(graph.size(), false);
    vector<int> parent(graph.size(), -1);
    vector<int> cost(graph.size(), INT_MAX);

    cost[start] = 0;
    pq.push({0, start});

    while(!pq.empty()){
        
        int u = pq.top().second;
        pq.pop();

        if(u == goal){
            cout << "Goal found \nwith cost : " << cost[u] << endl;
            cout << "Path: ";

            while(u != -1){
                cout << u << " ";
                u = parent[u];
                cout<<"<-";
            }

            return;
        }

        if(visited[u]) continue;
        visited[u] = true;

        for(auto v : graph[u]){

            if(!visited[v.first]){

                if(cost[v.first] > cost[u] + v.second){
                    cost[v.first] = cost[u] + v.second;
                    parent[v.first] = u;
                }

                pq.push({ heuristic[v.first], v.first});
            }
        }
    }

    cout << "Goal not found" << endl;
}


int main(){

    graph.resize(12);

    addEdge(0, 1, 4);
    addEdge(0, 2, 18);
    addEdge(0, 3, 11);

    addEdge(1, 2, 8);
    addEdge(1, 4, 5);

    addEdge(3, 4, 13);
    addEdge(3, 5, 20);
    addEdge(3, 6, 2);

    addEdge(4, 6, 1);
    addEdge(4, 8, 1);
    addEdge(4, 9, 20);

    addEdge(5, 7, 19);
    addEdge(6, 7, 13);

    addEdge(8, 9, 1);
    addEdge(8, 10, 2);

    addEdge(9, 7, 3);
    addEdge(9, 10, 5);
    addEdge(9, 11, 13);

    addEdge(10, 11, 7);
    addEdge(11, 7, 6);

    bestFirstSearch(0, 7);

    return 0;
}