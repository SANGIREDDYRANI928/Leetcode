class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        
        for i in range(len(asteroids)):
            while stack and asteroids[i] < 0 and stack[-1] > 0:
                
                if stack[-1] < abs(asteroids[i]):
                    stack.pop()
                    continue
                
                elif stack[-1] == abs(asteroids[i]):
                    stack.pop()
                    break
                
                else:
                    break
            
            else:
                stack.append(asteroids[i])
        
        return stack