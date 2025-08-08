

def orangesRotting(grid) -> int:
    """
    深度优先：24% & 98%
    :param grid:
    :return:
    """
    rotting_time = -1
    x = len(grid)
    y = len(grid[0])
    while True:
        new_rotting = []
        no_rotting = 0
        for nl in range(x):
            for nc in range(y):
                if grid[nl][nc] == 2:
                    grid[nl][nc] = 0
                    # 有腐烂的，开始腐烂
                    for x1, y1 in [(nl - 1, nc), (nl + 1, nc), (nl, nc - 1), (nl, nc + 1)]:
                        if 0 <= x1 < x and 0 <= y1 < y and grid[x1][y1] == 1:
                            new_rotting.append((x1, y1))
                            no_rotting -= 1

                elif grid[nl][nc] == 1:
                    no_rotting += 1
        # 完成一次感染：
        if len(new_rotting) == 0:
            rotting_time += 1
            if no_rotting > 0:
                rotting_time = -1
            break
        else:
            rotting_time += 1
        # 执行感染：
        for x1, y1 in new_rotting:
            grid[x1][y1] = 2
    return rotting_time



def orangesRotting_2(grid) -> int:
    """
    多源广度优先搜索:24% & 75%
    :param grid:
    :return:
    """
    import collections
    R, C = len(grid), len(grid[0])
    # queue - all starting cells with rotting oranges
    queue = collections.deque()
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == 2:
                queue.append((r, c, 0))

    def neighbors(r, c) -> (int, int):
        for nr, nc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
            if 0 <= nr < R and 0 <= nc < C:
                yield nr, nc

    d = 0
    # queue 保存找到当前栏的橘子
    while queue:
        r, c, d = queue.popleft()
        for nr, nc in neighbors(r, c):
            if grid[nr][nc] == 1:
                grid[nr][nc] = 2  # 进行感染
                queue.append((nr, nc, d + 1))

    if any(1 in row for row in grid):
        return -1
    return d


def orangesRotting_3(grid) -> int:
    """
    多源广度优先搜索: 100% & 84%; 82%&5%
    :param grid:
    :return:
    """
    import collections
    R, C = len(grid), len(grid[0])
    # queue - all starting cells with rotting oranges
    queue = collections.deque()
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == 2:
                queue.append((r, c, 0))

    d = 0
    while queue:
        r, c, d = queue.popleft()
        print(r, c, d)

        for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            x1, y1 = r + dr, c + dc
            if 0 <= x1 < R and 0 <= y1 < C and grid[x1][y1] == 1:
                grid[x1][y1] = 2  # 进行感染
                queue.append((x1, y1, d + 1))
        # for x1, y1 in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
        #     if 0 <= x1 < R and 0 <= y1 < C and grid[x1][y1] == 1:
        #         grid[x1][y1] = 2  # 进行感染
        #         queue.append((x1, y1, d + 1))
    if any(1 in row for row in grid):
        return -1
    return d



if __name__ == "__main__":
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    # grid = [[2,1,1],[0,1,1],[1,0,1]]
    # grid = [[0, 2]]
    resp = orangesRotting_3(grid)
    print(resp)
