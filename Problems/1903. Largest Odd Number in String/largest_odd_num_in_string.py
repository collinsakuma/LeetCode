class Solution:

    # first solution exceeds linigt for integer string conversion otherwise words except for super large numbers over 4300 characters
    def largestOddNumber(self, num):
        n = len(num)

        while n != 0: # while n does not equal 0 continue loop
            if int(num[:n]) % 2 != 0: # first loop will take entire num while each loop will remove the last number off num 
                return (num[:n])
            n -= 1 # reduce n by 1 next loop will loop at len(num) - 1
        return ""
    
    def largestOddNumberTwo(self, num):
        for i in range(len(num) - 1, -1, -1): # loop though range of len(num) backwards
            if num[i] in {'1', '3', '5', '7', '9'}: # if num in dictionary of odd numbers
                return num[:i + 1] # return number up to i + 1
        return "" 
    
    # third solution using a array instead of a dictionary
    def largestOddNumber(self, num: str) -> str:
        odds = ["1", "3", "5", "7", "9"]
        for i in range(len(num) - 1, -1, -1):
            if num[i] in odds:
                return num[:i + 1]
        return ""