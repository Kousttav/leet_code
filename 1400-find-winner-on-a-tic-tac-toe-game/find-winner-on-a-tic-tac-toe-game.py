class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [["", "", ""] for _ in range(3)]
        idx=1
        for i,j in moves:
            print(i,j)
            if idx%2!=0:
                grid[i][j]="X"
            elif idx%2==0:
                grid[i][j]="O"
            idx+=1
            print(grid)
        if (
        (grid[0][0] != "" and grid[0][0] == grid[1][1] == grid[2][2]=="X") or
        (grid[2][0] != "" and grid[2][0] == grid[1][1] == grid[0][2]=="X") or
        (grid[0][0] != "" and grid[0][0] == grid[0][1] == grid[0][2]=="X") or
        (grid[1][0] != "" and grid[1][0] == grid[1][1] == grid[1][2]=="X") or
        (grid[2][0] != "" and grid[2][0] == grid[2][1] == grid[2][2]=="X") or
        (grid[0][0] != "" and grid[0][0] == grid[1][0] == grid[2][0]=="X") or
        (grid[0][1] != "" and grid[0][1] == grid[1][1] == grid[2][1]=="X") or
        (grid[0][2] != "" and grid[0][2] == grid[1][2] == grid[2][2]=="X")
        ):
            return "A"
        elif (
        (grid[0][0] != "" and grid[0][0] == grid[1][1] == grid[2][2] == "O") or
        (grid[2][0] != "" and grid[2][0] == grid[1][1] == grid[0][2] == "O") or
        (grid[0][0] != "" and grid[0][0] == grid[0][1] == grid[0][2] == "O") or
        (grid[1][0] != "" and grid[1][0] == grid[1][1] == grid[1][2] == "O") or
        (grid[2][0] != "" and grid[2][0] == grid[2][1] == grid[2][2] == "O") or
        (grid[0][0] != "" and grid[0][0] == grid[1][0] == grid[2][0] == "O") or
        (grid[0][1] != "" and grid[0][1] == grid[1][1] == grid[2][1] == "O") or
        (grid[0][2] != "" and grid[0][2] == grid[1][2] == grid[2][2] == "O")
        ):
            return "B"

        if len(moves) == 9:
            return "Draw"

        return "Pending"
    
        