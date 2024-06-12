def orangesRotting(grid) -> int:
        Q = []
        f = 0
        n,m = len(grid),len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    Q.append((i,j))
                elif grid[i][j] == 1:
                    f += 1
        level = 0
        while Q and f > 0:
            n1 = len(Q)
            for i in range(n1):
                c0,c1 = Q.pop(0)
                for r,c in [[0,1],[1,0],[-1,0],[0,-1]]:
                    r,c = (c0+r,c1+c)
                    if 0 <= r < n and 0 <= c < m and grid[r][c] == 1:
                        Q.append((r,c))
                        grid[r][c] = 2
                        f -= 1
            level += 1
        return level if f == 0 else -1
print(orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))