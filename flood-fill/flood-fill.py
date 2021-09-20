class Solution:
    def floodFill(self, mat: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # BFS
        def bfs():
            # Empty or not
            #if not mat: return []
            
            rows,cols = len(mat),len(mat[0])
            visited = set()
            dir_ = ( (0,1),(0,-1),(1,0),(-1,0) )
            # Keep Track of the old cuz it would be changed in the mat
            old = mat[sr][sc]
            
            def traverse(i,j):
                q = deque( [(i,j)] )
                mat[i][j] = newColor
                while(q):
                    
                    cur_i,cur_j = q.popleft()
                    
                    if(cur_i,cur_j) not in visited :
                        visited.add( (cur_i,cur_j) )
                        # Traverse neighbors
                        for direc in dir_:
                            next_i,next_j = cur_i + direc[0] , cur_j + direc[1]
                            # Check for edges
                            if (0 <= next_i < rows and 0 <= next_j < cols and mat[next_i][next_j] == old):
                                
                                # Question Specific
                                mat[next_i][next_j] = newColor
                                # End
                                print(next_i,next_j)
                                q.append((next_i,next_j))
            
            # for i in range(rows):
            #     for j in range(cols):
            traverse(sr,sc)
        
        bfs()
        return mat