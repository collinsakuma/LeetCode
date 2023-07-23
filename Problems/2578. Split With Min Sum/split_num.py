class Solution:
    def splitNum(self, num):
        s = "".join(sorted(str(num)))
        return int(s[::2]) + int(s[1::2])