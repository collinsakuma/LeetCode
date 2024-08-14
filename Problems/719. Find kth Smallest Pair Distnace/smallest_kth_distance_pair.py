class Solution:
    def smallestDistancePair(self, nums, k):
        nums.sort() # sor the list of numbers
        # find the minimum distance and maximum distance between two pairs possible
        min_distance, max_distnace = 0, nums[-1] -  nums[0]

        # while minimum and maximum distances are different
        while min_distance < max_distnace:
            # find the distnace between the two
            mid_distance = min_distance + (max_distnace - min_distance) // 2
            # set two pointer and count of pairs before the mid distance
            left, count = 0, 0

            # loop the right pointer
            for right in range(len(nums)):
                # is the distance between pairs are less than the current mid disstance 
                while nums[right] - nums[left] > mid_distance:
                    # move pointer further left
                    left += 1
                # find the count of pairs with a distance less than the mid distance
                count += right - left

            # if the count is less than k than the Kth furthest pair comes
            # after the mid distance point set a new minimum distnace
            if count < k:
                min_distance = mid_distance + 1
            # if the count is greater than Kth furthest pair then mid distance is too great
            # set a new max distance 
            else:
                max_distnace = mid_distance

        return min_distance