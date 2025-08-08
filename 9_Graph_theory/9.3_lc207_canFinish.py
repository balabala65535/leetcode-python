from typing import *


def canFinish(numCourses, prerequisites) -> bool:
    # course_num = 0
    if len(prerequisites) == 0:
        return True
    independ_course = set()
    for i1, i2 in prerequisites:
        depend = f"{i1}<-{i2}"
        revert_depend = f"{i2}<-{i1}"
        if depend not in independ_course and revert_depend not in independ_course:
            independ_course.add(depend)
        else:
            independ_course.remove(revert_depend)

    return len(independ_course) * 2 <= numCourses


def canFinish_1(numCourses, prerequisites) -> bool:
    import collections
    edges = collections.defaultdict(list)
    visited = [0] * numCourses
    result = list()
    valid = True

    for info in prerequisites:
        edges[info[1]].append(info[0])

    def dfs(u: int):
        nonlocal valid
        visited[u] = 1
        for v in edges[u]:
            if visited[v] == 0:
                dfs(v)
                if not valid:
                    return
            elif visited[v] == 1:
                valid = False
                return
        visited[u] = 2
        result.append(u)

    for i in range(numCourses):
        if valid and not visited[i]:
            dfs(i)

    return valid


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict, deque
        # 选课问题其实本质是拓扑排序，每次处理入度为0（当前可选）的节点（队列处理）
        # 修改它修完后的其他课程变化（用邻接表记录）
        indegree = [0] * numCourses
        adj = defaultdict(list)  # key为当前课，value为它的后续课程,用列表存

        # 初始化入度和邻接表
        for cur, pre in prerequisites:
            indegree[cur] += 1
            adj[pre].append(cur)
        # 把入度为0的入队列
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        # 开始bfs：
        while q:
            # 当前批次要处理的课程个数
            lenth = len(q)
            for i in range(lenth):
                # 当前处理的课
                pre = q.popleft()
                numCourses -= 1
                # 遍历课程pre的邻接表：它的后续课程
                for cur in adj[pre]:
                    # 课程pre已经完成，入度减一
                    indegree[cur] -= 1
                    # 如果入度减到0，加入队列
                    if indegree[cur] == 0:
                        q.append(cur)
        return numCourses == 0


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        import collections
        edges = collections.defaultdict(list)
        visited = [0] * numCourses
        result = list()
        valid = True

        for info in prerequisites:
            edges[info[1]].append(info[0])  # 统计节点是哪些节点的入度

        def dfs(u: int):
            """
            统计每个课程，它的入度状态
            """
            nonlocal valid
            visited[u] = 1  # 该门课已修
            # 让它所有的下级依赖的课程都修完
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                elif visited[v] == 1:
                    valid = False
                    return
            # 功德圆满完全出厂完毕
            visited[u] = 2
            result.append(u)

        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)

        return valid


    def canFinish_1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        import collections
        edges = collections.defaultdict(list)
        indeg = [0] * numCourses

        for info in prerequisites:
            edges[info[1]].append(info[0])  # 统计节点是哪些节点的入度
            indeg[info[0]] += 1  # 它的完成依赖于前面多少节课，即它的先修课程的数量

        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])
        visited = 0

        while q:
            visited += 1
            u = q.popleft()
            for v in edges[u]:
                indeg[v] -= 1
                if indeg[v] == 0:  # 表示它的先修课程已经完成了
                    q.append(v)

        return visited == numCourses



if __name__ == "__main__":
    numCourses = 3
    prerequisites = [[1,0]]
    # prerequisites = []
    # prerequisites = [[1,0], [0, 1]]
    resp = canFinish(numCourses, prerequisites)
    print(resp)

