class Solution:
    def maxScore(self, s):
        score = 0

        for i in range(1,len(s)):
            # split the string at a different index during each iteration
            left = s[:i] # numbers to the left of i
            right = s[i:] # numbers to the right of i

            if left.count("0") + right.count("1") > score: #count the number of 0's in left string and number of 1's in right string compare to curr score
                score = left.count("0") + right.count("1") # if greater than score, set new score

        return score
    

    # second attempt from scratch 12/22/23 same general process, use max() method instead of if statement to find if there is a new highest score
    def maxScoreTwo(self, s):
        max_score = 0

        for i in range(1, len(s)):
            left = s[:i]
            right =s[i:]
            max_score = max(max_score, left.count("0") + right.count("1"))
        
        return max_score