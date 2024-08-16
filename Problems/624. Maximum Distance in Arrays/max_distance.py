class Solution:
    def maxDistance(self, arrays):
        # set initial lowest and highetst values
        low, high = arrays[0][0], arrays[0][-1]
        max_distance = 0

        # remove the first array of distances
        arrays.pop(0)

        # loop through the remaining distance arrays
        for arr in arrays:
            # find the max distance between the previous lowest and highest distances
            # and the current arr's low and high points
            max_distance = max(max_distance, abs(high - arr[0]), abs(arr[-1] - low))
            # update a new lowest and highest distnaces if necesary
            low = min(low, arr[0])
            high = max(high, arr[-1])

        return max_distance