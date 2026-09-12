from collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        graph=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses
        ans=[]
        for course,prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course]+=1
        queue=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        while queue:
            course=queue.popleft()
            ans.append(course)
            for i in graph[course]:
                indegree[i]-=1
                if indegree[i]==0:
                    queue.append(i)
        if len(ans)==numCourses:
            return ans
        else:
            return []

        
        