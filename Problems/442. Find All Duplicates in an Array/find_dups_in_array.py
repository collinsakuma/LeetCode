class Solution:

    # idea is to loop though list and for each number check if the number at that index is negative (meaning that it has been encounter before in the list and turned to a negative value)
    def findDuplicates(self, nums):
        answer = [] # empty list to add numbers that appear twice in the list
        for num in nums: # loop through list
            num = abs(num) # set num to the absolute value of num ( positive number )
            if nums[num - 1] < 0: # check if the value at nums[num - 1] is less than 0
                answer.append(num) # if value is negative append that number to answer
            else:
                nums[num - 1] = - nums[num - 1] # if value is not negative make the number at index num-1 negative
        return answer
    
    # original number that I came up with runs two slow time limit exceeded error
    def findDuplicatesTwo(self, nums):
        answer = []
        for num in set(nums):
            if nums.count(num) == 2:
                answer.append(num)
        return answer