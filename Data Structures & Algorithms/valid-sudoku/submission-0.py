class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows=[set() for _ in  range(9) ]
        cols=[set() for _ in  range(9) ]
        boxes=[set() for _ in  range(9) ]

        for r in range(9):
            for c in range(9):
                cell=board[r][c]

                if cell == ".":
                    continue
                

                boxindex=3*(r//3)+(c//3)

                if cell in rows[r] or cell in cols[c] or cell in boxes[boxindex]:
                    return False

                rows[r].add(cell)
                cols[c].add(cell)
                boxes[boxindex].add(cell)

        return True

        