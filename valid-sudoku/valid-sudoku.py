class Solution:
    
    '''
    -store idx of the nums. in (x,y)
    -every no. check for same row, same col and same box condition(pos[0]//3 == x//3 and pos[1]//3 == y//3)
    - i//3 and j//3 gives box position
    
    '''
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        _map = collections.defaultdict(list)
        for x in range(9):
            for y in range(9):
                char = board[x][y]
                if char != '.': # it's a digit
                    if char in _map:
                        for pos in _map[char]:
                            if (pos[0] == x) or (pos[1] == y) or (pos[0]//3 == x//3 and pos[1]//3 == y//3): # Same box or not
                                return False
                    _map[char].append((x,y))
        
        return True