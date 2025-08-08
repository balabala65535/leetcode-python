def numIslands(grid):
    def is_island(grid, x, y):
        having_water = 0
        x_length = len(grid) - 1
        y_length = len(grid[0]) - 1
        # 左
        if x - 1 < 0 or grid[x - 1][y] == 0:
            having_water += 1
        # 右
        if x + 1 > x_length or grid[x + 1][y] == 0:
            having_water += 1

        # 上
        if y - 1 < 0 or grid[x][y - 1] == 0:
            having_water += 1
        # 下
        if y + 1 > y_length or grid[x][y + 1] == 0:
            having_water += 1

        if having_water >= 3:
            return True
        else:
            return False

    for x in grid:
        for y in x:
            ...


class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m * n)
        print(self.parent)
        print(grid)
        self.rank = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent[i * n + j] = i * n + j
                    self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]:
                rootx, rooty = rooty, rootx
            self.parent[rooty] = rootx
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1
            self.count -= 1

    def getCount(self):
        return self.count


class Solution:
    def dfs(self, grid, r, c):
        print("==="*3)
        grid[r][c] = 0  # 每个搜索到的 1 都会被重新标记为 0，最终岛屿的数量就是我们进行深度优先搜索的次数。
        nr, nc = len(grid), len(grid[0])
        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            # 看它四周有没有陆地，有就给变为0，表示已经扫完了，直到扫来没有为止。
            # for i in grid:
            #     print(i)
            # print('***'*3)
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                self.dfs(grid, x, y)

    def numIslands(self, grid) -> int:
        """
        深度优先搜索
        :param grid:
        :return:
        """
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    self.dfs(grid, r, c)
            print(grid)
        return num_islands


    def numIslands_1(self, grid) -> int:
        """
        方法二：广度优先搜索
        """
        import collections
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    grid[r][c] = "0"
                    neighbors = collections.deque([(r, c)])
                    while neighbors:
                        row, col = neighbors.popleft()
                        for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                                neighbors.append((x, y))
                                grid[x][y] = "0"

        return num_islands

    def numIslands_3(self, grid) -> int:
        """
        方法三：并查集
        :param grid:
        :return:
        """
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        uf = UnionFind(grid)
        num_islands = 0
        for r in range(nr):
            print(uf.parent)
            for c in range(nc):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    print('==>', [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)])
                    for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                        if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                            uf.union(r * nc + c, x * nc + y)

        return uf.getCount()


if __name__ == "__main__":
    # grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    # resp = numIslands(grid)

    resp = Solution().numIslands_3(grid)
    print(resp)
