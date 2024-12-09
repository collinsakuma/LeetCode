class Solution:
    def largestNumber(self, nums):
        arr = list(map(str, nums))
        # sort the list 
        arr.sort(key=lambda x:x*10, reverse=True)

        # if first number is 0 return 0
        if arr[0] == '0':
            return '0'
        
        return ''.join(arr)