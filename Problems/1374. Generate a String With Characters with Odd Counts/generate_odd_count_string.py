class Solution:
    def generateTheString(self, n):
        answer = "" # string to generate answer
        if n % 2 == 0: # if n is even return a string with n-1 "a" plus one "b" will always be an odd count of letters
            answer = answer + ("a" * (n - 1) + "b")
        else: # if n is odd return a string with n number of "a" 
            answer += "a" * n
        
        return answer