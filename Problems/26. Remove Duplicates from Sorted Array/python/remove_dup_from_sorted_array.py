class Solution:
    def removeDuplicates(self, nums):
        nums[:] = sorted(set(nums))
        # 1. set(nums) creates an unordered list of unique elements from the nums list.
        # 2. sorted(set(nums)) sorts the list returned from the first set and orders them. 
        # 3. nums[:] = sorted(set(nums)) modifies the list in place instead of creating a new list.
        return len(nums)
    
    def removeDuplicatesTwoPointer(self, nums):
        slow, fast = 0, 1  # short hand for writing slow = 0, fast = 1
        while fast in range(len(nums)):
            if nums[slow] == nums[fast]:
            # - in the first time through the loop it checks if nums[0] is equal to nums[1] if they are equal(true)
            #   that means that nums[1] is a duplicate of nums[0] and the fast variable is incremented by 1 to check
            #   the next index. 
                fast += 1
            else:
            # if the values of nums[slow] and nums[fast] are not equal, the element at nums[slow +1] is set to the value of the 
            # newly found element at nums[fast]
            # Example:
                # if nums = [1,1,2] and slow = 0, fast = 2
                # nums[0] != nums[2]
                # so nums[0 + 1] is set to 2
                nums[slow + 1] = nums[fast]
                fast += 1
                slow += 1
                # fast and slow are both incremented by 1 to move on and check the next element in the list. 

        return slow + 1
        # slow represents the last no duplicate number in the list, 1 is added to find the length of the 
        # list becuase the starting index is 0. 