class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:

        G = defaultdict(list)
        dist = [inf] * N
        visited = [False] * N
        h = [(0,0)]
        heapq.heapify(h)
        ans = 0
        for src,des,dis in edges:
            G[src].append((des,dis+1))
            G[des].append((src,dis+1))
        
        def shortest_path():
            nonlocal ans
            while h:
                dis,src = heapq.heappop(h)
                if not visited[src]:
                    visited[src] = True
                    dist[src] = dis
                    if dist[src]<=M: ans+=1 
                    for des,wgt in G[src]:
                        if not visited[des]: 
                            heapq.heappush(h,(wgt+dis,des))
            
        shortest_path()
        
        for i, j, w in edges:
            w1, w2 = M - dist[i], M - dist[j]
            ans += (max(0, w1) + max(0, w2))
            if w1 >= 0 and w2 >= 0: ans -= max(w1 + w2 - w, 0)
        
        return ans