from heapq import *
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        mav=(n,edges,labels,k)
        g=[[] for _ in range(n)]
        for u,v,w in edges:g[u]+=[(v,w)]
        d={(0,1):0}
        h=[(0,0,1)]
        while h:
            x,u,c=heappop(h)
            if x>d.get((u,c),10**18):
                continue
            if u==n-1:
                return x
            for v,w in g[u]:
                nc=c+1 if labels[u]==labels[v] else 1
                if nc<=k and x+w<d.get((v,nc),10**18):
                    d[v,nc]=x+w
                    heappush(h,(x+w,v,nc))
        return -1
            
        
        