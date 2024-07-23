from collections import Counter

class Solution:
    def frequencySort(self, nums):
        # output list to hold the sorted array by increasing frequency
        # current frequency array to be a temporary array of numbers with the same frequency
        output, temp_list = [], []
        # track the frequency of the current number in the list
        curr_freq = 0

        # create a count dict of nums
        count = Counter(nums)
        # sort the dictionary by the frequency that the number occurs in the list
        count = sorted(count.items(), key=lambda x:x[1])

        # loop through the tuple pairs in count
        for num, frequency in count:
            # if curr_frequency has not been set (first loop) set it to
            # the first numbers frequency
            if not curr_freq:
                curr_freq = frequency
            # if the frequency of the current number is the same as the previous
            if frequency == curr_freq:
                # add num to the temporary list "frequency" times
                temp_list += [num] * frequency
            # if the frequency of the current num is different from the previous
            else:
                # sort the numbers in the temporary list in descending order 
                # and add it to the final output list
                output += sorted(temp_list, reverse=True)
                # reset the temporary array to only the current number and its frequency
                temp_list = [num] * frequency
                # set the current frequency 
                curr_freq = frequency
        # if there are numbers in the temp list add them to the output sorted in 
        # descending order
        if temp_list:
            output += sorted(temp_list, reverse=True)

        return output
