class Solution:
    def isArraySpecial(self, nums, queries):
        n = len(nums)
        # create prefix sum
        prefix_sum = [0] * (n + 1)

        # loop through and create a prefix sum of non intersecting arrays
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1]
            if nums[i] % 2 == nums[i - 1] % 2:
                prefix_sum[i] += 1


        output = []

        # check if each query is a special array
        for x, y in queries:
            if x == y:
                output.append(True)
            else:
                if prefix_sum[y] - prefix_sum[x] > 0:
                    output.append(False)
                else:
                    output.append(True)

        return output
    
    def isArraySpecialTwo(self, nums, queries):
        # list of non repeating subarrays
        sub_arrays = []
        # queries output set to False by default
        output = [False for _ in range(len(queries))]
        curr = 0 # curr position in nums list

        # loop through index of nums (second of two pointers)
        for idx in range(1,len(nums)):
            # if parity is the same between the two adjacent elements 
            if nums[idx - 1] % 2 == nums[idx] % 2:
                # add to the non interesecting subarrays
                sub_arrays.append([curr, idx - 1])
                # set new starting point of next sub array
                curr = idx
        # add the last subarry to the list of non intersecting subarrays
        sub_arrays.append([curr, len(nums) - 1])


        # loop through queries
        for index, (x, y) in enumerate(queries):
            # check each subarray if the query is a special subarray
            for (i, j) in sub_arrays:
                if x >= i and y <= j:
                    # if special set that query to true
                    output[index] = True
                    break
        return output