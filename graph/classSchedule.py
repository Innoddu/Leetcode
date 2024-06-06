def canFinish(numCourses, prerequisites):

        hashmap = {i: [] for i in range(numCourses) }

        def dfs(course):
            if course in visited:
                return False
            if hashmap[course] == []:
                return True
            visited.add(course)
            print("course", course)
            for pre in hashmap[course]:
                if not dfs(pre):
                    return False
            
            visited.remove(course)
            hashmap[course].pop(0)

            return True

        for want, pre in prerequisites:
                hashmap[want].append(pre)
   
        visited = set() 

        for course in range(numCourses):
            if not dfs(course):
                return False
