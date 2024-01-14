class Solution:
    def arithmeticTriplets(self, nums, diff):
        count = 0 # set count of triplets that meet conditions

        # nest three loops within eachother to check each possible set of indexes
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    # check if conditions are meet and triplet set is found
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        count += 1 # if aritmetic triples increase count

        return count 