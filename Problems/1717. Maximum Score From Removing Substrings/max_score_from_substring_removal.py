class Solution:
    def maximumGain(self, s, x, y):
        # helper function to remove the substring ( "ab" or "ba") that rewards the most points first
        def remove_substring(s, first, second, points):
            # initalize a stack and track points 
            stack = []
            score = 0

            # looop through characters in the string
            for ch in s:
                # if there is currently letters in the stack and the list letter in the stack 
                # and the current letter being iterator over match the letters of the substring being
                # searched for
                if stack and stack[-1] == first and ch == second:
                    # pop the last letter out of the stack and increment the score
                    stack.pop()
                    score += points
                else:
                    # if a substring is not found add the character to the end of the stack
                    stack.append(ch)
            # return a string of the remaining letters in the string and the score achieved
            return ''.join(stack), score
        
        # remove the substring that is more profitable first
        if x > y:
            s, score1 = remove_substring(s, 'a', 'b', x)
            s, score2 = remove_substring(s, 'b', 'a', y)
        else:
            s, score1 = remove_substring(s, 'b', 'a', y)
            s, score2 = remove_substring(s, 'a', 'b', x)
    
        # returned the combined score after both substrings are searched for and removed
        return score1 + score2