class Solution:
    def countFairPairs(self, nums, lower, upper):
        # count the number of pairs that are less than a certain value
        def count(n):
            output, j = 0, len(nums) - 1
            for i in range(len(nums)):
                while i < j and nums[i] + nums[j] > n:
                    j -= 1
                output += max(0, j - i)

            return output
        
        nums.sort()

        return count(upper) - count(lower - 1)
    
    ### Solution works on shorter list of nums, TLE encountered once nums increases in length
    ### nested for loops not optimal for runtime (Duhhhh)
    def countFairPairsTLE1(self, nums, lower, upper):
        nums.sort()
        output = 0

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if lower <= (nums[i] + nums[j]) <= upper:
                    output += 1

        return output    

    def countFairPairsTwo(self, nums, lower, upper):
        nums.sort()
        output = 0

        low = high = len(nums) - 1

        for index, num in enumerate(nums):
            # increment the upper bound down until num + nums[high] goes lower than upper bound
            while 0 <= high and num + nums[high] > upper:
                # incrment high down with each loop
                high -= 1
            # increment low down until num + nums[low] is less than the lower limit
            while 0 <= low and num + nums[low] >= lower:
                # increment low down
                low -= 1
            
            output += high - low # add the number of fair pairs

            if low < index <= high: # remove duplace pair (low, low) if in pairs
                output -= 1

        return output // 2 