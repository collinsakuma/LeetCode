class Solution:
    def bagOfTokensScore(self, tokens, power):
        
        tokens.sort() # sort the list of tokens
        # set intial values for score, max_score, and first of two pointers to 0
        score = max_score = left = 0
        # set right pointer to the length of tokens array
        right = len(tokens) - 1 

        # traverse through two pointers
        while left <= right:
            # if power is greater than the lowest token, use that token 
            if power >= tokens[left]:
                power -= tokens[left] # subtract token value from power
                score += 1 # increase score by 1
                left += 1 # increment left token by 1
                max_score = max(max_score, score) # set a new max score
            elif score > 0: # if score is greater than 0
                # incrase the power by the greatest valued token 
                power += tokens[right] # increase power by right token ( highest token value available )
                score -= 1 # decrease score by 1
                right -= 1 # increment right pointer
            else:
                break # if no operations can be performed break from the loop
        
        return max_score