class Solution:
    def checkIfExist(self, arr):
        seen = set() # create a set of seen numbers

        # loop through numbers in arr
        for i in arr:
            # check if i * 2 is in seen or if i / 2 is in seen
            if i * 2 in seen or i / 2 in seen:
                return True
            else:
                # add i to set if condition not met
                seen.add(i)

        return False