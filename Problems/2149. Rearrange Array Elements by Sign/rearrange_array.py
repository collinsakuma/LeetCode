class Solution:
    def rearrangeArray(self, nums):
        # set three lists, one to hold negative numbers, positive numbers, and the output list in the alternating pos, neg order
        neg, pos, output = [], [], []

        for num in nums: # loop though numbers in nums
            # sort th negative and positive numbers into the correct lists
            if num < 0: neg.append(num)
            else: pos.append(num)

        # loop through a range of length of a sub array
        for i in range(len(neg)):
            # first append a number from the pos list and then a number from the neg list
            output.append(pos[i])
            output.append(neg[i])

        return output # return the list in the correct alternating pattern
    
    def rearrangeArrayTwo(self, nums):
        n = len(nums) # set length of nums to variable n
        pos, neg = 0, 1 # set pos and neg pointers
        ans = [0] * n # set a answer array to the length of nums with place holder 0

        for i in range(n): # loop through range of  n
            # if the number at pos index is posivite replace the value at ans[pos] with the current i index of nums
            if nums[pos] > 0: 
                ans[pos] = nums[i]
                pos += 2 # increment pos by 2 becuase posivite number must be at every other index
            else: # else the number must be negative
                ans[neg] = nums[i] # replace ans[neg] with number at nums index i
                neg += 2 # increment neg pointer by 2

        return ans