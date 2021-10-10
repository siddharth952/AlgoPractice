class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i: [] for i in range(numCourses)} # Map to empty list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        
        # visitSet  -> all the courses along the curr DFS path
        
        visitSet = set()
        
        def dfs(crs):
            # Base
            if crs in visitSet:
                # Detected a loop
                return False
            
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False # if anyone cannot be completed
            # So can be taken
            # No logner visit
            visitSet.remove(crs)
            preMap[crs] = [] # To not repeat the work
            return True
        
        # Call for all, for disjoint sets
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
        