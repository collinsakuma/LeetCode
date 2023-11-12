class Solution:
    def sumZero(self, n):
        length, rem = n // 2, n % 2

        if rem != 0: 
            ans = [0]
        else:
            ans = []

        for i in range(1, length + 1):
            ans.append(-i)
            ans.append(i)
        return ans