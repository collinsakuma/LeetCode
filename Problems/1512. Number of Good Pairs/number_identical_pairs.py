class Solution:
    def numIdenticalPairs(self, nums):
        pairs = 0 # count the number of valid pairs found

        for i in range(len(nums) - 1): # loop though range of length nums
            # second loop for a list of nums at i to end of nums
            for j in nums[i + 1:]:
                # if num at i is the same as j then a valid pair has been found increment pairs
                if nums[i] == j:
                    pairs += 1
        return pairs # return number of pairs found
    

    def numIdenticalPairsTwo(self, nums):
        pairs = 0 # count of number of valid pairs

        for num in set(nums): # loop though a list of unique numbers in nums
            count = nums.count(num) # count how many time each number is in nums
            pairs += count * (count - 1) // 2
        
        return pairs