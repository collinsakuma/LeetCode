class Solution:
    def equalSubstring(self, s, t, maxCost):
        n = len(s)
        # set starter of sliding window
        start = 0
        current_cost = 0
        max_length = 0

        # loop through range of string with end as the right side of the window
        for end in range(n):
            # find the cost to make string s to string t at index end
            current_cost += abs(ord(s[end]) - ord(t[end]))
            # if the current cost is greater than the maxCost allowed move the windows left side
            while current_cost > maxCost:
                # reduce the current cost by the value being removed from the window 
                current_cost -= abs(ord(s[start]) - ord(t[start]))
                # increment windows left side
                start += 1
            # check if a new max length has been round
            max_length = max(max_length, end - start + 1)

        return max_length