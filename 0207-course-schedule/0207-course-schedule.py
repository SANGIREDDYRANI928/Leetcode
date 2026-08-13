from collections import deque
class Solution:
    def canFinish(self, numCourses, prerequisites):
        queue=deque()
        graph=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses
        for course,pre in prerequisites:
            graph[pre].append(course)
            indegree[course]+=1
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        c=0
        while queue:
            course=queue.popleft()
            c+=1
            for neigh in graph[course]:
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    queue.append(neigh)
        return c==numCourses


        