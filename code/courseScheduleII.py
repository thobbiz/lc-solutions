from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)

        output = []
        visitSet, cycleSet = set(), set()

        def dfs(course):
            if course in cycleSet:
                return False
            if course in visitSet:
                return True

            cycleSet.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False

            cycleSet.remove(course)
            visitSet.add(course)
            output.append(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return output
