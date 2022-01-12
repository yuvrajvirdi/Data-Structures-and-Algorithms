#include <iostream>
#include <limits.h>
#include <stdio.h>

// setting num of vertices in graph
#define V 9

int minDist(int dist[], bool set[]){
    int min = INT_MAX, min_index;
    for (int v = 0; v < V; v++)
        if (set[v] == false && dist[v] <= min)
            min = dist[v], min_index = v;
    return min_index;
}

void dijkstra(int graph[V][V], int origin){
    int dist[V];
    bool set[V];
    for (int i = 0; i < V; i++)
        dist[i] = INT_MAX, set[i] = false;
    dist[origin] = 0;
    for (int count = 0; count < V - 1; count++) {
        int u = minDist(dist, set);
        set[u] = true;
        for (int v = 0; v < V; v++)
            if (!set[v] && graph[u][v] && dist[u] != INT_MAX
                && dist[u] + graph[u][v] < dist[v])
                dist[v] = dist[u] + graph[u][v];
    }

}
