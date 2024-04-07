class Solution:
    def checkValidString(self, s):
        # track left parentheses occurances and star occurances 
        stack_parentheses = []
        stack_star = []


        for i, char in enumerate(s):
            # if character a left parentheses append its index to stack
            if char == '(':
                stack_parentheses.append(i)
            # if character is a closing parentheses
            elif char == ')':
                # if there are opening parentheses pop one from the stack to pair 
                if stack_parentheses:
                    stack_parentheses.pop()
                # if there are no parentheses check for star and if there are stars, use one to close the parentheses
                elif stack_star:
                    stack_star.pop()
                # unable to close the parentheses return False
                else:
                    return False
                
            else:
                stack_star.append(i)

        while stack_parentheses and stack_star:
            # if parentheses is uncloseable return False
            if stack_parentheses[-1] > stack_star[-1]:
                return False

            # pair off the parentheses and stars untill none are left or condition fails
            stack_parentheses.pop()
            stack_star.pop()