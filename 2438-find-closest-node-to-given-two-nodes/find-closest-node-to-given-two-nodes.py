class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n=len(edges)
        def dfs(edges,node,dist,visited):
            visited[node]=True
            v=edges[node]
            if(v!=-1 and not visited[v]):
                visited[v]=True
                dist[v]=1+dist[node]
                dfs(edges,v,dist,visited)
            return
        visited1=[False]*n
        visited2=[False]*n
        dist1=[float('inf')]*n
        dist2=[float('inf')]*n
        dist1[node1]=0
        dist2[node2]=0
        dfs(edges,node1,dist1,visited1)
        dfs(edges,node2,dist2,visited2)

        mindistnode=-1
        mindistnow=float('inf')
        for i in range(n):
            mx=max(dist1[i],dist2[i])
            if(mindistnow>mx):
                mindistnow=mx
                mindistnode=i
        return mindistnode