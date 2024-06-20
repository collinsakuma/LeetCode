class Solution:
    def minDays(self, bloomDay, m, k):
        if len(bloomDay) < m * k:
            return -1
        
        low, high = 0, max(bloomDay)

        while low < high:
            mid = low + high >> 1
            bouquet = flower = 0
            for i in bloomDay:
                if i <= mid:
                    flower += 1
                else:
                    flower = 0
                if flower == k:
                    flower = 0
                    bouquet += 1
            if bouquet >= m:
                high = mid
            else:
                low = mid + 1
        return low