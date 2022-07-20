class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_lst = defaultdict(list)
        
        for dst,src in prerequisites:
            adj_lst[src].append(dst)
        # print(adj_lst)
        vis = {}
        for i in range(numCourses):
            if i not in vis:
                vis[i] = '0'
        # print(vis)
        cycle = False
        stack = []
        
        def dfs(vertex,vis):
            nonlocal cycle
            
            if cycle:
                return
            
            vis[vertex] = '1'
            for i in adj_lst[vertex]:
                print(i)
                if vis[i] == '0':
                    dfs(i,vis)
                elif vis[i] == '1':
                    cycle = True
            vis[vertex] = '2'
            stack.append(vertex)
                
        
        
        for i in range(numCourses):
            if vis[i] =='0':
                dfs(i,vis)
                
        if cycle:
            return False
        else:
            return True