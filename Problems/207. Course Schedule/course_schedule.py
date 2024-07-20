class Solution:
    def canFinish(self, numCourses, prerequisites):
        # create an adjacent 2D graph that represents the courses
        adj = [[] for _ in range(numCourses)]