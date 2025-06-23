from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict, deque
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        queue = deque()

        for course in range(numCourses):
            # 第一个入度为 0 的课程可以先学习
            if indegree[course] == 0:
                queue.append(course)

        count = 0

        while queue:
            left = queue.popleft()
            count += 1
            # 把后续课程的入度减 1，如果入度为 0 则入队
            for course in graph[left]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)

        return count == numCourses


if __name__ == "__main__":
    # Example usage:
    numCourses = 2
    prerequisites = [[1, 0]]
    solution = Solution()
    result = solution.canFinish(numCourses, prerequisites)
    print(result)  # Expected output: True (can finish all courses)
