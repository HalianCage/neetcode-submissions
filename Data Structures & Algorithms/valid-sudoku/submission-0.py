class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        box = defaultdict(set)
        row = defaultdict(set)
        col = defaultdict(set)
        
        for i, brdRow in enumerate(board):
            for j, ele in enumerate(brdRow):

                if ele == '.':
                    continue

                temp = str(i//3) + str(j//3)

                if ele in row[i] or ele in col[j] or ele in box[temp]:
                    return False
                
                row[i].add(ele)
                col[j].add(ele)
                box[temp].add(ele)


        return True