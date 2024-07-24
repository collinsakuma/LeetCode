class Solution:
    def sortJumbled(self, mapping, nums):
        coded = []
        # loop through each number in nums list
        for num in nums:
            # empty string to hold the decoded number
            code = ''
            # loop through each digit in num convert num to a string to loop through
            for digit in str(num):
                # add the coded equivalent for each digit from mapping
                code += str(mapping[int(digit)])
            # add the de-coded number and the original number to a 2D array 
            coded.append([int(code), num])

        # sort the decoded and number array by the decoded value in assending order
        coded = sorted(coded, key=lambda x:x[0])

        # return a list of only the starting number in the new sorted order
        return [num[1] for num in coded]