class Solution:
    def isValid(self, s):
        front = "({["
        stack = []  # create an empty stack. 
        for char in s:
            if char in front:
            # for each character in list "s" check if any are ( , { , or [. If it does match add it to the stack. 
                stack.append(char)
            else:
                if not stack:
                    return False  # if the stack is empty return false. 
                elif char == ")" and stack[-1] == "(":
                    # if the character is a back character I.E. ), }, or ] it will check the last character in the string
                    # to see if it the corresponding symbol type "()", "{}", or "[]" and if it is it the last element in
                    # the string is deleted with the .pop() method. 
                    stack.pop()
                elif char == "}" and stack[-1] == "{":
                    stack.pop()
                elif char == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return False  
                    # if none of the condition are met then there is no corresponding matching symbol 
                    # meaning there is an invalid parentheses and it will return False. 
        return not stack
        # at the end if the stack is empty that means all parentheses conditions have been meet meaning its True. 