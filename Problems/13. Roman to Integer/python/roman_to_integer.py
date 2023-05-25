class Solution:
    def romanToInt(self, s):
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        answer = 0
        for i in range(len(s)-1):
            if symbols[s[i]] < symbols[s[i+1]]:
                answer = answer - symbols[s[i]]
            else: 
                answer = answer + symbols[s[i]]
        return answer + symbols[s[-1]]