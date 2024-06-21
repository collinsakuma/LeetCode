class Solution:
    def maxDistance(self, position, m):
        position.sort()

        def is_possible(d):
            ans, prev = 0, -inf
            for i in position:
                if i - prev >= d:
                    ans += 1
                    if ans == m:
                        return True
                    prev = i
            return False

        low, high = 1, position[-1] - position[0]
        while low < high:
            mid = low + high + 1 >> 1
            if is_possible(mid):
                low = mid
            else:
                high = mid - 1
        
        return low