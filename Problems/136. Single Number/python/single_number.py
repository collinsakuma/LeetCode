class Solution:
    def singleNumber(self, nums):
        dict = {} # create an empyt dict to hold number as key and value of how many times that number occurs in array.
        for i in nums:
        # loop through all elements in the array.
            if i not in dict:
            # if number is not in the dict create a new entry and set its default value to 1(I.E. one occurance of that number)
                dict[i] = 1
            else:
            # if the number is already in the dictionary as a key increment that keys value by 1(I.E. number occurs twice in the array)
                dict[i] += 1
        for i in dict:
            # now loop through the dictinary and find the key whos value is equal to 1 meaning that number on occured once in the array
            # return that number
            if dict[i] == 1:
                return i