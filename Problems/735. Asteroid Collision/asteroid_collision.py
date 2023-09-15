class Solution:
    def asteroidCollision(self, asteroids):
        stack = []

        for a in asteroids:
            while stack and stack[-1] > 0 > a:
                if stack[-1] < abs(a):
                    stack.pop()
                    continue
                elif stack[-1] == abs(a):
                    stack.pop()
                break
            else:
                stack.append(a)
        return stack
    
    def asteroidCollisionTwo(self, asteroids):
        output = [] # set list to stack and pop asteroids in and out of

        for i in asteroids: # loop through asteroids
            # check several conditions 
            # 1. output list exist and is not empty
            # 2. the last element in output is greater than 0
            # 3. the current i in the loop is less than 0 ( negative number ) 
            while output and output[-1] > 0 and i < 0:
                if output[-1] + i < 0:
                    # if ouput[-1] and i combined is negative then the two asteroids have collided and i is bigger than output[-1]
                    output.pop() # pop the last asteroid from output
                elif output[-1] + i > 0:
                    # if output[-1] and i combined is greater than 0 then output[-1] was larger than i, do not modify output
                    break
                else:
                    output.pop()
                    break
            else:
                # if output is empty, the current last element is negative, or i is positive
                output.append(i) # append i to output
        return output