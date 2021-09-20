class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # BFS
        
        
        def bfs():
            rows,cols = len(grid),len(grid[0])
            visited = set()
            dir_ = ( (0,1),(0,-1),(1,0),(-1,0) )
            maxArea = 0
            
            def traverse(i,j):
                area = 0
                q = deque([ (i,j) ])
                while(q):
                    cur_i,cur_j = q.popleft()
                    if (cur_i,cur_j) not in visited:
                        visited.add((cur_i,cur_j))
                        area += 1
                        
                        # Traverse neighbors
                        for direc in dir_:
                            next_i,next_j = cur_i + direc[0], cur_j + direc[1]
                            # Check edges & question condition
                            if(0<=next_i<rows and 0<=next_j<cols and grid[next_i][next_j] != 0):
                                q.append((next_i,next_j))
                        
                return area
        
            for i in range(rows):
                for j in range(cols):
                    if (grid[i][j] == 1 and grid[i][j] not in visited ):
                        larea = traverse(i,j)
                        maxArea = max(maxArea,larea)
            
            return maxArea
        
        return bfs()
        