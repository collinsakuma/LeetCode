from collections import defaultdict

class Solution:
    def maximumLength(self, s):
        n = len(s)
        map = defaultdict(list)
        l = 0

        while l < n:
            r = l
            while r < n and s[l] == s[r]:
                r += 1
            for i in range(r-l, max(0, r - l - 4), -1):
                map[s[l]].append(i)
            l = r
        output = -1

        for key in map:
            if len(map[key]) >= 3:
                output = max(output, sorted(map[key])[-3])
        return output
